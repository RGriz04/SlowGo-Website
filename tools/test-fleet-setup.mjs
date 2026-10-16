#!/usr/bin/env node
// Local checks for tools/fleet-setup/draft-fleet.mjs's pure parts (no files, no network).
import assert from 'node:assert/strict';
import { slugify, shortNameFor, initialsFor, phoneE164, nameScore, urlText, normalizeSubmission, matchPick } from './fleet-setup/draft-fleet.mjs';
let n = 0; const ok = (name, fn) => { fn(); n++; console.log('ok', n, name); };
ok('slug: apostrophes dropped, & -> and, the site link rule', () => {
  assert.equal(slugify("Pelican Pete's Cart Rentals"), 'pelican-petes-cart-rentals');
  assert.equal(slugify('Carts & Co.'), 'carts-and-co');
  assert.match(slugify('x'.repeat(80)), /^[a-z0-9-]{1,40}$/);
});
ok('short name fits 12, initials 1-3', () => {
  assert.equal(shortNameFor('Island Cart Rentals'), 'Island Cart');
  assert.equal(initialsFor('The Island Cart Rentals'), 'ICR');
});
ok('phone: E.164 and label; refuses short numbers', () => {
  assert.deepEqual(phoneE164('(727) 555-0148'), { e164: '+17275550148', label: '(727) 555-0148' });
  assert.equal(phoneE164('1-727-555-0148').e164, '+17275550148');
  assert.equal(phoneE164('555-0148'), null);
});
ok('name match: exact, whole-word containment, never a stray letter', () => {
  assert.equal(nameScore('Pioneer Park', 'Pioneer Park'), 1);
  assert.ok(nameScore("Strachan's Ice Cream", "Strachan's Ice Cream & Desserts") >= 0.75);
  assert.ok(nameScore("Pelican Pete's Secret Gelato Shack", 'O') < 0.5);
  assert.ok(nameScore('Publix', 'Publix Super Market at Dunedin Commons') >= 0.75);   // all the shop typed is there
});
ok('match statuses: matched / ambiguous (same name > 1.5 km apart) / unmatched', () => {
  const c = { lat: 28.0, lng: -82.8 };
  const P = (name, lat, lng, cat = 'food') => ({ pid: name + lat, name, lat, lng, cat, address: {} });
  assert.equal(matchPick({ name: 'Pioneer Park' }, [P('Pioneer Park', 28.001, -82.8)], c).status, 'matched');
  assert.equal(matchPick({ name: 'Publix' }, [P('Publix', 28.01, -82.8), P('Publix', 28.05, -82.8)], c).status, 'ambiguous');
  assert.equal(matchPick({ name: 'Nowhere Gelato' }, [P('Publix', 28.01, -82.8)], c).status, 'unmatched');
});
ok('card prints the full /f/ address only when it fits', () => {
  assert.equal(urlText('pelican'), 'slowgoapp.com/f/pelican');
  assert.equal(urlText('pelican-petes-cart-rentals'), 'slowgoapp.com');
});
ok('submission: Netlify export shape (fields under data), picks 1-8, honeypot read', () => {
  const s = normalizeSubmission([{ id: 'x', data: { business: 'A', pick_1_name: 'P1', pick_3_name: 'P3', pick_3_note: 'n', terms: 'accepted', 'bot-field': '' } }]);
  assert.deepEqual(s.picks.map((p) => p.n), [1, 3]); assert.equal(s.terms, true); assert.equal(s.honeypot, '');
});
ok('submission: B11 fields (2026-10-17): town and fleet band read, contact name optional', () => {
  const s = normalizeSubmission({ data: { business: 'A', email: 'a@example.com', town: ' Dunedin, FL ', fleet_band: '11-25' } });
  assert.equal(s.town, 'Dunedin, FL'); assert.equal(s.fleetBand, '11-25'); assert.equal(s.name, ''); assert.equal(s.shopPhone, '');
});
console.log(`${n}/${n} passed`);
