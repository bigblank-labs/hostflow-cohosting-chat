# Plan — Hostflow Small-Ticket Layer (Lead Magnets for Social)

## Why this layer exists

Josh confirmed (2026-09-15, ~last turn): "small ticket items can be okay or lead magnets for the social media content." Two distinct roles for cheap products:

1. **Lead magnets** — free or cheap opt-ins used to capture email addresses from social traffic. Friction: lowest possible. Conversion goal: collect the email.
2. **Tripwire offers** — $7-47 paid products that convert social audience to buyer. Profitability: thin margin, but breaks them into "customer" state for the funnel.

The chat funnel and the $200 Kit + $1,000 Mentorship already handle the high-end. This layer handles the *front door*.

## What we're shipping (8 small-ticket items)

### Free lead magnets (4 PDFs, email-gated)

| # | Name | Format | Gate |
|---|---|---|---|
| L1 | **"First 10 Nights: A New Cohost's Pricing Worksheet"** | 4-page PDF | Email-only signup |
| L2 | **"Cohosting Contract Clause-by-Clause Checklist"** | 6-page PDF | Email-only signup |
| L3 | **"Listing Audit 15-Point Self-Score Card"** | 3-page PDF | Email-only signup |
| L4 | **"Owner Outreach Email Templates (5 Scripts)"** | 5-page PDF | Email-only signup |

### Paid tripwires (4 small PDFs or templates, $7-$47)

| # | Name | Price | Format |
|---|---|---|---|
| T1 | **"Cohost Pricing Calculator (Notion template)"** | $17 | Notion template |
| T2 | **"Guest Screening Script Pack (10 industries)"** | $27 | 12-page PDF |
| T3 | **"Listing Photo Checklist"** | $7 | 2-page printable PDF |
| T4 | **"Cohost First 30 Days: Owner Onboarding Workbook"** | $37 | 18-page workbook |

## Funnel role

```
Reel/Short → Free lead magnet → email capture → 4-email sequence → $200 Kit OR $1,000 Mentorship

(Cheap tripwire path: Reel → $17 tripwire → thank-you page → $200 Kit upsell)
```

## Distribution

- Chat funnel: extend the recommendation step to surface L1 first ("start with the free worksheet"), then Kit/Mentorship after they download
- Email sequences: Resend (cheap + simple)
- Sales pages: 4 tripwire landings at `hostflow.me/l/<slug>` (or Chat GitHub Pages)

## What gets shipped this session

Three things, in order:

1. **Generate 4 lead magnets + 4 tripwire PDFs** (using same reportlab pipeline as the main Kit)
2. **Generate a landing-page builder skill** so I can spin up the 4 tripwire pages quickly (similar pattern to the chat interface — single HTML file, brand-matched, Stripe-ready)
3. **Update the chat to recommend free lead magnets first** for cooler buyers (the "free worksheet" angle), Kit for warm buyers, Mentorship for hot buyers

## Constraints (per watchlist)

- No exclamation marks, no emoji
- Hedged claims ("may support", "designed to")
- No fake testimonials
- Each lead magnet must be independently useful — not just a teaser for the Kit
- "PDF lessons" or template-style — consistent with the existing Kit format

## QA gate

After build, QA Bot reviews all 8 new assets against the same brand-voice / forbidden-claims scan used on the Kit.

## Timeline

This session — design + build + QA + ship to gh-pages alongside the existing Kit.

Then Josh QC. Then sales traffic.
