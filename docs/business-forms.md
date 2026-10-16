# /business and the fleet setup form (drafts, 2026-10-17)

Status: **drafts on local branch `drafts/site-2026-10-17`. Not deployed, not pushed.** No form has been
submitted to Netlify; everything was checked on a local static server only.

## What's on the pages

**/business** (`SlowGo-Launch/business.html`, linked from the home page footer, in the sitemap): one
section and one short form for each audience. Five Netlify forms:

| Form name | Who | Required | Optional |
|---|---|---|---|
| `business-rental` | rental shops | shop (`business`), `email`, town served (`town`), inquiry (`message`) | contact `name`, `phone`, `fleet_band` (carts rented) |
| `business-dealer` | dealers | dealership, email, town served, inquiry | name, phone, `fleet_band` (carts sold a year) |
| `business-community` | communities / HOAs | community, email, town, inquiry | name, phone |
| `business-town` | towns / tourism boards | organisation, email, town, inquiry | name, phone |
| `business-partner` | realtors / partners | company, email, town, inquiry | name, phone |

Fields follow Ron's privacy ruling of 2026-10-17 (required = business name, contact email, service town,
inquiry; optional = contact name, phone, fleet-size band). Website, role, home count and the free-number
cart counts were dropped. `fleet_band` is one of `1-10`, `11-25`, `26-50`, `51-100`, `100+`. Each form
says "Please don't include renter personal information or payment details." above the button, and a
Privacy link beside the button goes to `/privacy#business-inquiries` (the anchor the policy update adds).
Netlify registers the new field names (`phone`, `fleet_band`) at the deploy that ships them. Each form
shows its next steps on the page after sending.

The setup form (`fleet-setup`) follows the same rule for its contact part: shop name, email and the new
`town` (town served) are required; contact name, shop phone (`shop_phone`) and `fleet_band` are optional.
Without a shop phone the app shows no Call button; `draft-fleet.mjs` flags it.

**/business/setup?t=<token>** (`SlowGo-Launch/business-setup.html`): fleet step 2, for a shop that said
yes. Not linked anywhere, `noindex, nofollow` in the page and as an `X-Robots-Tag` header, not in the
sitemap. One Netlify form, `fleet-setup`, with a file field. It refuses to send without a well-formed
`?t=` token. The token is a filter, not a lock (a static page can't keep a secret): the real check is
offline, when `tools/fleet-setup/draft-fleet.mjs` compares it with the tokens Ron issued
(`tools/fleet-setup/new-token.mjs`, stored only in `~/.slowgo/fleet-setup-tokens.json`).

It collects: logo upload (PNG/JPG/SVG, 4 MB cap in the page) and optional brand colour; shop phone;
return spot (address, plus a pin on a MapLibre map); hours; up to 8 picks with optional notes; a
welcome line; the dealer's call-for-service number; card quantity and shipping address; and a required
box accepting the fleet terms.

## Spam

- Every form has Netlify's honeypot (`data-netlify-honeypot="bot-field"`, hidden off-screen). Netlify
  "quietly rejects" a submission whose honeypot is filled, and doesn't even keep it as spam.
- Netlify also runs every submission through Akismet; flagged ones go to the Spam list, not the
  Verified list, and notifications are for verified submissions.
- **No reCAPTCHA** for now: it adds a Google widget and a privacy line, and the town-request form has
  managed without one. Netlify's built-in reCAPTCHA is one attribute (`data-netlify-recaptcha="true"`)
  if spam gets through.
- The setup form also refuses to submit without a token, and the draft tool refuses an unissued token.

Source: https://docs.netlify.com/manage/forms/spam-filters/

## Notifications to Ron: built in

Netlify can email each verified submission (also Slack or a webhook). Ron sets it in the Netlify app:
**Project configuration → Notifications → Emails and webhooks → Form submission notifications → Add
notification → Email notification**, pick the form (or "any form"), and the address. Netlify's email
comes from formresponses@netlify.com; because each form has a field named `email`, the notification's
Reply-to is the person who filled it in, so Ron can just reply.

Source: https://docs.netlify.com/manage/forms/notifications/

## Automatic reply with next steps: NOT built in (the honest version)

**Netlify Forms does not send an email to the person who filled in the form.** Its notifications go to
the site owner only. Options, cheapest first:

1. **What's built now: the next steps appear on the page** the moment the form sends (a numbered list
   under "Thanks. Ron reads every one of these himself."). Free, nothing to set up, works on day one.
   Ron's own reply (Reply-to is already the sender) is the first email they get.
2. **Zapier or n8n** (Netlify's suggested route for "greater control of form-triggered emails"):
   trigger = new Netlify form submission, action = send an email from Ron's Gmail. Needs a Zapier or
   n8n account (Ron makes it; agents never create accounts) and Gmail access granted to it. Zapier's
   free plan has a monthly task cap; check its current pricing before relying on it.
3. **A Netlify Function on the "form submitted" event** that sends the reply through an email-sending
   service (Resend, Postmark, Amazon SES…). Needs an account with that service, an API key in Netlify's
   environment variables, and DNS records (SPF/DKIM) for slowgoapp.com in Netlify DNS so the mail isn't
   junked. It also adds a processor to the Privacy Policy. Most control, most setup. **Not built**: per
   "show the trade before building", this waits for Ron to pick 2 or 3.

My recommendation: keep option 1 until submissions are more than a handful a week; then option 2.

Source for the event function: https://docs.netlify.com/build/functions/trigger-on-events/ (the
`formSubmitted` event fires for verified submissions).

## Plan limits (Netlify, read 2026-10-16)

SlowGo's Netlify team is on the **credit-based Free plan** (memory: ~20 production deploys a month =
300 credits at 15 credits each).

| Fact | Value | Source |
|---|---|---|
| Form submissions on credit-based plans | **"free and unlimited … no submission limits or tier levels for forms"** | https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/billing-faq-for-credit-based-plans ; credit table: https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-plans/how-credits-work/ |
| Free plan credits | 300 (pricing page: "300 credit limit"); production deploy = 15 credits; you cannot buy extra credits on Free; when credits run out **every site on the team pauses** ("Site not available"), forms included | https://www.netlify.com/pricing/ and the billing FAQ above |
| File uploads per submission | **8 MB per form request** (all fields and files together), **one file per field**, upload **times out after 30 s** | https://docs.netlify.com/manage/forms/setup/ |
| File-upload storage allowance on credit plans | **Not stated** anywhere I could find; the credit table lists Forms as free with no upload line | as above |
| Legacy plans (for comparison, not ours) | Free tier is metered; Netlify's own example of "Forms Level 0" is 100 submissions and 10 MB of uploads a month; going over on legacy Free pauses all sites | https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-legacy-plans/billing-faq-for-legacy-plans/ ; https://docs.netlify.com/manage/forms/usage-and-billing/ |
| Function compute (if an auto-reply function is ever added) | 10 credits per GB-hour; web requests 2 credits per 10,000 | how-credits-work, above |

**Do logo uploads work on our plan?** Yes, as far as the docs say: file fields are a standard Netlify
Forms feature, forms are free and unlimited on credit plans, and the page keeps a logo to 4 MB, well
under the 8 MB request cap. Two caveats: (1) Netlify doesn't state an upload-storage figure for credit
plans, so **Ron should glance at Forms → Usage after the first few setups**; (2) Netlify's docs say forms
that collect personal information "need extra configuration" and point to a paid add-on (Very Good
Security); the setup form collects business contact details and a shipping address, which is the
privacy line in `SlowGo-Privacy-Policy.business-contact-DRAFT.md`. **Fallback if uploads ever fail or
get capped:** the form already says "too big, or no file handy? Email it to hello@slowgoapp.com", and
the draft tool takes a logo from a local file (`--logo`), so an emailed logo works the same way.

Uploaded files are reached from the Netlify dashboard (the submission links to Netlify's copy). The
draft tool never downloads them; Ron saves the file and passes `--logo`.

## The map pin, and Stadia

- The setup page loads **MapLibre GL JS 4.7.1** from unpkg and Stadia Maps' `alidade_smooth` style,
  **with no key in the page**: Stadia authenticates a web page by its domain.
- **Checked 2026-10-16 (9 requests, spaced):** tiles answer **200 for a localhost origin** and **401 for
  `https://slowgoapp.com`**. So **slowgoapp.com is not on the SlowGo property's allowed domains today.**
  On the live site the map would fail; the page then hides it and says "type the address above and Ron
  will place the pin", and the form still works. Seen on localhost in Chrome: the map loads, a tap drops
  a draggable pin and fills the hidden lat/lng fields; the 401 fallback fires (tested against a local
  server that answers 401).
- **Needs Ron (Stadia dashboard):** add `slowgoapp.com` to the property's allowed domains. No new
  service, and it uses the Starter plan Ron already pays for (map views count against its credits; a
  setup form is a handful of views per shop).

## The flow end to end

1. A shop sends the `business-rental` (or `business-dealer`) form. Ron gets the Netlify email.
2. Ron replies from his own email. If it's a yes: `node tools/fleet-setup/new-token.mjs "Shop Name"`
   prints the private link; Ron pastes it into his email.
3. The shop fills `/business/setup?t=…`. Ron gets the Netlify email.
4. Ron exports the submission JSON from Netlify (and saves the logo), then runs
   `node tools/fleet-setup/draft-fleet.mjs submission.json --logo logo.png [--id shortname]`.
   Everything lands in `~/Desktop/SlowGo/fleet-setup/waiting-for-ron-approval/<id>-<date>/` (README
   with flags and a checklist, profile.js in the app's fleet format, the app's own validator output,
   extras.json, link, QR PNG/SVG, card PNG/PDF, picks matched to the local places build).
5. Ron runs the routing checks, sends the proof, and (with a release and a batched deploy) the shop goes
   live. Nothing in step 4 publishes anything.

## Before deploying any of this

- **LEGAL:** the Privacy Policy covers only the waitlist and town-request forms. The business forms and
  the setup form need the business-contact amendment (draft next to the policy) in the same deploy or
  earlier. See `SlowGo-Privacy-Policy.business-contact-DRAFT.md`.
- **LEGAL:** the setup page's terms link is a placeholder. The fleet agreement is a draft in the app
  repo (`docs/plans/fleet-agreement-draft.md`, f16-fleet), marked "to be reviewed by an attorney before
  the first paid contract". Remove the page's DRAFT banner only when the link points at published terms.
- Turn on the email notification for the six forms (above).
- Stadia allowed domain (above).
- Deploy budget: these pages, the favicon set, the counted links and the town pages can all go in one
  batched deploy.
