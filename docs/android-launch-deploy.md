# Android launch: website switch (DRAFT, not deployed)

Branch `android-launch-1_4` (local only). Deploy it **only on Ron's go**, on launch day, after
Android 1.4 is published on Google Play (Play Console → Publish).

## What changes
- `netlify/functions/link.mjs`: `PLAY_URL` = https://play.google.com/store/apps/details?id=com.slowgoapp.slowgo.
  Android visits to /go, /card, /rental and /f/<shop> now go straight to Google Play. iPhone and
  computer links are unchanged (checked: `destinationFor` gives the same App Store URL as before).
- `android.html` (/android): "almost here" becomes "SlowGo is on Android", with Google's official
  "Get it on Google Play" badge, the support email, and an App Store link. No longer `noindex`;
  added to `sitemap.xml`. The path itself doesn't change (additive rule).
- `index.html`: the Google Play badge next to Apple's in the hero, the closer and the footer;
  "Live on the App Store and Google Play"; "Android 7.0 or later" (minSdk 24, read from the 1.4 APK);
  the FAQ "Android?" answer (HTML and the JSON-LD copy); the roadmap's "Later: Android" becomes
  "More states"; SoftwareApplication `operatingSystem` adds Android, `softwareVersion` 1.4.
- `google-play-badge.png`: Google's en_badge_web_generic.png, downloaded unaltered from
  play.google.com/intl/en_us/badges. The trademark line Google asks for sits under it.
- `llms.txt`: Android is on Google Play.
- `go/index.html` (the /go link's preview card and fallback): the card says "free on iPhone and Android" (and
  Arizona); if the link function ever failed, the page itself sends Android to Google Play.
- **The launch posts link slowgoapp.com/go** (Ron, 2026-10-13): after this deploy, /go sends Android phones to Google
  Play (the link function, `PLAY_URL`), iPhones to the App Store, computers home.

## Before deploying (launch day)
1. Replace the 3 `LAUNCH-DAY` placeholders with the date (`sitemap.xml` ×2, `llms.txt` ×1):
   `grep -rn LAUNCH-DAY SlowGo-Launch` must print nothing.
2. Check the Play link opens the live listing (not "not found") on a phone.
3. Count this month's Netlify deploys (free plan, about 20 a month). This switch is **1 deploy**.
4. Merge to `main` and push = the deploy. Ron's go first.

## After deploying
- Open slowgoapp.com/go from an Android phone (or emulator Chrome): it should land on Google Play. **This is the
  link the posts use, so check it before posting.**
- Paste slowgoapp.com/go into a Facebook post draft (don't post): the preview card should say "free on iPhone and
  Android". Facebook caches cards; if it shows the old line, use Facebook's Sharing Debugger to refresh it.
- slowgoapp.com/android shows the new page; slowgoapp.com/go on an iPhone still opens the App Store.

## Rollback
Set `PLAY_URL` back to `null` and redeploy: Android visits go to /android again.
