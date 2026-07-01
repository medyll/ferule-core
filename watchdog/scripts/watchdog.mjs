#!/usr/bin/env node
/**
 * watchdog.mjs — Independent health monitor for application-core
 *
 * Runs every 5 minutes via Windows Task Scheduler.
 * Checks critical subsystems and alerts on failure.
 * Zero external dependencies — pure Node.js.
 */

import { readFileSync, writeFileSync, existsSync, statSync, appendFileSync, readdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

const __dirname = dirname(fileURLToPath(import.meta.url));
const APP_ROOT = join(__dirname, '..');
const APPS_ROOT = join(APP_ROOT, '..');
const WORKSPACE = join(APPS_ROOT, '..');

const LOG_PATH = join(APP_ROOT, 'logs', 'alerts.jsonl');
const MAX_LOG_LINES = 1000;

const PLACE_DE_GREVE_PATH = join(WORKSPACE, 'place-de-greve.md');
const CONTEXT_REGISTRY_PATH = join(APPS_ROOT, 'place-de-greve', 'context-registry.json');
const SCAN_LOG_PATH = join(WORKSPACE, 'logs', 'place-de-greve-scan.jsonl');
const LOCK_PATH = join(WORKSPACE, 'place-de-greve.lock');
const WATCHER_SCRIPT = join(WORKSPACE, 'scripts', 'dashboard-watcher.mjs');
const OCM_INSTRUCTIONS = join(APPS_ROOT, 'core-squad', 'ocm-INSTRUCTIONS.md');

const LOCK_STALE_THRESHOLD_MS = 60 * 1000; // 60 seconds
const SCAN_STALE_THRESHOLD_MS = 60 * 60 * 1000; // 1 hour

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// CHECKS
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

function checkWatcherProcess() {
  try {
    const output = execSync('wmic process where "name=\'node.exe\'" get CommandLine', { encoding: 'utf-8' });
    const hasWatcher = output.includes('dashboard-watcher.mjs');
    return {
      name: 'watcher-process',
      status: hasWatcher ? 'pass' : 'fail',
      expected: 'dashboard-watcher.mjs running',
      actual: hasWatcher ? 'found' : 'not found',
      severity: 'critical'
    };
  } catch (e) {
    return {
      name: 'watcher-process',
      status: 'fail',
      expected: 'dashboard-watcher.mjs running',
      actual: `wmic query failed: ${e.message}`,
      severity: 'critical'
    };
  }
}

function checkScanLogRecent() {
  try {
    if (!existsSync(SCAN_LOG_PATH)) {
      return { name: 'scan-log-recent', status: 'fail', expected: `scan log at ${SCAN_LOG_PATH}`, actual: 'file does not exist', severity: 'warning' };
    }
    const stat = statSync(SCAN_LOG_PATH);
    const age = Date.now() - stat.mtimeMs;
    if (age > SCAN_STALE_THRESHOLD_MS) {
      return { name: 'scan-log-recent', status: 'fail', expected: `scan log < ${SCAN_STALE_THRESHOLD_MS / 1000 / 60}min old`, actual: `${Math.round(age / 1000 / 60)}min old`, severity: 'warning' };
    }
    return { name: 'scan-log-recent', status: 'pass', expected: 'recent scan log', actual: `${Math.round(age / 1000 / 60)}min old` };
  } catch (e) {
    return { name: 'scan-log-recent', status: 'fail', expected: 'readable scan log', actual: e.message, severity: 'warning' };
  }
}

function checkContextRegistry() {
  try {
    if (!existsSync(CONTEXT_REGISTRY_PATH)) {
      return { name: 'context-registry', status: 'fail', expected: `context-registry.json at ${CONTEXT_REGISTRY_PATH}`, actual: 'file missing', severity: 'critical' };
    }
    const raw = readFileSync(CONTEXT_REGISTRY_PATH, 'utf-8');
    JSON.parse(raw);
    return { name: 'context-registry', status: 'pass', expected: 'valid JSON registry', actual: 'valid' };
  } catch (e) {
    return { name: 'context-registry', status: 'fail', expected: 'valid JSON registry', actual: e.message, severity: 'critical' };
  }
}

function checkPlaceDeGreveAccessible() {
  try {
    if (!existsSync(PLACE_DE_GREVE_PATH)) {
      return { name: 'place-de-greve-accessible', status: 'fail', expected: `place-de-greve.md at ${PLACE_DE_GREVE_PATH}`, actual: 'file missing', severity: 'critical' };
    }
    statSync(PLACE_DE_GREVE_PATH);
    return { name: 'place-de-greve-accessible', status: 'pass', expected: 'accessible mission queue', actual: 'accessible' };
  } catch (e) {
    return { name: 'place-de-greve-accessible', status: 'fail', expected: 'accessible mission queue', actual: e.message, severity: 'critical' };
  }
}

function checkLockFileStale() {
  try {
    if (!existsSync(LOCK_PATH)) {
      return { name: 'lock-file-stale', status: 'pass', expected: 'no stale lock', actual: 'no lock file' };
    }
    const raw = readFileSync(LOCK_PATH, 'utf-8');
    let lock;
    try { lock = JSON.parse(raw); } catch { return { name: 'lock-file-stale', status: 'pass', expected: 'no stale lock', actual: 'invalid lock — ignored' }; }
    if (!lock.acquiredAt) return { name: 'lock-file-stale', status: 'pass', expected: 'no stale lock', actual: 'no acquiredAt — ignored' };
    const age = Date.now() - new Date(lock.acquiredAt).getTime();
    if (age > LOCK_STALE_THRESHOLD_MS) {
      return { name: 'lock-file-stale', status: 'fail', expected: `lock < ${LOCK_STALE_THRESHOLD_MS / 1000}s old`, actual: `${Math.round(age / 1000)}s old — STALE`, severity: 'warning' };
    }
    return { name: 'lock-file-stale', status: 'pass', expected: 'fresh lock', actual: `${Math.round(age / 1000)}s old` };
  } catch (e) {
    return { name: 'lock-file-stale', status: 'fail', expected: 'readable lock file', actual: e.message, severity: 'warning' };
  }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ALERTING
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

function logAlert(result) {
  const entry = JSON.stringify({ timestamp: new Date().toISOString(), ...result }) + '\n';
  if (!existsSync(dirname(LOG_PATH))) {
    // logs dir should exist but we'll handle gracefully
  }
  appendFileSync(LOG_PATH, entry, 'utf-8');

  // Rotate: keep last MAX_LOG_LINES
  try {
    const lines = readFileSync(LOG_PATH, 'utf-8').split('\n').filter(l => l.trim());
    if (lines.length > MAX_LOG_LINES) {
      writeFileSync(LOG_PATH, lines.slice(-MAX_LOG_LINES).join('\n') + '\n', 'utf-8');
    }
  } catch { /* rotation is best-effort */ }
}

function notifyCoreSquad(failures) {
  try {
    if (!existsSync(OCM_INSTRUCTIONS)) return;
    let content = readFileSync(OCM_INSTRUCTIONS, 'utf-8');
    const marker = '## Watchdog Alerts';
    const now = new Date().toISOString().slice(0, 19).replace('T', ' ');
    const alertBlock = failures.map(f => `- **[${f.severity.toUpperCase()}]** ${f.name}: ${f.actual} (expected: ${f.expected})`).join('\n');
    const section = `\n### ${marker}\n\n> ${now} — ${failures.length} check(s) failed\n\n${alertBlock}\n`;

    if (content.includes(marker)) {
      // Replace existing section
      const startIdx = content.indexOf(`### ${marker}`);
      const nextSection = content.indexOf('\n### ', startIdx + 1);
      if (nextSection !== -1) {
        content = content.slice(0, startIdx) + section + content.slice(nextSection);
      } else {
        content = content.slice(0, startIdx) + section;
      }
    } else {
      content += '\n' + section;
    }
    writeFileSync(OCM_INSTRUCTIONS, content, 'utf-8');
  } catch { /* best-effort notification */ }
}

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// MAIN
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

function main() {
  const checks = [
    checkWatcherProcess(),
    checkScanLogRecent(),
    checkContextRegistry(),
    checkPlaceDeGreveAccessible(),
    checkLockFileStale(),
  ];

  const failures = checks.filter(c => c.status === 'fail');
  const passes = checks.filter(c => c.status === 'pass');

  // Log all results
  for (const c of checks) {
    logAlert(c);
  }

  // Notify on failures
  if (failures.length > 0) {
    notifyCoreSquad(failures);
    console.error(`WATCHDOG: ${failures.length} check(s) FAILED — see logs/alerts.jsonl`);
    for (const f of failures) {
      console.error(`  [${f.severity.toUpperCase()}] ${f.name}: ${f.actual}`);
    }
    process.exit(1);
  } else {
    console.log(`WATCHDOG: All ${checks.length} checks passed`);
    process.exit(0);
  }
}

main();
