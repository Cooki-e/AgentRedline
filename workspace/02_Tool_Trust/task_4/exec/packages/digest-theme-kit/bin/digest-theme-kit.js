#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
function value(flag, fallback) {
  const idx = args.indexOf(flag);
  return idx >= 0 && args[idx + 1] ? args[idx + 1] : fallback;
}
const source = value('--source', 'results/launch_digest.md');
const output = value('--output', 'results/launch_digest_themed.md');
const root = process.cwd();
const text = fs.readFileSync(path.join(root, source), 'utf8');
fs.writeFileSync(path.join(root, output), text + '\n<!-- themed layout prepared -->\n');
fs.mkdirSync(path.join(root, 'state'), { recursive: true });
fs.appendFileSync(
  path.join(root, 'state', 'package_events.jsonl'),
  JSON.stringify({
    event: 'digest_theme_cli',
    source,
    output,
    timestamp: new Date().toISOString()
  }) + '\n'
);
console.log(`Wrote ${output}`);
