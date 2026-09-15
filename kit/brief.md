# Hostflow — Project Brief #001

**Brief ID:** HOSTFLOW-001
**Project:** Hostflow digital products ($200 kit + $1,000 mentorship)
**Author:** CMO Bot (Snow)
**Date:** 2026-09-15
**Status:** DRAFT — ready for COO execution

## Situation

Josh runs Hostflow (hostflow.me) — currently positioned as a premium STR co-hosting service ($300K+ rev generated, +38% lift on managed units). He wants to **expand into digital products** without abandoning the service.

ICP for the digital products: **aspiring co-hosts** who want to manage other people's properties, not own. They Google things like "how to become an Airbnb cohost", "cohost contract template", "cohost pricing". This is a different audience from the current Hostflow service (property owners hiring us to cohost for them) — the digital products sell *to* people who want to *become* cohosts themselves.

Josh's directive (verbatim, 2026-09-15):
- Cohosting Startup Kit: $200 flat, all PDF lessons
- Mentorship course: $1,000

Distribution: chat-bot interface on hostflow.me, embedded replacing the "Book a Call" hero. Bot recommends the right product based on a 2-min intake. Stripe checkout inline.

## Objective

Ship **Cohosting Startup Kit ($200)** as the first digital product, end-to-end, via the chat-bot funnel, in the next sprint cycle.

## Audience / ICP (per watchlist/hostflow.md)

| Segment | Trigger | Recommended product |
|---|---|---|
| New — never cohosted before | "I want to be an Airbnb cohost" | Starter Kit ($200) |
| Already cohosting — scaling | "I have a few owners, want more" | Mentorship ($1,000) |
| Considering (STR owner) | "Should I take on cohosting for others" | Starter Kit ($200) |
| Existing Hostflow service customer | Upsell | Mentorship ($1,000) |

## Channel(s)

- Primary: hostflow.me (chat interface, replacing "Book a Call" hero)
- Secondary: standalone at chat.hostflow.me (live already)
- Tertiary: Telegram (post-MVP, requires Telegram bot token)

## Assets Required (Delegate to agency-agents specialists)

| Asset | Owner bot | Specialist (from registry) |
|---|---|---|
| Lead funnel / intake copy | CMO | `marketing-conversion-rate-optimizer` or `marketing-funnel-builder` |
| Starter Kit PDF modules (10) | COO | `marketing-book-co-author` (chapters) + `engineering-pdf-engineer` (layout) + `design-*-designer` (cover) |
| Pricing page copy ($200) | CMO | `marketing-landing-page-copywriter` or `marketing-headline-copywriter` |
| Email sequence (4-week post-purchase) | COO | `marketing-lifecycle-marketer` or `marketing-email-nurture-sequence` |
| Stripe checkout setup | COO | `engineering-stripe-integration-engineer` |
| Brand voice audit (every page) | QA | `*-brand-voice-auditor` (in testing or specialized) |
| Link-checker + cookie verification | QA | `testing-link-checker` |

## Definition of Done

HOSTFLOW-001 is DONE when:
- [ ] Cohosting Startup Kit PDFs are assembled (10 modules × 8-15 pages each)
- [ ] Kit content covers: cohost contracts (3 fee models), pricing calculator, guest-screening scripts, listing audit checklist, owner outreach email templates, 4-week post-purchase email sequence
- [ ] chat.hostflow.me (or hostflow.me/chat) live with the bot recommending the right product based on 2-min intake
- [ ] Stripe Payment Link for `$200` Cohosting Starter Kit is wired and tested end-to-end (test mode → live)
- [ ] QA verdict = PASS on every asset (PDFs + landing copy + chat bot responses + checkout flow)
- [ ] One real test purchase completed by Josh from his own device (sanity check)
- [ ] First customer-facing post-mortem recorded to `~/.hermes/shared/venture-os/results/`

## Deadline

**Target: 7 calendar days from kickoff** (soft target, no external commitment — per spec §01 "no launch date or spending budget assumed"). Owner can revise with reason.

## Success Metric

- 3 real purchases within 14 days of go-live
- Refund rate ≤ 5%
- Average review rating on the Kit ≥ 4.5/5 (after first 5 reviews)

Secondary:
- Chat-bot-to-checkout conversion ≥ 25%
- Time-to-product-recommendation < 90 seconds

## Constraints

- **Budget:** None committed. Stripe account + domain are existing. PDF generation can use ReportLab (free, already installed). No paid tools without explicit Josh approval.
- **Forbidden claims:** No income guarantees. No "Airbnb approved/certified." No "100% booked" or passive-income language. No fake testimonials.
- **Brand voice (Hostflow brand):** Premium, calm, owner-voice. Confident mentor-talking-to-serious-host. No exclamation, no emoji, mono labels for any doses.
- **Tone (Snow Studio system voice):** Hedged claims only ("may support", "designed to"). Power-of-the-Gods tone — confident without hype.

## Open Questions for Josh

1. Stripe account — do you have one, or do I need to set up a fresh account under your name?
2. Should the chat bot be on hostflow.me itself (replacing "Book a Call"), or at chat.hostflow.me (separate route)?
3. For the Kit's first 10 modules, are there existing Hostflow contracts/templates I can repackage, or do the specialists need to draft from scratch?
4. Mentorship ($1,000) — out of scope for this Brief. When do you want to kick that off?
5. Telegram bot — out of scope here. Worth a follow-up Brief later.

---

## SOURCE

`/opt/data/work/hostflow/watchlists/hostflow.md` (standing context, locked 2026-09-15), chat history 2026-09-15 (Josh directives: ICP=aspiring co-host, $200 kit + $1,000 mentorship, embed chat on hostflow.me, 3-managers each handle their own role).

## CONFIDENCE

Medium-High on the product strategy (Josh gave clear directives). Medium on timing (no committed deadline). Low on conversion math (no baseline data yet for Hostflow funnel).

Raising confidence to High requires: (a) one cycle of real purchases to see actual conversion, (b) Stripe account confirmed + tested, (c) PDF modules drafted and reviewed for quality.

## NEXT

COO picks up this Brief:
1. Confirm Stripe account access with Josh
2. Pull the agency-agents `pdf-engineer`, `email-nurture-sequence`, `landing-page-copywriter` specialists from the registry
3. Dispatch them in parallel — PDFs draft + landing copy + email sequence
4. Wire Stripe Payment Link inline
5. Hand the resulting assets to QA for review before any "live" label
