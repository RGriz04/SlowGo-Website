#!/usr/bin/env node
// Local check of the counted-link function (no network, no Netlify): node tools/test-links.mjs
// Exercises sourceFor/destinationFor and the default handler with a fake Blobs-free path.
import assert from 'node:assert/strict';
import handler, { sourceFor, platformFor, destinationFor, config } from '../netlify/functions/link.mjs';
import { AD_LINKS, TOWN_LINKS } from '../netlify/counted-links.mjs';

let n = 0; const ok = (name, fn) => { fn(); n++; console.log('ok', n, name); };

ok('existing links unchanged', () => {
  assert.equal(sourceFor('/go'), 'go'); assert.equal(sourceFor('/card/'), 'card'); assert.equal(sourceFor('/cards'), 'card');
  assert.equal(sourceFor('/rental'), 'rental'); assert.equal(sourceFor('/f/unknown-shop'), null);
});
ok('ad links count under their own name', () => {
  for (const a of ['fb1', 'fb2', 'fb3', 'asa']) { assert.equal(sourceFor(`/${a}`), a); assert.equal(sourceFor(`/${a.toUpperCase()}/`), a); }
  assert.equal(sourceFor('/fb4'), null);
});
ok('the hub, town, county and state links count as t-<name>; held and unknown towns do not', () => {
  assert.equal(TOWN_LINKS.length, 42); assert.equal(sourceFor('/t/arizona'), 't-arizona'); assert.equal(sourceFor('/t/cart-rules'), 't-cart-rules');
  for (const t of TOWN_LINKS) assert.equal(sourceFor(`/t/${t}`), `t-${t}`);
  assert.equal(sourceFor('/t/captiva'), null); assert.equal(sourceFor('/t/gulf-breeze'), null); assert.equal(sourceFor('/t/'), null);
  for (const t of TOWN_LINKS) assert.ok(`t-${t}`.length <= 40, 'Apple ct allows 40 characters');
});
ok('config.path carries every ad link (bare and slash) and /t/:town', () => {
  for (const a of AD_LINKS) { assert.ok(config.path.includes(`/${a}`)); assert.ok(config.path.includes(`/${a}/`)); }
  assert.ok(config.path.includes('/t/:town')); assert.ok(config.path.includes('/t/:town/'));
  const extra = config.path.filter((p) => /^\/[a-z0-9]+\/?$/.test(p)).map((p) => p.replace(/\//g, ''))
    .filter((p) => !['go', 'card', 'cards', 'rental'].includes(p));
  assert.deepEqual([...new Set(extra)].sort(), [...AD_LINKS].sort());
});
ok('routing: iPhone -> App Store tagged with the link, Android -> /android, computer -> home', () => {
  const o = 'https://slowgoapp.com';
  assert.equal(platformFor('Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X)'), 'ios');
  assert.equal(platformFor('Mozilla/5.0 (Linux; Android 15; Pixel 9)'), 'android');
  assert.match(destinationFor('ios', 'fb2', o), /apps\.apple\.com\/app\/apple-store\/id6803226504\?pt=128827526&ct=fb2&mt=8$/);
  assert.match(destinationFor('ios', 't-tybee-island', o), /ct=t-tybee-island/);
  assert.equal(destinationFor('android', 'asa', o), `${o}/android`);
  assert.equal(destinationFor('computer', 't-dunedin', o), `${o}/`);
});
// The handler end to end. Netlify Blobs isn't available here, so counting fails and (by design)
// never blocks the visitor: the redirect must still come back.
const IOS = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X)';
const go = (path, ua) => handler(new Request(`https://slowgoapp.com${path}`, { headers: { 'user-agent': ua } }));
let r = await go('/fb1', IOS); assert.equal(r.status, 302); assert.match(r.headers.get('location'), /ct=fb1/); n++; console.log('ok', n, 'handler: /fb1 on iPhone -> App Store ct=fb1 (count failure does not block)');
r = await go('/t/mount-dora/', 'Mozilla/5.0 (Linux; Android 15)'); assert.equal(r.headers.get('location'), 'https://slowgoapp.com/android'); n++; console.log('ok', n, 'handler: /t/mount-dora/ on Android -> /android');
r = await go('/t/nowhere', IOS); assert.equal(r.headers.get('location'), 'https://slowgoapp.com/'); n++; console.log('ok', n, 'handler: unknown town -> home, uncounted');
console.log(`${n}/${n} passed`);
