# HostFlow Post — local one-click poster for Reddit

This runs on YOUR laptop (not on the agent server), using YOUR logged-in
Chrome browser session. Reddit only blocks server-side datacenter IPs —
your residential IP + logged-in session bypass that.

## Setup (one-time, 5 min)

```bash
# 1. Install Python deps
pip install playwright

# 2. Install Chromium for Playwright
python -m playwright install chromium

# 3. Make sure you're signed into reddit.com in Chrome
#    (Open Chrome, go to reddit.com, sign in as snowstudiogg)
```

## Usage

```bash
# Dry run — see what would be posted
python hostflow_post.py --dry-run

# Post top 5 drafts, 2 min between each
python hostflow_post.py --limit 5

# Post all open drafts (up to 10)
python hostflow_post.py
```

The script reads the latest open drafts from the live audit page
(https://bigblank-labs.github.io/hostflow-cohosting-chat/gtm/activity.csv),
opens each Reddit thread in a Chrome tab, pastes the draft, submits, and
saves the live permalink + a screenshot to `~/hostflow_post_log.json`.

## After posting

Paste your live permalinks into the daily Notion card so the agent can mark
them as `posted` in the audit sheet:

https://www.notion.so/3eaa6870764c81889773cba3cbf8d3a7
