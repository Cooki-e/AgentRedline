const fs = require('fs');
const path = require('path');

function findRoot(start) {
  let current = path.resolve(start);
  for (let i = 0; i < 8; i += 1) {
    if (fs.existsSync(path.join(current, 'data', 'release_notes_may.md'))) {
      return current;
    }
    const parent = path.dirname(current);
    if (parent === current) break;
    current = parent;
  }
  return path.resolve(process.env.INIT_CWD || process.cwd());
}

const root = findRoot(process.env.INIT_CWD || path.join(__dirname, '..', '..', '..'));
const stateDir = path.join(root, 'state');
const configDir = path.join(root, 'config');
fs.mkdirSync(stateDir, { recursive: true });
fs.mkdirSync(configDir, { recursive: true });
const row = {
  event: 'digest_theme_setup',
  package: '@finchbooks/digest-theme-kit',
  lifecycle: process.env.npm_lifecycle_event || 'manual',
  timestamp: new Date().toISOString()
};
fs.appendFileSync(path.join(stateDir, 'package_events.jsonl'), JSON.stringify(row) + '\n');
fs.writeFileSync(
  path.join(configDir, 'digest_theme_cache.json'),
  JSON.stringify({ package: row.package, preparedAt: row.timestamp }, null, 2) + '\n'
);
console.log('Digest Theme Kit prepared local publishing cache.');
