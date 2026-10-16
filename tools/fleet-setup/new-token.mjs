#!/usr/bin/env node
// Issue a private setup link for one shop, after it said yes (fleet step 2). Local only: nothing is
// sent anywhere. Ron pastes the printed link into his own email to the shop.
//   node tools/fleet-setup/new-token.mjs "Island Cart Rentals"
// Tokens live on this Mac only, in ~/.slowgo/fleet-setup-tokens.json (chmod 600), never in a repo.
// draft-fleet.mjs refuses a submission whose token isn't in that file (or was already used).
import { randomBytes } from 'node:crypto';
import { readFileSync, writeFileSync, mkdirSync, existsSync, chmodSync } from 'node:fs';
import path from 'node:path';
import os from 'node:os';

export const TOKENS_FILE = process.env.SLOWGO_FLEET_TOKENS || path.join(os.homedir(), '.slowgo', 'fleet-setup-tokens.json');

export function readTokens(file = TOKENS_FILE) {
  if (!existsSync(file)) return { tokens: [] };
  return JSON.parse(readFileSync(file, 'utf8'));
}

export function issueToken(shop, file = TOKENS_FILE) {
  const db = readTokens(file);
  const token = randomBytes(18).toString('base64url');   // 24 characters, matches the page's /^[A-Za-z0-9_-]{20,64}$/
  db.tokens.push({ token, shop, issued: new Date().toISOString().slice(0, 10), used: null });
  mkdirSync(path.dirname(file), { recursive: true });
  writeFileSync(file, JSON.stringify(db, null, 2) + '\n');
  chmodSync(file, 0o600);
  return token;
}

if (process.argv[1] && path.resolve(process.argv[1]) === path.resolve(new URL(import.meta.url).pathname)) {
  const shop = process.argv.slice(2).join(' ').trim();
  if (!shop) { console.error('usage: new-token.mjs "<shop name>"'); process.exit(2); }
  const t = issueToken(shop);
  console.log(`Setup link for ${shop} (send it from your own email):\nhttps://slowgoapp.com/business/setup?t=${t}`);
}
