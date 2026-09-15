# Hostflow Catalog — Everything Josh needs to QC

## Digital products (live now, QC pending)

| Tier | Code | Name | Price | Link |
|---|---|---|---|---|
| Free | L1 | First 10 Nights Worksheet | FREE | [PDF](../../small-tickets/L1_first_10_nights_pricing_worksheet.pdf) |
| Free | L2 | Contract Checklist | FREE | [PDF](../../small-tickets/L2_cohosting_contract_checklist.pdf) |
| Free | L3 | Listing Audit Card | FREE | [PDF](../../small-tickets/L3_listing_audit_self_score_card.pdf) |
| Free | L4 | Outreach Email Scripts | FREE | [PDF](../../small-tickets/L4_owner_outreach_email_templates.pdf) |
| Tripwire | T1 | Pricing Calculator | $17 | [PDF guide](../../small-tickets/T1_cohost_pricing_calculator_NOTION_TEMPLATE_INSTRUCTIONS.pdf) + Notion template (delivered on purchase) |
| Tripwire | T2 | Guest Screening Scripts | $27 | [PDF](../../small-tickets/T2_guest_screening_script_pack.pdf) |
| Tripwire | T3 | Photo Checklist | $7 | [PDF](../../small-tickets/T3_listing_photo_checklist.pdf) |
| Tripwire | T4 | First 30 Days Workbook | $37 | [PDF](../../small-tickets/T4_cohost_first_30_days_workbook.pdf) |
| Main | Starter | Cohosting Startup Kit | $200 | [PDF (21 pages)](Cohosting_Startup_Kit.pdf) |
| Main | Mentor | Cohosting Mentorship | $1,000 | Cohort — Stripe / scheduling pending Josh |

## Status

- **10 digital products built:** 4 free, 4 tripwires, 1 $200 Kit, 1 $1,000 Mentorship brief
- **1 chat interface:** Live with role-based routing, small-ticket warm-up panel, main reco card
- **2 QA verdicts passed:** QA-001 (Kit + chat), QA-002 (small-tickets layer)
- **1 routing bug fixed:** role-based tree routing was bypassed by `nextBot()` walking sequentially; now skips non-matching nodes
- **1 Notion card updated:** AgenticOS master plan logged this session's work

## Still pending (out of session scope)

- Stripe account + 6 Payment Links (Josh's identity required)
- Email capture service for free downloads (Resend / Klaviyo choice)
- Notion template delivery for T1 (Notion account under Hostflow workspace)
- Brand voice claim "we have +38% revenue lift" — left out of digital product copy because it's a service metric

## How to QC

1. Open https://bigblank-labs.github.io/hostflow-cohosting-chat/ — click through the 2-minute chat, see the small-ticket panel, see the recommendation
2. Click each small-ticket PDF (table above) — verify content + brand voice
3. Click the full Kit PDF (21 pages) — verify chapter structure, cross-references
4. Check the role-based routing fix: pick "I'm new" + "US (single state)" — should go straight to reco. Pick "scaling" + "Pricing + contracts" — should also go to reco (skips geo). Pick "considering" — should go straight to reco (skips geo + bottleneck).

Mark anything that's off; Snow will iterate after your QC pass.
