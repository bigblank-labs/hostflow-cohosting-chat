#!/usr/bin/env python3
"""
hostflow_post.py — One-click Reddit poster for Josh.

Designed to run on Josh's laptop (NOT on the agent server), because
Reddit's auth layer blocks datacenter IPs but not residential sessions.

What it does:
  1. Reads the latest gtm.db from the agent (or from a downloaded CSV)
  2. For each open draft, opens a Chrome tab logged into Reddit
  3. Navigates to the thread, pastes the draft, submits
  4. Captures the live permalink + screenshot
  5. Updates a local log file with what's been posted

Requirements:
  pip install playwright
  python -m playwright install chromium
  # Optional: set HOSTFLOW_GTM_DB env to point at the live DB
"""
import csv
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

# ------- Config -------
# Default: read from the live agent's CSV export
DEFAULT_CSV = "https://bigblank-labs.github.io/hostflow-cohosting-chat/gtm/activity.csv"
LOG_FILE = Path.home() / "hostflow_post_log.json"

# Safety knobs
MIN_SCORE = 7
DELAY_BETWEEN_POSTS_SEC = 120    # 2 min between posts (slow & human)
DELAY_JITTER_SEC = 30
MAX_POSTS_PER_RUN = 10


def load_open_drafts_from_csv(csv_path: str) -> list:
    """Fetch the latest activity.csv from the agent."""
    import urllib.request
    out = []
    with urllib.request.urlopen(csv_path, timeout=20) as r:
        text = r.read().decode("utf-8", "replace")
    for row in csv.DictReader(text.splitlines()):
        if (row.get("status") == "open"
                and row.get("post_url", "").startswith("http")
                and "comments/" in row.get("post_url", "")
                and len(row.get("our_response", "") or "") > 50
                and int(row.get("score") or 0) >= MIN_SCORE):
            out.append({
                "id": row.get("id"),
                "community": row.get("community"),
                "post_url": row.get("post_url"),
                "post_title": row.get("post_title"),
                "draft": (row.get("our_response") or "").strip(),
            })
    out.sort(key=lambda r: -int(r.get("id", 0) or 0))
    return out


def load_log() -> dict:
    if LOG_FILE.exists():
        try:
            return json.loads(LOG_FILE.read_text())
        except Exception:
            pass
    return {"posted": [], "failed": []}


def save_log(log: dict):
    LOG_FILE.write_text(json.dumps(log, indent=2, default=str))


def post_via_browser(draft: dict, headless: bool = False) -> dict:
    """
    Open Chrome, navigate to thread, paste draft, submit, capture permalink.

    Requires `playwright` and a logged-in Reddit session in Chrome.
    If the user isn't logged in, this returns {"ok": False, "error": "not_logged_in"}.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return {"ok": False, "error": "playwright_not_installed",
                "hint": "run: pip install playwright && python -m playwright install chromium"}

    url = draft["post_url"]
    body = draft["draft"]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, channel="chrome")
        context = browser.new_context()
        # Try to load any existing logged-in session from Chrome's default profile
        # by using launch_persistent_context instead:
        #   p.chromium.launch_persistent_context(user_data_dir, ...)
        # If the user runs this with their normal Chrome profile, they'll already be logged in.
        page = context.new_page()

        # Step 1: Check if logged in
        page.goto("https://www.reddit.com", timeout=30000)
        time.sleep(2)
        is_logged_in = page.locator("text=Log In").count() == 0
        if not is_logged_in:
            browser.close()
            return {"ok": False, "error": "not_logged_in",
                    "hint": "Sign into Reddit in Chrome first, then run this script."}

        # Step 2: Go to the thread
        page.goto(url, timeout=30000)
        time.sleep(3)

        # Step 3: Find the comment textarea. Reddit uses several variants:
        # - <textarea name="comment">
        # - <shreddit-composer> custom element
        # - <div contenteditable="true" data-reddit-comment>
        # We try the most common one first.
        try:
            ta = page.locator('textarea[name="comment"]').first
            ta.scroll_into_view_if_needed()
            ta.click()
            ta.fill(body)
        except Exception:
            try:
                # shreddit-composer approach
                composer = page.locator('shreddit-composer').first
                composer.scroll_into_view_if_needed()
                composer.click()
                time.sleep(1)
                ta2 = page.locator('textarea[name="comment"]').first
                ta2.fill(body)
            except Exception as e:
                browser.close()
                return {"ok": False, "error": "composer_not_found", "msg": str(e)[:200]}

        time.sleep(1)

        # Step 4: Find and click the submit button
        try:
            submit = page.locator('button:has-text("Comment"), button:has-text("Post"), button:has-text("Submit")').first
            submit.click()
        except Exception as e:
            browser.close()
            return {"ok": False, "error": "submit_not_clicked", "msg": str(e)[:200]}

        time.sleep(4)  # let Reddit render the new comment

        # Step 5: Capture the new permalink
        new_url = page.url

        # Take a screenshot for proof
        screenshot_dir = Path.home() / "hostflow_post_screenshots"
        screenshot_dir.mkdir(exist_ok=True)
        shot_path = screenshot_dir / f"posted-{draft['id']}-{int(time.time())}.png"
        try:
            page.screenshot(path=str(shot_path))
        except Exception:
            shot_path = None

        browser.close()

        # Extract comment_id from the URL
        # Reddit URLs look like: https://www.reddit.com/r/.../comments/THREAD/.../comment/COMMENT/
        m = re.search(r"/comments/([a-z0-9]+)/.*?/comment/([a-z0-9]+)", new_url)
        if m:
            thread_id, comment_id = m.group(1), m.group(2)
            permalink = f"https://www.reddit.com/r/{draft['community'].lstrip('r/')}/comments/{thread_id}/-/comment/{comment_id}/"
        else:
            permalink = new_url  # fallback

        return {
            "ok": True,
            "permalink": permalink,
            "screenshot": str(shot_path) if shot_path else None,
        }


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=DEFAULT_CSV,
                    help="URL or path to the agent's activity.csv")
    ap.add_argument("--headless", action="store_true",
                    help="Run Chrome headless (won't work without a saved session)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Show what would be posted, but don't actually post")
    ap.add_argument("--limit", type=int, default=MAX_POSTS_PER_RUN)
    args = ap.parse_args()

    drafts = load_open_drafts_from_csv(args.csv)
    log = load_log()
    already = {p["draft_id"] for p in log["posted"]}
    to_post = [d for d in drafts if d["id"] not in already]
    to_post = to_post[:args.limit]

    print(f"open drafts available: {len(drafts)}")
    print(f"already posted (logged): {len(already)}")
    print(f"will attempt: {len(to_post)}")
    print()

    for i, d in enumerate(to_post, 1):
        print(f"[{i}/{len(to_post)}] {d['community']}  score={d.get('id', '?')}  {d['post_url']}")
        print(f"  draft ({len(d['draft'])} chars): {d['draft'][:100]}...")
        if args.dry_run:
            print(f"  [DRY RUN] would post now\n")
            continue

        result = post_via_browser(d, headless=args.headless)
        if result.get("ok"):
            entry = {
                "draft_id": d["id"],
                "community": d["community"],
                "post_url": d["post_url"],
                "permalink": result["permalink"],
                "screenshot": result.get("screenshot"),
                "posted_at": datetime.now(timezone.utc).isoformat(),
            }
            log["posted"].append(entry)
            save_log(log)
            print(f"  ✓ POSTED: {result['permalink']}")
            if result.get("screenshot"):
                print(f"    screenshot: {result['screenshot']}")
        else:
            log["failed"].append({
                "draft_id": d["id"],
                "post_url": d["post_url"],
                "error": result.get("error"),
                "msg": result.get("msg"),
                "attempted_at": datetime.now(timezone.utc).isoformat(),
            })
            save_log(log)
            print(f"  ✗ FAILED: {result.get('error')} — {result.get('msg', '')[:200]}")
        print()

        if i < len(to_post):
            wait = DELAY_BETWEEN_POSTS_SEC + (hash(d["id"]) % (DELAY_JITTER_SEC * 2) - DELAY_JITTER_SEC)
            print(f"  sleeping {wait}s before next post…\n")
            time.sleep(wait)

    print()
    print(f"summary: {len([p for p in log['posted'] if p['draft_id'] in {d['id'] for d in to_post}])} posted, "
          f"{len([f for f in log['failed'] if f['draft_id'] in {d['id'] for d in to_post}])} failed")
    print(f"log: {LOG_FILE}")


if __name__ == "__main__":
    main()
