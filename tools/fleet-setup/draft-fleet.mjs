#!/usr/bin/env node
// Draft everything for one fleet setup submission, for Ron to approve. LOCAL ONLY: it reads files,
// writes files, and sends, fetches and publishes nothing (no network at all).
//
//   node tools/fleet-setup/draft-fleet.mjs <submission.json> [--logo <file>] [--out <dir>]
//        [--tokens <file>] [--places <places.sqlite>] [--app <app worktree>] [--id <link-name>] [--no-token-check]
//
// <submission.json> is a fleet-setup submission as Netlify exports it (Forms -> fleet-setup ->
// the submission's JSON, or the API's /submissions list): an object, or an array of them, with
// the fields under "data". An uploaded logo arrives as a link to Netlify's copy; this script never
// downloads it: save the file from the Netlify dashboard and pass --logo.
//
// Writes <out>/<shop-id>-<date>/ (default out: ~/Desktop/SlowGo/fleet-setup/waiting-for-ron-approval):
//   README.txt            what was drafted, what's flagged, Ron's checklist
//   profile.js            the shop in the app's fleet format (schema 1, utils/fleetProfile.js on f16-fleet),
//                         every check "unchecked" until Ron runs the routing checks
//   profile-check.txt     the app's own validateFleetProfile() on it, as a shipping profile
//   extras.json           what the form collects that schema 1 has no field for (hours, welcome line,
//                         brand colour, service number, card order, picks 6-8)
//   link.txt              the /f/ link and the one line for netlify/fleet-shops.mjs
//   qr-<id>.png / .svg    QR code for https://slowgoapp.com/f/<id>
//   card-<id>.png / .pdf  the printable card, from the existing rental-card design
//   picks.json / picks.csv  each pick matched against the local places build (Overture + OSM, r3)
//   submission.json       the submission as received
// Nothing is published: adding the shop to the app, the site's fleet list and printing all stay Ron's.
import { readFileSync, writeFileSync, mkdirSync, existsSync, copyFileSync, unlinkSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { createRequire } from 'node:module';
import { deflateSync } from 'node:zlib';
import path from 'node:path';
import os from 'node:os';
import { pathToFileURL, fileURLToPath } from 'node:url';
import { readTokens, TOKENS_FILE } from './new-token.mjs';

const HOME = os.homedir();
const DEFAULTS = {
  out: path.join(HOME, 'Desktop/SlowGo/fleet-setup/waiting-for-ron-approval'),
  places: path.join(HOME, 'Desktop/SlowGo/places-builds/2026-09-23.1-r3/places.sqlite'),
  app: path.join(HOME, 'dev/SlowGo-fleet-demo'),      // has utils/fleetProfile.js and the card template
  appRepo: path.join(HOME, 'dev/SlowGo'),             // fallbacks: git show f16-fleet:<path>, node_modules
  fonts: process.env.SLOWGO_FONTS || path.join(HOME, 'Desktop/SlowGo/brand/SlowGo-Canva-Brand-Kit/fonts'),
  chrome: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
};
const CARD_TEMPLATE = 'docs/drafts/fleet-outreach/rental-card/rental-card.template.html';
const PROFILE_JS = 'utils/fleetProfile.js';
const SLUG_RE = /^[a-z0-9-]{1,40}$/;   // the site's link rule and FLEET_SLUG_RE in the app

// ---------------------------------------------------------------- parsing the submission
export function normalizeSubmission(raw) {
  const s = Array.isArray(raw) ? raw[0] : raw;
  if (!s || typeof s !== 'object') throw new Error('submission.json: expected an object or an array of them');
  const d = s.data && typeof s.data === 'object' ? s.data : s;
  const str = (k) => (typeof d[k] === 'string' ? d[k].trim() : d[k] == null ? '' : String(d[k]).trim());
  const picks = [];
  for (let i = 1; i <= 8; i++) {
    const name = str(`pick_${i}_name`);
    if (name) picks.push({ n: i, name, note: str(`pick_${i}_note`) });
  }
  const logo = d.logo && typeof d.logo === 'object' ? d.logo : str('logo') ? { url: str('logo') } : null;
  return {
    id: s.id || null, created: s.created_at || null, form: s.form_name || null,
    token: str('token'), business: str('business'), kind: str('kind') === 'dealer' ? 'dealer' : 'rental',
    name: str('name'), email: str('email'), town: str('town'), fleetBand: str('fleet_band'), shopPhone: str('shop_phone'), servicePhone: str('service_phone'),
    brandColor: /^#[0-9a-f]{6}$/i.test(str('brand_color')) ? str('brand_color').toUpperCase() : null,
    brandColorRaw: str('brand_color'),
    returnAddress: str('return_address'), returnLabel: str('return_label'),
    returnLat: Number.parseFloat(str('return_lat')), returnLng: Number.parseFloat(str('return_lng')),
    hours: str('hours'), welcome: str('welcome'), picks,
    cardQty: Number.parseInt(str('card_qty'), 10) || null, shipName: str('ship_name'), shipAddress: str('ship_address'),
    terms: str('terms') === 'accepted', logo, honeypot: str('bot-field'),
  };
}

export function slugify(name) {
  return name.toLowerCase().replace(/['’]/g, '').normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/&/g, ' and ')
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 40).replace(/-+$/, '');
}
export function shortNameFor(name, max = 12) {
  if (name.length <= max) return name;
  const words = name.split(/\s+/);
  let out = '';
  for (const w of words) { const next = out ? `${out} ${w}` : w; if (next.length > max) break; out = next; }
  return out || name.slice(0, max);
}
export function initialsFor(name) {
  const w = name.replace(/&/g, ' ').split(/\s+/).filter((x) => /[A-Za-z0-9]/.test(x) && !/^(the|of|and)$/i.test(x));
  return w.slice(0, 3).map((x) => x.replace(/[^A-Za-z0-9]/g, '')[0].toUpperCase()).join('') || 'S';
}
export function phoneE164(p) {
  const digits = String(p || '').replace(/\D/g, '');
  const ten = digits.length === 11 && digits[0] === '1' ? digits.slice(1) : digits;
  if (ten.length !== 10) return null;
  return { e164: `+1${ten}`, label: `(${ten.slice(0, 3)}) ${ten.slice(3, 6)}-${ten.slice(6)}` };
}

// ---------------------------------------------------------------- picks vs the places build
const norm = (s) => s.toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '').replace(/&/g, ' and ')
  .replace(/['’]/g, '').replace(/[^a-z0-9]+/g, ' ').replace(/\b(the|at|on|of)\b/g, ' ').replace(/\s+/g, ' ').trim();
export function nameScore(a, b) {
  const A = norm(a), B = norm(b);
  if (!A || !B) return 0;
  if (A === B) return 1;
  const ta = new Set(A.split(' ')), tb = new Set(B.split(' '));
  const inter = [...ta].filter((t) => tb.has(t)).length;
  const jac = inter / new Set([...ta, ...tb]).size;
  // Whole-word containment ("Strachan's Ice Cream" in "Strachan's Ice Cream & Desserts"), never a
  // stray letter: the shorter name needs real words and at least half the longer one's.
  const [sh, lo] = ta.size <= tb.size ? [ta, tb] : [tb, ta];
  const contain = [...sh].every((t) => lo.has(t)) && [...sh].some((t) => t.length >= 3) && sh.size / lo.size >= 0.5 ? 0.85 : 0;
  const cover = inter / ta.size;   // how much of what the shop typed is in the place's name
  return Math.max(jac, contain, 0.9 * cover * (inter >= 1 ? 1 : 0) * (ta.size >= 2 || inter === ta.size ? 1 : 0.5));
}
const EMOJI = { food: '🍽️', grocery: '🛒', park: '🌳', gas: '⛽', coffee: '☕', bar: '🍺', pharmacy: '💊', beach: '🏖️',
  ice_cream: '🍦', loop: '🔁', dessert: '🍰', golf: '⛳', lake: '🌊', viewpoint: '🌅', square: '🏛️', breakfast: '🥞' };
export const emojiFor = (cat) => EMOJI[cat] || '📍';
const km = (a, b) => {
  const R = 6371, r = Math.PI / 180, dLat = (b.lat - a.lat) * r, dLng = (b.lng - a.lng) * r;
  const h = Math.sin(dLat / 2) ** 2 + Math.cos(a.lat * r) * Math.cos(b.lat * r) * Math.sin(dLng / 2) ** 2;
  return 2 * R * Math.asin(Math.sqrt(h));
};

/** Every named place within radiusKm of center, read-only, through the sqlite3 command line tool. */
export function placesNear(dbFile, center, radiusKm = 25) {
  const dLat = radiusKm / 111, dLng = radiusKm / (111 * Math.cos(center.lat * Math.PI / 180));
  // Through the build's R-tree per category (rt_<cat>, id = places.rid): no full scan.
  const tables = execFileSync('sqlite3', ['-readonly', dbFile, "select name from sqlite_master where type='table' and sql like 'CREATE VIRTUAL TABLE%rtree%'"])
    .toString().split('\n').map((t) => t.trim()).filter((t) => /^rt_[a-z_]+$/.test(t));
  const box = `minlat >= ${center.lat - dLat} and maxlat <= ${center.lat + dLat} and minlng >= ${center.lng - dLng} and maxlng <= ${center.lng + dLng}`;
  const sql = `select p.detail from places p where p.rid in (${tables.map((t) => `select id from ${t} where ${box}`).join(' union ')})
    and json_extract(p.detail,'$.name') is not null`;
  const out = execFileSync('sqlite3', ['-readonly', '-json', dbFile, sql], { maxBuffer: 512 * 1024 * 1024 }).toString().trim();
  if (!out) return [];
  return JSON.parse(out).map((r) => JSON.parse(r.detail)).filter((p) => km(center, p) <= radiusKm);
}

export const MATCH = 0.75, CHECK = 0.5;
export function matchPick(pick, places, center) {
  const scored = places.map((p) => ({ p, score: nameScore(pick.name, p.name), km: km(center, p) }))
    .filter((x) => x.score >= CHECK)
    .sort((x, y) => y.score - x.score || x.km - y.km);
  if (!scored.length) return { status: 'unmatched', candidates: [] };
  const best = scored[0];
  // Same top score at another spot more than 300 m away: a chain or a common name. Ron picks.
  // (1.5 km: one big park often has several records a few hundred metres apart; chain stores don't.)
  const rivals = scored.filter((x) => x !== best && best.score - x.score < 0.05 && km(best.p, x.p) > 1.5);
  const status = best.score < MATCH ? 'check' : rivals.length ? 'ambiguous' : 'matched';
  const view = (x) => ({ pid: x.p.pid, name: x.p.name, cat: x.p.cat, lat: x.p.lat, lng: x.p.lng,
    city: x.p.address?.city || null, score: Number(x.score.toFixed(2)), mi: Number((x.km / 1.609).toFixed(1)), sources: x.p.sources });
  return { status, best: view(best), candidates: scored.slice(0, 5).map(view) };
}

// ---------------------------------------------------------------- QR (PNG written directly) and card
function qrMatrix(appRepo, text) {
  const req = createRequire(path.join(appRepo, 'package.json'));
  const QRCode = req('qrcode-terminal/vendor/QRCode');
  const L = req('qrcode-terminal/vendor/QRCode/QRErrorCorrectLevel');
  const q = new QRCode(-1, L.M); q.addData(text); q.make();
  const n = q.getModuleCount();
  return { n, dark: (r, c) => q.isDark(r, c) };
}
export function qrSvg(m, url, { quiet = 4, fg = '#1E3A2B', bg = '#FFFFFF' } = {}) {
  let d = '';
  for (let r = 0; r < m.n; r++) for (let c = 0; c < m.n; c++) if (m.dark(r, c)) d += `M${c + quiet} ${r + quiet}h1v1h-1z`;
  const size = m.n + quiet * 2;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${size} ${size}" shape-rendering="crispEdges" role="img" aria-label="QR code for ${url}"><rect width="${size}" height="${size}" fill="${bg}"/><path d="${d}" fill="${fg}"/></svg>`;
}
const CRC = (() => { const t = new Int32Array(256); for (let n = 0; n < 256; n++) { let c = n; for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1; t[n] = c; } return t; })();
const crc32 = (buf) => { let c = -1; for (const b of buf) c = CRC[(c ^ b) & 0xff] ^ (c >>> 8); return (c ^ -1) >>> 0; };
const chunk = (type, data) => { const len = Buffer.alloc(4); len.writeUInt32BE(data.length); const td = Buffer.concat([Buffer.from(type), data]); const crc = Buffer.alloc(4); crc.writeUInt32BE(crc32(td)); return Buffer.concat([len, td, crc]); };
export function qrPng(m, { scale = 20, quiet = 4 } = {}) {
  const size = (m.n + quiet * 2) * scale;
  const raw = Buffer.alloc((size + 1) * size, 255);
  for (let y = 0; y < size; y++) {
    raw[y * (size + 1)] = 0;
    const r = Math.floor(y / scale) - quiet;
    for (let x = 0; x < size; x++) {
      const c = Math.floor(x / scale) - quiet;
      if (r >= 0 && c >= 0 && r < m.n && c < m.n && m.dark(r, c)) raw[y * (size + 1) + 1 + x] = 0;
    }
  }
  const ihdr = Buffer.alloc(13); ihdr.writeUInt32BE(size, 0); ihdr.writeUInt32BE(size, 4); ihdr[8] = 8; ihdr[9] = 0;
  return Buffer.concat([Buffer.from([137, 80, 78, 71, 13, 10, 26, 10]), chunk('IHDR', ihdr), chunk('IDAT', deflateSync(raw)), chunk('IEND', Buffer.alloc(0))]);
}

function readAppFile(opts, rel) {
  const local = path.join(opts.app, rel);
  if (existsSync(local)) return { text: readFileSync(local, 'utf8'), from: local };
  const text = execFileSync('git', ['-C', opts.appRepo, 'show', `f16-fleet:${rel}`]).toString();
  return { text, from: `${opts.appRepo} (git show f16-fleet:${rel})` };
}

// The printed address fits the QR panel up to about 24 characters; longer, print the bare domain
// (as the dealer sample cards do) and flag a shorter id.
export const CARD_URL_MAX = 24;
export const urlText = (id) => (`slowgoapp.com/f/${id}`.length <= CARD_URL_MAX ? `slowgoapp.com/f/${id}` : 'slowgoapp.com');

function renderCard(opts, sub, id, svg, dir) {
  const { text: tpl } = readAppFile(opts, CARD_TEMPLATE);
  const shop = sub.business;
  const dealer = sub.kind === 'dealer';
  const size = shop.length <= 16 ? 88 : shop.length <= 22 ? 76 : shop.length <= 28 ? 62 : 52;   // as render.cjs
  const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
  const html = tpl.replace('{{QR}}', svg).replaceAll('{{FONTS}}', pathToFileURL(opts.fonts).href).replace('{{SHOP}}', esc(shop))
    .replace('{{SHOPSIZE}}', size).replace('{{HEADLINE}}', dealer ? '' : 'New in town?')
    .replace('{{BYLINE}}', dealer ? 'Your cart from' : 'Courtesy of').replace('{{URLTEXT}}', urlText(id));
  const tmp = path.join(dir, `.card-${process.pid}.html`);
  writeFileSync(tmp, html);
  const png = path.join(dir, `card-${id}.png`), pdf = path.join(dir, `card-${id}.pdf`);
  const base = ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files', `--user-data-dir=${path.join(os.tmpdir(), 'slowgo-card-chrome')}`];
  execFileSync(opts.chrome, [...base, `--screenshot=${png}`, '--window-size=2250,1350', '--force-device-scale-factor=1', pathToFileURL(tmp).href], { stdio: 'ignore' });
  // PDF: one card per page at 7.5 x 4.5 in (the 2250 x 1350 artwork at 300 dpi). Print size is Ron's call.
  const sheet = path.join(dir, `.sheet-${process.pid}.html`);
  writeFileSync(sheet, `<!doctype html><style>@page{size:7.5in 4.5in;margin:0}html,body{margin:0}img{width:7.5in;height:4.5in;display:block}</style><img src="${pathToFileURL(png).href}">`);
  execFileSync(opts.chrome, [...base, '--no-pdf-header-footer', `--print-to-pdf=${pdf}`, pathToFileURL(sheet).href], { stdio: 'ignore' });
  unlinkSync(tmp); unlinkSync(sheet);
  return { png, pdf };
}

// ---------------------------------------------------------------- the profile
export function buildProfile(sub, id, picksMatched, area) {
  const ph = phoneE164(sub.shopPhone);
  const today = new Date().toISOString().slice(0, 10);
  const unchecked = (from) => ({ result: 'unchecked', setting: 'slow-only', from, on: today, note: 'drafted; Ron runs the routing check' });
  const hasPin = Number.isFinite(sub.returnLat) && Number.isFinite(sub.returnLng);
  const picks = picksMatched.filter((m) => m.best && m.status !== 'unmatched').slice(0, 5).map((m) => ({
    emoji: emojiFor(m.best.cat),
    label: m.pick.name.slice(0, 24),
    subLabel: `Shop pick · ${(m.pick.note || m.best.cat || 'place').replace(/_/g, ' ')}`.slice(0, 80),
    lat: m.best.lat, lng: m.best.lng,
    check: unchecked(sub.kind === 'rental' ? 'returnSpot' : 'shop'),
  }));
  return {
    schema: 1, id, kind: sub.kind, name: sub.business.slice(0, 40), shortName: shortNameFor(sub.business), initials: initialsFor(sub.business),
    logo: { light: id, dark: `${id}-dark` },
    phone: ph ? ph.e164 : sub.shopPhone, phoneLabel: ph ? ph.label : sub.shopPhone,
    area,
    returnSpot: sub.kind === 'rental'
      ? { label: `${sub.business}${sub.returnLabel ? ` · ${sub.returnLabel}` : ''}`.slice(0, 80), lat: hasPin ? sub.returnLat : null, lng: hasPin ? sub.returnLng : null, check: unchecked('shop') }
      : null,
    rentalDays: sub.kind === 'rental' ? 7 : null,
    picks,
  };
}

function areaFrom(places, center, fallbackState) {
  const near = places.filter((p) => km(center, p) <= 3 && p.address?.city);
  const count = {};
  for (const p of near) { const k = `${p.address.city}|${p.address.state || ''}`; count[k] = (count[k] || 0) + 1; }
  const top = Object.entries(count).sort((a, b) => b[1] - a[1])[0];
  if (!top) return { name: '?', state: fallbackState || '?' };
  const [name, state] = top[0].split('|');
  return { name, state: state || fallbackState || '?' };
}

// ---------------------------------------------------------------- main
export async function draft(file, opts) {
  const flags = []; const flag = (s) => flags.push(s);
  const raw = JSON.parse(readFileSync(file, 'utf8'));
  const sub = normalizeSubmission(raw);
  if (sub.honeypot) throw new Error('honeypot field is filled: this is a bot submission. Nothing drafted.');
  if (!sub.business) throw new Error('no shop name ("business") in the submission');

  // Token: must be one Ron issued and not used yet.
  if (opts.tokenCheck) {
    const t = readTokens(opts.tokens).tokens.find((x) => x.token === sub.token);
    if (!t) throw new Error(`token not issued on this Mac (${opts.tokens}). Treat as spam, or rerun with --no-token-check if Ron knows the shop.`);
    if (t.used) flag(`TOKEN ALREADY USED on ${t.used}: a second submission from the same link. Compare with the first.`);
    if (t.shop && slugify(t.shop) !== slugify(sub.business)) flag(`Token was issued for "${t.shop}" but the form says "${sub.business}".`);
  } else flag('Token NOT checked (--no-token-check).');

  let id = opts.id || slugify(sub.business);
  if (!SLUG_RE.test(id)) { flag(`Could not make a link name from "${sub.business}"; set the id by hand.`); id = id || 'shop'; }
  if (urlText(id) === 'slowgoapp.com') flag(`Link name "${id}" is long: the card prints just "slowgoapp.com" under the QR. A shorter id (8 characters or fewer) prints the full /f/ address.`);
  if (id.startsWith('t-')) flag(`Link name "${id}" starts with "t-", which the site uses for town links: pick another id.`);
  const date = new Date().toISOString().slice(0, 10);
  const dir = path.join(opts.out, `${id}-${date}`);
  mkdirSync(dir, { recursive: true });
  writeFileSync(path.join(dir, 'submission.json'), JSON.stringify(raw, null, 2) + '\n');

  // Required bits.
  if (!sub.terms) flag('Fleet terms box NOT ticked. Do not set up the shop until it is.');
  if (!sub.shopPhone) flag('No shop phone (optional on the form since 2026-10-17): the app shows no Call button unless the shop sends one.');
  else if (!phoneE164(sub.shopPhone)) flag(`Shop phone "${sub.shopPhone}" is not a 10-digit US/Canada number.`);
  if (!sub.town) flag('No service town in the submission (required on the form since 2026-10-17).');
  if (sub.kind === 'dealer' && sub.servicePhone && !phoneE164(sub.servicePhone)) flag(`Service number "${sub.servicePhone}" is not a 10-digit number.`);
  if (sub.brandColorRaw && !sub.brandColor) flag(`Brand colour "${sub.brandColorRaw}" is not #RRGGBB; ignored.`);
  if (sub.welcome.length > 120) flag('Welcome line is over 120 characters.');
  if (!sub.cardQty) flag('No card quantity.');
  if (!sub.shipAddress) flag('No shipping address.');

  // Where the shop is.
  const hasPin = Number.isFinite(sub.returnLat) && Number.isFinite(sub.returnLng);
  if (sub.kind === 'rental' && !hasPin) flag(`No map pin for the return spot. Address given: "${sub.returnAddress || '(none)'}". Place it by hand.`);
  const stateHint = (sub.returnAddress.match(/\b(FL|GA|AZ|SC|NY)\b/) || sub.shipAddress.match(/\b(FL|GA|AZ|SC|NY)\b/) || [])[1];
  const center = hasPin ? { lat: sub.returnLat, lng: sub.returnLng } : null;

  // Picks vs the places build (read-only).
  let places = [];
  if (!existsSync(opts.places)) flag(`Places build not found at ${opts.places}; picks not matched.`);
  else if (!center) flag('No pin, so picks were not matched (they need a centre to search around).');
  else places = placesNear(opts.places, center, opts.radiusKm);
  const picksMatched = sub.picks.map((pick) => ({ pick, ...(center && places.length ? matchPick(pick, places, center) : { status: 'unmatched', candidates: [] }) }));
  for (const m of picksMatched) {
    if (m.status === 'unmatched') flag(`Pick ${m.pick.n} "${m.pick.name}": UNMATCHED in the places build within ${opts.radiusKm} km. Find it by hand or drop it.`);
    else if (m.status === 'check') flag(`Pick ${m.pick.n} "${m.pick.name}": weak match "${m.best.name}" (score ${m.best.score}). Check it.`);
    else if (m.status === 'ambiguous') flag(`Pick ${m.pick.n} "${m.pick.name}": several places share the name (${m.candidates.length} candidates). Took the closest; check it.`);
  }
  const usable = picksMatched.filter((m) => m.best && m.status !== 'unmatched');
  if (usable.length > 5) flag(`${usable.length} usable picks but the app's profile holds 5 (FLEET_PICKS_MAX). Picks after the 5th are in extras.json for Ron to choose.`);
  if (sub.kind === 'rental' && usable.length < 3) flag(`Only ${usable.length} usable pick(s); a shipping rental profile needs 3-5.`);

  const area = center && places.length ? areaFrom(places, center, stateHint) : { name: '?', state: stateHint || '?' };
  if (area.name === '?') flag('Area name could not be worked out; set profile.area by hand.');
  const profile = buildProfile(sub, id, picksMatched, area);
  if (profile.shortName !== sub.business) flag(`shortName shortened to "${profile.shortName}" (12 characters for the car's row). Ron or the shop may prefer another.`);
  flag('rentalDays drafted as 7 (the automatic end date). Ask the shop for its usual rental length.');
  flag('Every routing check is "unchecked": run them (plan §4) and record "go" before shipping; a NoGo point is dropped.');

  // Logo.
  let logoNote;
  if (opts.logo) {
    const ext = path.extname(opts.logo).toLowerCase() || '.png';
    copyFileSync(opts.logo, path.join(dir, `logo-original${ext}`));
    logoNote = `copied to logo-original${ext}; make assets/fleet/${id}.png and ${id}-dark.png (sizes per utils/fleetProfile.test.mjs).`;
  } else if (sub.logo) {
    logoNote = `uploaded to Netlify (${sub.logo.filename || 'file'}${sub.logo.size ? `, ${Math.round(sub.logo.size / 1024)} KB` : ''}). Not downloaded: save it from the Netlify dashboard and rerun with --logo.`;
    flag('Logo is on Netlify only; save it and rerun with --logo <file>.');
  } else { logoNote = 'none uploaded; the app draws the initials until the shop emails one.'; flag('No logo: ask the shop to email it.'); }

  // App-format file + the app's own validator.
  const profileJs = `// DRAFT for ${sub.business}: tools/fleet-setup/draft-fleet.mjs, ${date}. WAITING FOR RON'S APPROVAL.\n// Goes in constants/fleet/shops/${id}.js on the fleet branch once every check is a recorded "go".\nexport default Object.freeze(${JSON.stringify(profile, null, 2)});\n`;
  writeFileSync(path.join(dir, 'profile.js'), profileJs);
  let checkText;
  try {
    const { text, from } = readAppFile(opts, PROFILE_JS);
    const tmp = path.join(os.tmpdir(), `fleetProfile-${process.pid}.mjs`);
    writeFileSync(tmp, text);
    const { validateFleetProfile } = await import(pathToFileURL(tmp).href);
    unlinkSync(tmp);
    const errs = validateFleetProfile(profile, { shipping: true });
    checkText = `validateFleetProfile (shipping: true), from ${from}\n${errs.length ? errs.map((e) => `- ${e}`).join('\n') : 'no problems'}\n` +
      `\nExpected until Ron finishes: "needs a recorded go check" for each point (routing checks not run yet).\n`;
  } catch (e) { checkText = `Could not run the app's validator: ${e.message}\n`; flag('App validator not run (see profile-check.txt).'); }
  writeFileSync(path.join(dir, 'profile-check.txt'), checkText);

  const extras = {
    note: 'Collected by the setup form; fleet profile schema 1 has no field for these yet.',
    hours: sub.hours || null, welcomeLine: sub.welcome || null, brandColor: sub.brandColor,
    servicePhone: phoneE164(sub.servicePhone)?.e164 || sub.servicePhone || null,
    returnAddress: sub.returnAddress || null,
    cards: { quantity: sub.cardQty, shipTo: sub.shipName || null, address: sub.shipAddress || null },
    contact: { name: sub.name || null, email: sub.email },
    serviceTown: sub.town || null, fleetBand: sub.fleetBand || null,
    picksBeyondFive: usable.slice(5).map((m) => ({ name: m.pick.name, note: m.pick.note, match: m.best })),
    termsAccepted: sub.terms, submittedAt: sub.created, netlifyId: sub.id,
  };
  writeFileSync(path.join(dir, 'extras.json'), JSON.stringify(extras, null, 2) + '\n');

  writeFileSync(path.join(dir, 'picks.json'), JSON.stringify(picksMatched, null, 2) + '\n');
  const csvq = (v) => `"${String(v ?? '').replace(/"/g, '""')}"`;
  writeFileSync(path.join(dir, 'picks.csv'), ['n,typed,note,status,matched_name,category,lat,lng,miles,score,pid',
    ...picksMatched.map((m) => [m.pick.n, m.pick.name, m.pick.note, m.status, m.best?.name, m.best?.cat, m.best?.lat, m.best?.lng, m.best?.mi, m.best?.score, m.best?.pid].map(csvq).join(','))].join('\n') + '\n');

  // Link, QR, card.
  const url = `https://slowgoapp.com/f/${id}`;
  writeFileSync(path.join(dir, 'link.txt'), `${url}\n\nTo turn the link on (Ron, in a batched website deploy): add this line to netlify/fleet-shops.mjs\n  '${id}',\nUntil then the link sends everyone to the home page, uncounted.\n`);
  const m = qrMatrix(opts.appRepo, url);
  const svg = qrSvg(m, url);
  writeFileSync(path.join(dir, `qr-${id}.svg`), svg);
  writeFileSync(path.join(dir, `qr-${id}.png`), qrPng(m));
  let card;
  try { card = renderCard(opts, sub, id, qrSvg(m, url, { quiet: 0, fg: '#1F3A2C', bg: '#F3EDE0' }), dir); }
  catch (e) { flag(`Card not rendered: ${e.message}`); }

  const readme = [
    `WAITING FOR RON'S APPROVAL: ${sub.business} (${sub.kind})`,
    `Drafted ${date} by tools/fleet-setup/draft-fleet.mjs from ${path.basename(file)}. Nothing was sent, published or deployed.`,
    '',
    `Link:      ${url}   (not live until the id is in netlify/fleet-shops.mjs)`,
    `Contact:   ${sub.name ? `${sub.name} ` : ''}<${sub.email}>`,
    `Town:      ${sub.town || '?'}${sub.fleetBand ? `   Fleet: ${sub.fleetBand} carts` : ''}`,
    `Phone:     ${profile.phoneLabel}${sub.servicePhone ? `   Service: ${sub.servicePhone}` : ''}`,
    `Return:    ${sub.kind === 'rental' ? (hasPin ? `${sub.returnLat}, ${sub.returnLng}` : 'NO PIN') + (sub.returnAddress ? `  (${sub.returnAddress})` : '') : 'dealer, none'}`,
    `Area:      ${area.name}, ${area.state}`,
    `Logo:      ${logoNote}`,
    `Cards:     ${sub.cardQty ?? '?'} to ${sub.shipName || '?'}, ${sub.shipAddress.replace(/\s*\n\s*/g, ', ') || '?'}`,
    `Terms:     ${sub.terms ? 'accepted' : 'NOT ACCEPTED'}`,
    '',
    'Picks:',
    ...picksMatched.map((x) => `  ${x.pick.n}. ${x.pick.name}${x.pick.note ? ` (${x.pick.note})` : ''} -> ${x.status.toUpperCase()}${x.best ? `: ${x.best.name} [${x.best.cat}] ${x.best.mi} mi, score ${x.best.score}` : ''}`),
    '',
    'Flagged:',
    ...flags.map((f) => `  - ${f}`),
    '',
    'Files: profile.js, profile-check.txt, extras.json, link.txt, picks.json/.csv, ' + `qr-${id}.png/.svg` + (card ? `, card-${id}.png/.pdf` : '') + ', submission.json',
    '',
    "Ron's checklist: [ ] routing checks run and recorded  [ ] logo assets made  [ ] proof emailed to the shop  [ ] shop said yes",
    '                 [ ] profile into the fleet branch (ships with a release)  [ ] id into fleet-shops.mjs (batched deploy)  [ ] cards printed',
  ].join('\n') + '\n';
  writeFileSync(path.join(dir, 'README.txt'), readme);
  return { dir, id, flags, picksMatched, profile };
}

function parseArgs(argv) {
  const o = { ...DEFAULTS, tokens: TOKENS_FILE, tokenCheck: true, radiusKm: 25, logo: null, file: null, id: null };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--logo') o.logo = argv[++i]; else if (a === '--out') o.out = argv[++i];
    else if (a === '--tokens') o.tokens = argv[++i]; else if (a === '--places') o.places = argv[++i];
    else if (a === '--app') o.app = argv[++i]; else if (a === '--radius-km') o.radiusKm = Number(argv[++i]);
    else if (a === '--id') o.id = argv[++i];
    else if (a === '--no-token-check') o.tokenCheck = false; else if (!o.file) o.file = a;
    else throw new Error(`unknown argument ${a}`);
  }
  if (!o.file) throw new Error('usage: draft-fleet.mjs <submission.json> [--logo file] [--out dir] [--tokens file] [--places sqlite] [--app worktree] [--no-token-check]');
  return o;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const o = parseArgs(process.argv.slice(2));
    const r = await draft(o.file, o);
    console.log(readFileSync(path.join(r.dir, 'README.txt'), 'utf8'));
    console.log(`Drafted into ${r.dir}`);
  } catch (e) { console.error(`draft-fleet: ${e.message}`); process.exit(1); }
}
