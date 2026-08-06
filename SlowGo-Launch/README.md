# SlowGo — Netlify Export

Static site for **slowgoapp.com**. Five hand-written HTML pages plus Netlify
configuration. No build step, no framework, no `node_modules`.

## What's in this folder

```
SlowGo-Launch/
├── index.html       # The launch page
├── privacy.html     # Privacy Policy — served at /privacy
├── terms.html       # Terms of Service — served at /terms
├── support.html     # Support & FAQ — served at /support
├── 404.html         # Not-found page (Netlify serves this by convention)
├── netlify.toml     # Build config + security/caching headers
├── _redirects       # HTTPS + www → apex, and clean URLs for the legal pages
├── robots.txt       # Allow all crawlers
├── sitemap.xml      # Four live pages, each with lastmod
├── llms.txt         # Plain-language site summary for language models
├── og-image.png     # 1200×630 social preview card
├── screenshots/     # Three app screenshots used on index.html
└── README.md        # This file
```

## Legal pages

The LLC is formed and the legal docs are live and versioned. `privacy.html` and
`terms.html` are **mirrors** — the source of truth is the Markdown in the SlowGo
app repo. When those change, the `.md` and the `.html` are updated together, and
the `lastmod` in `sitemap.xml` moves with them.

Both pages carry a visible "Last updated" date. Do not edit the legal copy here
without syncing the app repo in the same pass.

`_redirects` rewrites `/privacy` and `/terms` to the `.html` files at status 200,
so the address bar stays clean. Those two URLs are referenced by the App Store
privacy-policy field and by in-app links, so the rules must not be removed in
favour of Netlify's "Pretty URLs" dashboard toggle, which someone could turn off.

## SEO and metadata

- **Unique `<title>` and meta description** on every page.
- **`rel=canonical`** on all four live pages, absolute URLs. `404.html` has none
  by design — it is `noindex, follow` and deliberately absent from the sitemap.
- **Open Graph + Twitter card** on all four live pages, all pointing at
  `og-image.png` (1200×630) with alt text.
- **Structured data** in `index.html`, as two JSON-LD blocks:
  - `Organization` (BackRoad Apps LLC) + `WebSite`, as an `@graph`
  - `FAQPage`, generated from the on-page FAQ with the wording unchanged
  - A `SoftwareApplication` node is still **TODO** — it needs the real App Store
    URL and is left out rather than shipped pointing at a placeholder.
- **`llms.txt`** describes the product honestly: pre-launch, Florida and Georgia
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

## Forms — already wired

`index.html` has three live forms using Netlify Forms: two `waitlist` forms (one
in the hero, one in the waitlist section) and one `town-request` form.

- Live forms carry `data-netlify="true"` and `data-netlify-honeypot="bot-field"`.
- Two hidden static stubs (`waitlist`, `town-request`) sit at the top of `<body>`
  so Netlify's build-time HTML scraper detects both forms even though the live
  ones are JS-enhanced.
- Each carries `<input type="hidden" name="form-name" ... />` so the async fetch
  submit routes to the right form.

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
| `privacy.html` | ~33 KB | |
| `terms.html` | ~43 KB | |
| `index.html` | ~76 KB | plus ~200 KB of screenshots, lazy-loaded |

Google Fonts (Fraunces + Inter + JetBrains Mono) load over the network on first
paint. `og-image.png` (~59 KB) is fetched by social crawlers, not on page render.

—

*Life's better at 15 mph.*
