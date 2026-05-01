# SlowGo — Netlify Export

Single-page launch site for **slowgoapp.com**. One self-contained HTML file plus Netlify configuration. No build step required.

## What's in this folder

```
netlify-export/
├── index.html       # The launch page (was "SlowGo Launch.html")
├── netlify.toml     # Build config + security/caching headers
├── _redirects       # HTTPS + www → apex redirects
├── robots.txt       # Allow all crawlers
├── sitemap.xml      # Single-URL sitemap
└── README.md        # This file
```

## Deploy — drag & drop (fastest)

1. Go to <https://app.netlify.com/drop>.
2. Drag this entire `netlify-export/` folder onto the drop zone.
3. Netlify creates a site at a random `*.netlify.app` URL.
4. **Site settings → Domain management → Add custom domain → `slowgoapp.com`**.
   DNS is presumably already pointed; HTTPS provisions automatically (Let's Encrypt).
5. Set `slowgoapp.com` as the **Primary domain** (not `www`).

## Deploy — Git (preferred long-term)

1. Push the contents of this folder to a Git repo (root of repo = root of site).
2. **Netlify → Add new site → Import from Git** → pick the repo.
3. **Build command:** *(leave blank)*
   **Publish directory:** `.`
4. Connect the `slowgoapp.com` domain as above.

## Forms — already wired

Both waitlist forms in `index.html` use Netlify Forms:

- `data-netlify="true"`, `name="waitlist"`, `data-netlify-honeypot="bot-field"`
- Hidden static `<form name="waitlist" netlify ...>` at the top of `<body>` so Netlify's
  build-time HTML scraper detects the form even though the live forms are JS-enhanced.
- `<input type="hidden" name="form-name" value="waitlist" />` so the async fetch submit
  routes to the right form.

After first deploy:

1. **Site settings → Forms → Form notifications → Add notification → Email notification.**
2. Point it at the address you want signups to land in (e.g. `hello@slowgoapp.com`).
3. Submit a test from the live site to confirm it arrives.
4. Submissions are also visible in **Site → Forms → waitlist** in the Netlify dashboard.

Spam protection: the honeypot (`bot-field`) is wired automatically. If you start seeing
spam, add a reCAPTCHA in the form settings.

## Custom domain checklist

- [ ] Add `slowgoapp.com` as custom domain in Netlify
- [ ] Set as **primary domain**
- [ ] HTTPS certificate provisioned (auto, ~1 minute)
- [ ] `_redirects` collapses `www` and `http` → `https://slowgoapp.com`
- [ ] Test: `curl -I https://slowgoapp.com` returns 200
- [ ] Test: `curl -I http://www.slowgoapp.com` returns 301 → apex

## Email signup form notification

The form will capture submissions immediately on first deploy, but you won't *receive*
them until you set up a notification:

**Site → Forms → Notifications → Add notification → Email notification**

## What's intentionally NOT here

- No analytics, no tracking, no cookies
- No Privacy / Terms pages (add when LLC formed)
- No press, about, or blog pages
- No images, photos, or stock illustrations
- Minimal favicon (inline SVG data URI in `<head>`)

## Updating the site

Edit `index.html` directly. Drag the folder back onto Netlify Drop, or push the change to Git.
There is no build step, no framework, no node_modules.

## Page weight

`index.html` is ~50KB minified-equivalent. Google Fonts (Fraunces + Inter + JetBrains Mono)
are loaded over the network on first paint. Total first-load is well under 200KB including fonts.

—

*Life's better at 15 mph.*
