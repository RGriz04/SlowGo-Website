# SlowGo — Netlify Export

Static site for **slowgoapp.com**. Six hand-written HTML pages plus Netlify
configuration. No build step, no framework, no `node_modules`.

## What's in this folder

```
SlowGo-Launch/
├── index.html       # The launch page
├── privacy.html     # Privacy Policy — served at /privacy
├── terms.html       # Terms of Service — served at /terms
├── support.html     # Support & FAQ — served at /support
├── safety.html      # How SlowGo is built to be careful — served at /safety
├── 404.html         # Not-found page (Netlify serves this by convention)
├── netlify.toml     # Build config + security/caching headers
├── _redirects       # HTTPS + www → apex, and clean URLs for the non-index pages
├── robots.txt       # Allow all crawlers
├── sitemap.xml      # Five live pages, each with lastmod
├── llms.txt         # Plain-language site summary for language models
├── og-image.png     # 1200×630 social preview card
├── go/index.html    # /go — App Store doorway page, carries the OG card
├── app-store-badge.svg  # Apple's official badge artwork, unaltered
├── screenshots/     # Four App Store screens used on index.html, webp + png
│                   #   (see screenshots/SOURCES.md for provenance)
└── README.md        # This file
```

## Legal pages

The LLC is formed and the legal docs are live and versioned. `privacy.html` and
`terms.html` are **mirrors** — the source of truth is the Markdown in the SlowGo
app repo. When those change, the `.md` and the `.html` are updated together, and
the `lastmod` in `sitemap.xml` moves with them.

Both pages carry a visible "Last updated" date. Do not edit the legal copy here
without syncing the app repo in the same pass.

## The App Store link

`/go` is a **page**, `go/index.html`, not a `_redirects` rule. Everything that
points at the app — the hero badge, the footer badge, the QR code in
`brand-assets/qr/`, anything printed — links to `/go` and never to
`apps.apple.com` directly, so the destination stays editable here.

### Why it stopped being a redirect

It began as a 302 straight to the App Store. That worked for people and broke
for link previews: a redirect carries no HTML, so when `/go` was shared in
iMessage there were no Open Graph tags to read and the preview was improvised
from whatever sat at the end of the hop — an App Store screenshot. The homepage
rendered the branded green card and `/go` rendered something else entirely.

One card everywhere. `go/index.html` carries the homepage's Open Graph and
Twitter tags **verbatim**, changing only `og:url`. Preview crawlers read those
and stop. Everyone else is handed to the store three ways, because each can fail
on its own:

1. `<meta http-equiv="refresh" content="0;...">` — works with JavaScript off
2. `location.replace(...)` — faster, and leaves no history entry, so *back* from
   the App Store does not land on `/go` and bounce the rider out again
3. the visible badge — if both are blocked

**If the homepage's card ever changes, change it in `go/index.html` in the same
pass.** The entire point of the file is that the two match. Nothing checks this
automatically.

The page is `noindex, follow` and deliberately absent from `sitemap.xml`. It is
a doorway, not something that should rank against the homepage.

**Trade-off on record:** a person tapping `/go` may catch roughly 100 ms of
charcoal before the store opens. That is the price of controlling the preview,
and it was accepted knowingly. Printed QR codes are unaffected — they encode
`/go` and always did.

### Why `/go` is still two lines in `_redirects`

They are **rewrites (200)** now, not redirects, pointing at `go/index.html`.
They look redundant next to a real file at that path, and they are not: `/go`
is the address printed on the QR code and it has **no trailing slash**. Left to
Netlify's directory handling a bare `/go` would 301 to `/go/`, or 404 outright
if someone switched off the "Pretty URLs" toggle — the same toggle this file
already warns against depending on for `/privacy` and `/terms`. For a URL
already printed on signage that cannot be reprinted, neither is acceptable.
These two lines make `/go` resolve at 200, directly, regardless of the
dashboard. Keep them.

They are written `200!`, forced, and **the bang is load-bearing**. Netlify
silently ignores a redirect rule whose path collides with something that already
exists in the publish directory — and `go/` is a real directory. Unforced, these
lines look right, deploy without complaint, and do nothing at all: `/go` 301s to
`/go/` and the rule never fires. This was measured on production, not reasoned
about. If you ever see `/go` answering 301, the bang has gone missing.

`app-store-badge.svg` is Apple's own artwork, byte-for-byte as they serve it.
Their guidelines require the real badge and forbid altering it — do not inline
it, recolour it, or redraw it. It is the white variant because the hero is dark.

The Smart App Banner (`<meta name="apple-itunes-app" content="app-id=6803226504">`)
is in the `<head>` of all seven pages, so Safari on iPhone offers the install
banner wherever someone lands, not only on the homepage.

`_redirects` rewrites `/privacy` and `/terms` to the `.html` files at status 200,
so the address bar stays clean. Those two URLs are referenced by the App Store
privacy-policy field and by in-app links, so the rules must not be removed in
favour of Netlify's "Pretty URLs" dashboard toggle, which someone could turn off.

## The safety page

`safety.html` is served at `/safety`; `/how-its-built` is a 301 to it, so a link
written either way lands in the same place.

Every factual claim on that page comes from the app repo: `APP-REVIEW-NOTES.md`
(the ratified product constitution, the speed policy, the coverage and outage
behaviour, the validation language) and `SlowGo-Privacy-Policy.md`. Do not add a
claim to it that is not in one of those two files, and keep the validation
wording **measured** — no "field-tested", "driven", or "road-tested". No human
has ridden these routes in a cart yet, and nothing on this site may read as
though one has.

There is no claim table on the page itself; this is where a claim is traced to
its source. One row per section that makes a checkable assertion:

| Section | Source in the app repo |
|---|---|
| "One rule, and the rest follows" | `APP-REVIEW-NOTES.md` — "How routes are chosen" (≤35 build, 36–45 disclosed in amber, never routed **along** a confirmed >45 road, crossings disclosed separately) |
| "Checked before you can start" | `APP-REVIEW-NOTES.md` — the end-to-end speed check, *"Checking speed limits…"*, *"We couldn't confirm the speed limits out here."*, partial check treated as failure |
| "Paths get a second question" | `APP-REVIEW-NOTES.md` ~142–148 and the questions-table row *"What are the 'cart-path checks' in the location list?"* — materiality threshold, *"Checking path access…"* holds Start only while pending, *"Includes 0.4 mi of paths — cart access not confirmed"*, *"Couldn't check path access — ride these sections with local knowledge"*, both startable, absent tag is absence of data |
| "When we don't know, we say so" | `APP-REVIEW-NOTES.md` — "Where the speed limits come from", the judged-by-road-type label, "35 mph and under" reserved for fully posted routes |
| "No route beats a bad route" | `APP-REVIEW-NOTES.md` — the refusal screen, *"That one's a NoGo."* |
| "Your eyes are still in charge" | `APP-REVIEW-NOTES.md` — "cart legality varies by municipality and SlowGo does not adjudicate it"; `SlowGo-Terms-of-Service.md` §4.3 |
| "Your privacy, in one breath" | `SlowGo-Privacy-Policy.md` — §3 provider table, §5 on-device storage |
| "How it's tested" | `APP-REVIEW-NOTES.md` — "How well validated is each?" (the two signed runs, 2026-08-08, neither state ridden in a cart) |

The page describes the cart-path check as **disclosure**, never as a legality
verdict. That distinction is the app's, not a hedge added here: an absent
`golf_cart` tag is an absence of data. Nothing on this site may say the app
determines whether a route is cart-legal — the Terms disclaim exactly that.

## SEO and metadata

- **Unique `<title>` and meta description** on every page.
- **`rel=canonical`** on all five live pages, absolute URLs. `404.html` has none
  by design — it is `noindex, follow` and deliberately absent from the sitemap.
- **Open Graph + Twitter card** on all five live pages, all pointing at
  `og-image.png` (1200×630) with alt text.
- **Structured data** in `index.html`, as two JSON-LD blocks:
  - `Organization` (BackRoad Apps LLC) + `WebSite`, as an `@graph`
  - `FAQPage`, generated from the on-page FAQ with the wording unchanged. If you
    edit an FAQ answer on the page, edit the matching `text` in the JSON-LD in
    the same pass - they are kept in step by hand, not generated.
  - `SoftwareApplication`, in the same `@graph`. Every field comes from the
    iTunes lookup API for id 6803226504 rather than from memory - version,
    price, minimum iOS, release date, file size, content rating. Re-check it
    when a new version ships; `softwareVersion` and `datePublished` go stale
    on their own.

    It carries **no `aggregateRating`**, on purpose: the listing has no ratings
    yet, and an invented one is precisely what Google penalises. Add it when
    there are real reviews. `applicationCategory` is `TravelApplication`
    because `NavigationApplication` is not a schema.org value; the intent
    lives in `applicationSubCategory` instead.

    Its `url`/`downloadUrl` point at `apps.apple.com` directly - the one place
    on the site that does not use `/go`. This is crawler metadata, not a link
    handed to a person, and a redirect would only weaken it.
- **`llms.txt`** describes the product honestly: released, Florida and Georgia
  only, the green/amber/NoGo system, and the no-accounts privacy posture.

## Deploy — Git (preferred)

1. Push to the connected repo (root of repo = root of site).
2. **Netlify → Add new site → Import from Git** → pick the repo.
3. **Build command:** *(leave blank)*
   **Publish directory:** `.`
4. Connect the `slowgoapp.com` domain.

Pushing `main` deploys to Netlify. There is no staging site.

## Deploy — drag & drop (fallback)

1. Go to <https://app.netlify.com/drop>.
2. Drag this entire folder onto the drop zone.
3. Netlify creates a site at a random `*.netlify.app` URL.
4. **Site settings → Domain management → Add custom domain → `slowgoapp.com`**.
5. Set `slowgoapp.com` as the **Primary domain** (not `www`).

## The screenshots

The four screens on the homepage are the **v1.0 App Store submission images**,
downscaled from the 1290x2796 originals in `~/Desktop/AppStore/6.9in/`.
They are not captures of the store page. `screenshots/SOURCES.md` records which
original each one came from, with the SHA-256 of the original, and how to
regenerate the derivatives.

Each ships as WebP with a PNG fallback in a `<picture>` element - about half the
bytes, still no build step. Replace both formats together or the fallback drifts.

Do not add device frames, crop, or upscale. The site shows the screens as they
actually appear in the app.

## Forms - one, and it is the town request

`index.html` has **one** live form using Netlify Forms: `town-request`.

- It carries `data-netlify="true"` and `data-netlify-honeypot="bot-field"`.
- A hidden static stub (`town-request`) sits at the top of `<body>` so Netlify's
  build-time HTML scraper detects it even though the live one is JS-enhanced.
- It carries `<input type="hidden" name="form-name" ... />` so the async fetch
  submit routes to the right form.

The two email-signup forms that used to sit in the hero and the closing section
were **retired at launch**, along with their hidden stub - the app is out, so
there is nothing left to sign up for. Removing them from the HTML stops new
submissions, but it does **not** delete what Netlify already stored: the old form
and its submissions have to be deleted in the Netlify dashboard under
**Site -> Forms**. That is a dashboard action, not a repo change.

Submissions post via `fetch` with an inline confirmation and no redirect. A non-OK
response restores the button label and shows an error rather than reading as success.

After first deploy:

1. **Site settings → Forms → Form notifications → Add notification → Email.**
2. Point it at the address you want signups to land in (e.g. `hello@slowgoapp.com`).
3. Submit a test from the live site to confirm it arrives.
4. Submissions are also visible in **Site → Forms** in the Netlify dashboard.

Spam protection: the honeypot (`bot-field`) is wired automatically. If you start
seeing spam, add a reCAPTCHA in the form settings.

## Custom domain checklist

- [ ] Add `slowgoapp.com` as custom domain in Netlify
- [ ] Set as **primary domain**
- [ ] HTTPS certificate provisioned (auto, ~1 minute)
- [ ] `_redirects` collapses `www` and `http` → `https://slowgoapp.com`
- [ ] Test: `curl -I https://slowgoapp.com` returns 200
- [ ] Test: `curl -I http://www.slowgoapp.com` returns 301 → apex
- [ ] Test: `curl -I https://slowgoapp.com/nonsense` returns 404, not 200

## What's intentionally NOT here

- No analytics, no tracking, no cookies
- No press, about, or blog pages
- No stock photography or illustration — the only images are the three real app
  screenshots and the social card
- No build step and no dependencies

## Still open

The favicon is an inline SVG data URI in each `<head>`. It works in modern
browsers but does not cover iOS home-screen or Android install. Still needed:

- `apple-touch-icon.png` — 180×180, no alpha
- `favicon.ico` — 32×32 (or multi-res 16/32/48)
- `icon-192.png`, `icon-512.png`
- `site.webmanifest`, once the icons exist

## Updating the site

Edit the HTML directly and push. There is no build step, no framework, no
`node_modules`. If you add or remove a page, update `sitemap.xml` (including
`lastmod`) and `llms.txt` in the same commit.

## Page weight

| Page | HTML | Notes |
|---|---|---|
| `404.html` | ~10 KB | |
| `support.html` | ~14 KB | |
| `safety.html` | ~15 KB | |
| `privacy.html` | ~33 KB | |
| `terms.html` | ~43 KB | |
| `index.html` | ~76 KB | plus ~207 KB of screenshots (WebP), lazy-loaded |

The four WebP screenshots weigh about what the three PNGs they replaced did. The
PNG fallbacks (~406 KB) sit in the repo but are only fetched by a browser that
cannot take WebP.

Google Fonts (Fraunces + Inter + JetBrains Mono) load over the network on first
paint. `og-image.png` (~59 KB) is fetched by social crawlers, not on page render.

—

*Life's better at 15 mph.*
