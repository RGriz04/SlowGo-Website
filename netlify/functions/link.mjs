// ONE LINK SYSTEM (Ron, 2026-10-05): /go, /card, /rental and /f/<shop>.
// Added 2026-10-17 (drafts, not deployed): ad links /fb1 /fb2 /fb3 (Facebook ad variants) and /asa
// (Apple Search Ads), and one download link per town page, /t/<town> (counted as "t-<town>").
//   iPhone   → the App Store, tagged with the link's source (App Store Connect → Campaigns)
//   Android  → Google Play (PLAY_URL; /android if it is ever set back to null)
//   computer → the home page
//   preview bots (iMessage, Facebook, Slack…) → the /go page and its card; not counted
// Each human visit adds 1 to "<source>/<UTC day>" in Netlify Blobs. Totals only: no IP, no
// device, no user agent and nothing else about the visitor is stored. The user agent is read
// for this one routing decision and discarded.
import { getStore } from '@netlify/blobs';
import { FLEET_SHOPS } from '../fleet-shops.mjs';
import { AD_LINKS, TOWN_LINKS } from '../counted-links.mjs';

export const APP_ID = '6803226504';
// App Store Connect provider token (pt=), from the campaign link Ron generated 2026-10-05.
// Not a secret: it appears in every public App Store campaign link. Each link sets its own ct.
export const PROVIDER_TOKEN = '128827526';
// Google Play listing (Android launch, 1.4). Set back to null and Android visits go to /android.
export const PLAY_URL = 'https://play.google.com/store/apps/details?id=com.slowgoapp.slowgo';

const BOT = /bot|crawler|spider|facebookexternalhit|facebot|slackbot|twitterbot|linkedinbot|discordbot|whatsapp|telegrambot|skypeuripreview|embedly|pinterest|vkshare|redditbot|applebot|googlebot|bingbot|preview/i;

export function sourceFor(pathname) {
  const p = pathname.replace(/\/+$/, '').toLowerCase();
  if (p === '/go') return 'go';
  if (p === '/card' || p === '/cards') return 'card';   // /cards: a common mistype of the printed address, counted as card
  if (p === '/rental') return 'rental';
  if (AD_LINKS.includes(p.slice(1))) return p.slice(1);
  // A town's download link. The count key and App Store tag are "t-<town>": a "/" can't go in a
  // count key (keys are "<source>/<day>"), and Apple's ct tag allows 40 characters.
  const t = /^\/t\/([a-z0-9-]{1,38})$/.exec(p);
  if (t && TOWN_LINKS.includes(t[1])) return `t-${t[1]}`;
  const m = /^\/f\/([a-z0-9-]{1,40})$/.exec(p);
  if (m && FLEET_SHOPS.includes(m[1])) return m[1];
  return null;
}

export function platformFor(ua = '') {
  if (/iPhone|iPad|iPod/i.test(ua)) return 'ios';
  if (/Android/i.test(ua)) return 'android';
  return 'computer';
}

export function appStoreUrl(source) {
  const q = new URLSearchParams();
  if (PROVIDER_TOKEN) q.set('pt', PROVIDER_TOKEN);
  q.set('ct', source);
  q.set('mt', '8');
  return `https://apps.apple.com/app/apple-store/id${APP_ID}?${q}`;
}

export function destinationFor(platform, source, origin) {
  if (platform === 'ios') return appStoreUrl(source);
  if (platform === 'android') return PLAY_URL || `${origin}/android`;
  return `${origin}/`;
}

const day = () => new Date().toISOString().slice(0, 10);

export async function countScan(store, source) {
  const key = `${source}/${day()}`;
  const n = Number(await store.get(key)) || 0;
  await store.set(key, String(n + 1));
}

export default async (req) => {
  const url = new URL(req.url);
  const source = sourceFor(url.pathname);
  if (!source) return Response.redirect(`${url.origin}/`, 302);   // an unknown /f/ name: home, uncounted
  const ua = req.headers.get('user-agent') || '';
  if (BOT.test(ua)) {
    // Link previews keep the /go page's card. Not a scan.
    const page = await fetch(`${url.origin}/go/index.html`);
    return new Response(page.body, { status: 200, headers: { 'content-type': 'text/html; charset=utf-8' } });
  }
  const isPrefetch = /prefetch|prerender/i.test(req.headers.get('purpose') || req.headers.get('sec-purpose') || '');
  if (req.method === 'GET' && !isPrefetch) {
    try { await countScan(getStore({ name: 'link-scans', consistency: 'strong' }), source); }
    catch { /* a counting failure never blocks the visitor */ }
  }
  return new Response(null, { status: 302, headers: {
    location: destinationFor(platformFor(ua), source, url.origin),
    'cache-control': 'no-store',
  } });
};

export const config = { path: ['/go', '/go/', '/card', '/card/', '/cards', '/cards/', '/rental', '/rental/', '/f/:shop', '/f/:shop/',
  // Ad and town links (2026-10-17). Netlify config must be static, so the ad names are written out here;
  // tools/test-links.mjs fails if this list and AD_LINKS ever disagree.
  '/fb1', '/fb1/', '/fb2', '/fb2/', '/fb3', '/fb3/', '/asa', '/asa/', '/t/:town', '/t/:town/'] };
