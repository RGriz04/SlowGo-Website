#!/usr/bin/env node
// Puts the favicon set's <link> block in the <head> of every HTML page under SlowGo-Launch/
// (or only the files/folders named on the command line). Idempotent: a page that already has
// the block is left alone. It also removes the old inline data-URI "S" icon, which Google
// cannot crawl (Google Search wants a crawlable favicon whose size is a multiple of 48 px).
//   node tools/add-favicon-links.mjs                       # every page
//   node tools/add-favicon-links.mjs SlowGo-Launch/golf-carts   # just one folder
import { readFileSync, writeFileSync, readdirSync, statSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', 'SlowGo-Launch');
export const MARK = '<!-- favicon set (2026-10-17) -->';
export const BLOCK = [
  MARK,
  '<link rel="icon" href="/favicon.ico" sizes="48x48" />',
  '<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png" />',
  '<link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png" />',
  '<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />',
  '<link rel="manifest" href="/site.webmanifest" />',
].join('\n');
const OLD_ICON = /<link rel="icon" type="image\/svg\+xml" href="data:image\/svg\+xml;[^"]*" \/>\n?/;

export function addBlock(html) {
  if (html.includes(MARK)) return html;
  if (OLD_ICON.test(html)) return html.replace(OLD_ICON, BLOCK + '\n');
  if (!/<\/head>/i.test(html)) return html;
  return html.replace(/<\/head>/i, BLOCK + '\n</head>');
}

function walk(p, out) {
  if (statSync(p).isDirectory()) { for (const f of readdirSync(p)) walk(path.join(p, f), out); }
  else if (p.endsWith('.html')) out.push(p);
  return out;
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const targets = process.argv.slice(2);
  const files = (targets.length ? targets : [ROOT]).flatMap((t) => walk(path.resolve(t), []));
  let changed = 0;
  for (const f of files) {
    const before = readFileSync(f, 'utf8'); const after = addBlock(before);
    if (after !== before) { writeFileSync(f, after); changed++; console.log('added:', path.relative(process.cwd(), f)); }
  }
  console.log(`${changed} of ${files.length} pages changed`);
}
