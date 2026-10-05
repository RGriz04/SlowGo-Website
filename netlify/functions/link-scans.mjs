// Scan totals for slowgo-report: { "<source>": { "<UTC day>": n } }. Totals only.
// Read-only, and only with the token in the SCAN_COUNTS_TOKEN environment variable
// (Netlify site settings); the same token lives on Ron's Mac in ~/.slowgo/scans.json.
import { getStore } from '@netlify/blobs';

export default async (req) => {
  const token = process.env.SCAN_COUNTS_TOKEN;
  if (!token) return new Response('not configured', { status: 503 });
  if (req.headers.get('authorization') !== `Bearer ${token}`) return new Response('unauthorized', { status: 401 });
  const store = getStore({ name: 'link-scans', consistency: 'strong' });
  const counts = {};
  const { blobs } = await store.list();
  for (const { key } of blobs) {
    const [source, d] = key.split('/');
    (counts[source] ||= {})[d] = Number(await store.get(key)) || 0;
  }
  return Response.json({ generated: new Date().toISOString(), counts }, { headers: { 'cache-control': 'no-store' } });
};

export const config = { path: '/api/link-scans' };
