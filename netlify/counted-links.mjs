// Counted links beyond /go, /card, /rental and /f/<shop> (2026-10-17, drafts; not deployed).
// Each one goes through netlify/functions/link.mjs exactly like /go: iPhone -> App Store tagged
// ct=<name>, Android -> /android until PLAY_URL is set, computers -> home, preview bots -> the
// /go card (uncounted). slowgo-report shows them in its Share links table.
//
// TO ADD AN AD LINK: add its name here AND its two paths to config.path in link.mjs
// (tools/test-links.mjs checks the two agree).
export const AD_LINKS = ['fb1', 'fb2', 'fb3', 'asa'];

// One download link per published town page: slowgoapp.com/t/<name>, counted as "t-<name>".
// The /cart-rules hub, 38 town and county pages, and the Florida/Georgia/Arizona state pages
// (drafts/town-pages-2026-10-16 at 019d338, tools/town-pages/build.py --links). Captiva and Gulf Breeze held.
// TO ADD A TOWN: add one line here, then deploy. No change to link.mjs is needed.
export const TOWN_LINKS = [
  'cart-rules',
  'st-pete-beach',
  'dunedin',
  'mount-dora',
  'miami-lakes',
  'pine-island',
  'jekyll-island',
  'st-simons-island',
  'tybee-island',
  'pinellas-county',
  'clearwater',
  'st-augustine-beach',
  'flagler-beach',
  'fort-walton-beach',
  'mexico-beach',
  'port-st-joe',
  'key-biscayne',
  'apollo-beach',
  'port-richey',
  'keaton-beach',
  'steinhatchee',
  'north-port',
  'oldsmar',
  'winter-garden',
  'oviedo',
  'clermont',
  'st-cloud',
  'celebration',
  'lynn-haven',
  'cutler-bay',
  'palmetto-bay',
  'tequesta',
  'nassau-county',
  'st-johns-county',
  'peachtree-city',
  'port-wentworth',
  'rome',
  'woodstock',
  'marana',
  'florida',
  'georgia',
  'arizona',
];
