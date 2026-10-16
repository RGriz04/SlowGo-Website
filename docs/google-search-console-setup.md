# Google Search Console: steps for Ron (2026-10-17)

Everything here is done by Ron, signed in to his own Google account. No agent submits anything to Google.

## Where things stand (checked 2026-10-16)

- **Ownership is already verified once, by the HTML tag.** The home page has carried
  `<meta name="google-site-verification" …>` since 2026-10-05 (website commit 5d24847). That verifies a
  **URL-prefix property** for `https://slowgoapp.com/`. Keep the tag: Google re-checks it.
- **DNS lives at Netlify DNS.** The name servers are `dns1`–`dns4.p06.nsone.net` (Netlify's), and the
  registrar is Namecheap. So a DNS record is added in Netlify, not at Namecheap.
- The only TXT record today is the email one (`v=spf1 include:spf.improvmx.com ~all`, for ImprovMX
  forwarding). A Google TXT record sits next to it and doesn't touch email.

## Step 1 (optional but better): add a Domain property

A Domain property covers `slowgoapp.com`, `www`, `http` and `https` in one place.

1. Go to https://search.google.com/search-console. Click the property menu (top left), then **Add property**.
2. Choose **Domain**. Type `slowgoapp.com`, then **Continue**.
3. Google shows a TXT record that starts `google-site-verification=…`. Click **Copy**.
4. In a new tab, open https://app.netlify.com. Click **Domains**, then **slowgoapp.com**, then **Add new record**.
   - Record type: **TXT**
   - Name: leave it as `@` (or blank, meaning slowgoapp.com itself)
   - Value: paste the `google-site-verification=…` text
   - TTL: leave the default
   - **Save**. Don't change or delete the existing ImprovMX TXT record.
5. Back in Search Console, click **Verify**. If it says it can't find the record, wait 10 minutes and try
   again (Netlify DNS is usually quick; Google says it can take up to a day).

Skipping Step 1 is fine: the URL-prefix property you already have works for everything below.

## Step 2: submit the sitemap

1. In Search Console, pick the property (the Domain one if you made it, otherwise `https://slowgoapp.com/`).
2. Left menu: **Sitemaps**.
3. Under **Add a new sitemap**, type `sitemap.xml` and click **Submit**.
4. Status should read **Success**. The sitemap lists the home page, /privacy, /terms, /safety, /support
   and (once deployed) /business and the town pages.

## Step 3: after the favicon deploy, ask Google to look again

Google shows the site's icon in search results only once it has re-crawled the home page and found a
crawlable favicon that is a multiple of 48 px. The new set (favicon.ico with 16/32/48, 48/96/192/512 PNGs,
apple-touch-icon 180) goes out with the next website deploy.

After that deploy is live:

1. Check it yourself first: open https://slowgoapp.com/favicon.ico and https://slowgoapp.com/icon-192.png.
   Both should show the SlowGo icon.
2. In Search Console, click the search bar at the top (**Inspect any URL**) and paste `https://slowgoapp.com/`.
3. Click **Request indexing**. Do the same for `https://slowgoapp.com/business` once it's live.
4. Then wait. Google says the icon can take days to weeks to appear, and it's Google's choice whether
   it shows one at all.

Google's rules for the icon: https://developers.google.com/search/docs/appearance/favicon-in-search

## Not needed

- No new account, no payment, no Google Analytics, nothing added to the app.
- Request indexing has a small daily quota. Use it for the home page and new pages only.
