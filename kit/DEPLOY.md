# Hostflow — Deploy Guide

## What was built

Three deliverables at `/opt/data/work/hostflow/`:

1. **`hostflow-chat.html`** — Single-file chat interface. Hostflow brand tokens (navy #0B1220, blue #3D5AFE, Inter). 2-minute intake → product recommendation ($200 or $1,000) → Stripe checkout.
2. **`briefs/HOSTFLOW-001_Cohosting_Startup_Kit.md`** — CMO Brief for the $200 Kit product
3. **`watchlists/hostflow.md`** — Standing context (ICP, competitors, forbidden claims, voice rules)

Plus **`/opt/data/skills/select-agent/SKILL.md`** — the skill cmo/coo/qa use to delegate to specialists from the agency-agents registry (321 definitions across 18 divisions).

## Two ways to deploy

### Option A — Embed on hostflow.me (most visible)

Since hostflow.me is a Vercel-hosted React app (per the live CSS `index-rFU2L66R.css`), the cleanest embed path is:

1. Add a `/chat` route to the Vercel project that renders the chat interface.
   - The chat HTML lives at `hostflow-chat.html`. Convert the `<style>` block to a CSS module and the inline `<script>` to a React component (or just iframe it).
   - Easier: serve the HTML as a static file at `public/chat.html` and link to it from the nav (already done: see the "Chat" link in the topbar).
2. Update the hero on the homepage to send visitors to `/chat` instead of "Book a Call", OR keep both (chat for digital products, Book a Call for service).
3. Replace Stripe placeholder URLs in the chat HTML with your real Payment Links.

### Option B — Standalone (zero-touch, ship today)

The HTML file works as-is, no build step needed. Deploy:

```bash
# Vercel
cd /opt/data/work/hostflow
npx vercel deploy --prod public/  # copy hostflow-chat.html into ./public/

# Or GitHub Pages
mkdir hostflow-deploy && cd hostflow-deploy
git init
cp /opt/data/work/hostflow/hostflow-chat.html index.html
git add . && git commit -m "Hostflow chat v1"
gh repo create hostflow-chat --public --source=. --push
# Enable Pages on the repo
```

URL: `https://bigblank-labs.github.io/hostflow-chat/` (or your custom domain).

Then point hostflow.me/chat at that URL with a redirect, OR buy a domain like `chat.hostflow.me` and DNS it.

## Before going live — required swaps

1. **Stripe Payment Links.** Two URLs need real values:
   ```js
   const STRIPE_LINKS = {
     starter: 'https://buy.stripe.com/test_PLACEHOLDER_STARTER',  // ← replace
     mentor:  'https://buy.stripe.com/test_PLACEHOLDER_MENTOR'    // ← replace
   };
   ```
   In Stripe Dashboard → Payment Links → New → $200 / $1,000.

2. **Brand confirmation.** The bot reads "Hostflow — cohosting done right" without copyright/registered issues. If you have a registered trademark, update the `<title>` and footer text.

3. **Email delivery post-purchase.** The chat bot doesn't email yet. For the post-purchase drip, you'll need:
   - Stripe webhook → your endpoint → sends email via Resend / ConvertKit / Gmail
   - OR keep it simple: Stripe auto-emails a download link, and you send a manual 4-week follow-up sequence via Klaviyo

4. **Analytics.** Add Plausible (`<script defer data-domain="hostflow.me" src="...">`) or Vercel Analytics to the chat page so you see who uses it.

5. **QA verdict on the bot.** Per spec §04 QA-08 (UI + mobile), you should test:
   - Keyboard flow (Tab + Enter on chips)
   - Mobile viewport (≤ 480px wide)
   - "Loading / Empty / Error / Stale" states (currently: loading OK, empty OK, error not handled, no stale state)
   - The bug found during testing: if user clicks a chip while the next message is still typing, both clicks register. Need a guard.

## Open items before Friday

| Item | Owner | Blocker? |
|---|---|---|
| Stripe account — confirm one exists for josh@hostflow.me | Josh | yes |
| Replace placeholder Stripe links | COO | after Stripe |
| Decide: chat embedded on /chat route, or chat.hostflow.me | Josh | cosmetic |
| PDF modules — 10 of them | COO via pdf-engineer specialist | biggest content work |
| Email sequence — 4-week post-purchase | COO via nurture specialist | depends on email provider |
| QA review (brand voice, claim audit) | QA via brand-voice-auditor specialist | before any "live" |

## What I'd do next (if you want me to keep moving)

1. Get Stripe account credentials from you → wire real Payment Links
2. Dispatch COO to start the PDF modules draft using the `marketing-book-co-author` specialist
3. Have QA pre-audit the bot's copy before any embedding
4. Set up the email sequence scaffolding (ConvertKit is the cheapest with a free tier)
5. Ship the chat route on hostflow.me

Tell me which of the above you want handled next.
