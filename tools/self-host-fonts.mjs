#!/usr/bin/env node
// Swap the Google Fonts head block for the self-hosted fonts (B9, 2026-10-17).
//
//   node tools/self-host-fonts.mjs <page.html ...>   rewrite those pages
//   node tools/self-host-fonts.mjs --all             rewrite every .html under SlowGo-Launch/
//   node tools/self-host-fonts.mjs --check           list pages under SlowGo-Launch/ that still load
//                                                    fonts.googleapis.com / fonts.gstatic.com (exit 1 if any)
//
// Why a script: the town pages (golf-carts/, generated from safety.html's head) and terms/privacy live on
// other branches. After those branches merge, run `--all` once (or regenerate the town pages from the new
// safety.html head) and then `--check` must print 0 before the deploy.
import { readFileSync, writeFileSync, readdirSync, statSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..', 'SlowGo-Launch');
const GOOGLE = /fonts\.(googleapis|gstatic)\.com/;
// The three lines every page carried (preconnect x2 + the css2 stylesheet), any indentation.
const BLOCK = /^([ \t]*)<link rel="preconnect" href="https:\/\/fonts\.googleapis\.com" \/>\r?\n[ \t]*<link rel="preconnect" href="https:\/\/fonts\.gstatic\.com" crossorigin \/>\r?\n[ \t]*<link href="https:\/\/fonts\.googleapis\.com\/css2\?[^"]*" rel="stylesheet" \/>$/m;
const LOCAL = (i) => [
  `${i}<link rel="preload" href="/fonts/Fraunces-Roman.latin.var.woff2" as="font" type="font/woff2" crossorigin />`,
  `${i}<link rel="preload" href="/fonts/Inter.latin.var.woff2" as="font" type="font/woff2" crossorigin />`,
  `${i}<link rel="stylesheet" href="/fonts/fonts.css" />`,
].join('\n');

function allPages(dir = ROOT) {
  const out = [];
  for (const name of readdirSync(dir)) {
    if (name.startsWith('.') || name === 'node_modules') continue;
    const p = join(dir, name);
    if (statSync(p).isDirectory()) out.push(...allPages(p));
    else if (name.endsWith('.html')) out.push(p);
  }
  return out.sort();
}

const args = process.argv.slice(2);
if (args[0] === '--check') {
  const bad = allPages().filter((p) => GOOGLE.test(readFileSync(p, 'utf8')));
  for (const p of bad) console.log('still on Google Fonts:', p.slice(ROOT.length + 1));
  console.log(`${bad.length} page(s) still load Google Fonts`);
  process.exit(bad.length ? 1 : 0);
}
const pages = args[0] === '--all' ? allPages() : args;
if (!pages.length) { console.error('usage: self-host-fonts.mjs <page.html ...> | --all | --check'); process.exit(2); }
let changed = 0, failed = 0;
for (const p of pages) {
  const html = readFileSync(p, 'utf8');
  if (!GOOGLE.test(html)) continue;
  const next = html.replace(BLOCK, (_, indent) => LOCAL(indent));
  if (GOOGLE.test(next)) { console.error('unrecognised Google Fonts markup, left alone:', p); failed++; continue; }
  writeFileSync(p, next);
  changed++;
}
console.log(`${changed} page(s) switched to /fonts/fonts.css${failed ? `, ${failed} left alone` : ''}`);
process.exit(failed ? 1 : 0);
