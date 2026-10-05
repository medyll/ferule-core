#!/usr/bin/env node
/**
 * check-structure.mjs — Structure validator for core-ferule/
 *
 * Verifies that each project under core-ferule/<app>/development/<version>-<project>/
 * conforms to the standard defined in core-ferule/README.md.
 *
 * Usage: node check-structure.mjs [path-to-applications]
 * Default path: C:\Users\Mydde\.openclaw\workspace\core-ferule
 *
 * Zero external dependencies — pure Node.js.
 */

import { readdirSync, existsSync, readFileSync, writeFileSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';

const APPS_ROOT = process.argv[2] || join(process.cwd(), 'core-ferule');

// ─── Severity levels ────────────────────────────────────────────────────────
const WARN = '⚠️';
const ERROR = '❌';
const OK = '✅';
const UNKNOWN = '🔍';

// ─── Known structure — elements covered by the standard ─────────────────────
const KNOWN_FILES = new Set(['llms.txt', 'README.md', 'USER-NOTES.md', 'PROMPT-TEMPLATES.md', 'SKILL.md', 'BLUEPRINT.md', 'SCRATCHPAD.md', 'DEPENDENCIES.md', 'context-registry.json', 'domain-registry.json', 'index.mjs', 'package.json', 'CLAW.md', 'requirements.txt', 'run_engine.py']);
const KNOWN_DIRS = new Set(['reports', 'archives', 'logs', 'scripts', 'contexts', 'skill', 'templates', 'rules', 'sources', 'source', 'assets', 'nexus-protocol', 'config', 'artifacts', 'references', '.openclaw', 'bmad', 'core', 'interfaces', 'embeddings']);
const KNOWN_FILE_PATTERNS = [
  /^phase-\d+-.+\.md$/,        // phase files
  /^phase-\d+-technical-debt/,  // debt files
  /^skill\/[^/]+\/SKILL\.md$/, // skill SKILL.md files
  /^config\/[^/]+\.yaml$/,     // workspace config files (§16)
];

// ─── Transient extensions — skip these entirely ─────────────────────────────
const TRANSIENT_EXTENSIONS = new Set(['.log', '.tmp', '.bak', '.swp', '.cache', '.DS_Store', '.md']);

function isTransient(entry) {
  const ext = entry.slice(entry.lastIndexOf('.'));
  if (TRANSIENT_EXTENSIONS.has(ext)) return true;
  // Skip known doc types that aren't structural elements
  if (entry.startsWith('HEARTBEAT.') || entry.startsWith('phase-') || entry.startsWith('llms.')) return true;
  if (entry.startsWith('ocm-')) return true;  // OCM coordination files live next to core-squad/
  return false;
}

// ─── Accumulator ────────────────────────────────────────────────────────────
const violations = [];
const unknowns = [];
let projectCount = 0;
let passCount = 0;

const FORMALIZE = process.argv.includes('--formalize');

// ─── Helpers ────────────────────────────────────────────────────────────────
function report(severity, project, message) {
  violations.push({ severity, project, message });
}

function reportUnknown(project, element, projPath) {
  unknowns.push({ project, element, projPath });
}

function isKnown(entry) {
  if (KNOWN_FILES.has(entry) || KNOWN_DIRS.has(entry)) return true;
  for (const pattern of KNOWN_FILE_PATTERNS) {
    if (pattern.test(entry)) return true;
  }
  return false;
}

function scanUnknownElements(projPath, projDir) {
  const entries = readdirSync(projPath);
  for (const entry of entries) {
    if (isTransient(entry)) continue;
    if (!isKnown(entry)) {
      reportUnknown(projDir, entry, projPath);
    }
  }
}

function fileExists(projectPath, file) {
  return existsSync(join(projectPath, file));
}

function extractIds(filePath, pattern) {
  if (!existsSync(filePath)) return [];
  const content = readFileSync(filePath, 'utf-8');
  // Only match IDs at the start of lines (section headers like ### BUG-001 or ### TD-01)
  // This avoids counting IDs that appear in summary tables or body text
  const lines = content.split('\n');
  const headerPattern = /^#{1,3}\s+/;
  const results = [];
  for (const line of lines) {
    if (headerPattern.test(line.trim())) {
      const match = line.match(pattern);
      if (match) {
        // Only take the first match per header line — avoids picking up
        // narrative references like "### TD-03 — TD-10 Risk Monitoring Closure"
        const m = match[0];
        const num = parseInt(m.replace(/\D/g, ''), 10);
        results.push({ raw: m, num });
      }
    }
  }
  return results;
}

function validateSequentialIds(ids, idType, projectPath) {
  if (ids.length === 0) return;
  const nums = ids.map(i => i.num).sort((a, b) => a - b);
  const expected = Array.from({ length: nums[nums.length - 1] }, (_, i) => i + 1);
  const missing = expected.filter(n => !nums.includes(n));
  const duplicates = nums.filter((n, i, arr) => arr.indexOf(n) !== i);

  if (missing.length > 0) {
    report(WARN, projectPath, `${idType}: Missing IDs: ${missing.map(n => `${idType.split('-')[0]}-${String(n).padStart(2, '0')}`).join(', ')}`);
  }
  if (duplicates.length > 0) {
    report(ERROR, projectPath, `${idType}: Duplicate IDs: ${duplicates.map(n => `${idType.split('-')[0]}-${String(n).padStart(2, '0')}`).join(', ')}`);
  }
}

function checkHeaderDepth(filePath, projectPath) {
  if (!existsSync(filePath)) return;
  const content = readFileSync(filePath, 'utf-8');
  const lines = content.split('\n');
  lines.forEach((line, idx) => {
    if (/^#{4,}/.test(line)) {
      report(ERROR, projectPath, `Header depth > ### at line ${idx + 1}: "${line.trim()}"`);
    }
  });
}

function checkFencedCodeBlocks(filePath, projectPath) {
  if (!existsSync(filePath)) return;
  const content = readFileSync(filePath, 'utf-8');
  const lines = content.split('\n');
  let inFence = false;
  let unfenced = false;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (/^```/.test(line)) {
      if (!inFence && !/```[a-zA-Z]/.test(line) && line.trim() !== '```') {
        // Opening fence without language tag
        report(WARN, projectPath, `Unfenced or untagged code block at line ${i + 1} in ${relative(APPS_ROOT, filePath)}`);
      }
      inFence = !inFence;
    }
  }
}

// ─── Main ───────────────────────────────────────────────────────────────────
function scanApplications() {
  if (!existsSync(APPS_ROOT)) {
    console.log(`${ERROR} Applications root not found: ${APPS_ROOT}`);
    process.exit(1);
  }

  const appDirs = readdirSync(APPS_ROOT).filter(d => {
    const fullPath = join(APPS_ROOT, d);
    return statSync(fullPath).isDirectory() && d !== 'node_modules' && d !== '.git';
  });

  for (const appDir of appDirs) {
    const appPath = join(APPS_ROOT, appDir);
    const devPath = join(appPath, 'development');

    // ─── Always scan app root for unknown elements ──────────────────────────
    const appRootEntries = readdirSync(appPath);
    for (const entry of appRootEntries) {
      if (isTransient(entry)) continue;
      // Known app-root elements
      const appRootKnown = new Set(['development', 'contexts', 'USER-NOTES.md', 'README.md', 'BLUEPRINT.md', 'SCRATCHPAD.md', 'DEPENDENCIES.md', 'context-registry.json', 'domain-registry.json', 'skill', '.gitkeep', 'templates', 'index.mjs', 'package.json', 'CLAW.md', 'HEARTBEAT.md']);
      if (!appRootKnown.has(entry) && !KNOWN_DIRS.has(entry) && !KNOWN_FILES.has(entry)) {
        reportUnknown(appDir, entry, appPath);
      }
    }

    // ─── Skill check (§15) ──────────────────────────────────────────────────
    if (appDir === 'templates') continue; // templates is a utility folder, not an app
    if (!existsSync(join(appPath, 'skill', appDir, 'SKILL.md'))) {
      report(WARN, appDir, `Missing skill/${appDir}/SKILL.md (§15 — required for every application)`);
    }

    if (!existsSync(devPath)) continue;

    const projectDirs = readdirSync(devPath).filter(d => {
      const fullPath = join(devPath, d);
      return statSync(fullPath).isDirectory() && /^v\d+-/.test(d);
    });

    for (const projDir of projectDirs) {
      const projPath = join(devPath, projDir);
      projectCount++;
      let projectViolations = 0;

      // Required files
      const requiredFiles = ['llms.txt', 'README.md'];
      for (const file of requiredFiles) {
        if (!fileExists(projPath, file)) {
          report(ERROR, projDir, `Missing required file: ${file}`);
          projectViolations++;
        }
      }
      // USER-NOTES.md can be at project root or app root
      if (!fileExists(projPath, 'USER-NOTES.md') && !fileExists(appPath, 'USER-NOTES.md')) {
        report(ERROR, projDir, `Missing USER-NOTES.md (expected at project root or app root)`);
        projectViolations++;
      }

      // SCRATCHPAD.md must be at app root (§14)
      if (!fileExists(appPath, 'SCRATCHPAD.md')) {
        report(ERROR, appDir, `Missing SCRATCHPAD.md (required at app root, §14)`);
        projectViolations++;
      }

      // Required directories
      if (!fileExists(projPath, 'reports')) {
        report(ERROR, projDir, `Missing required directory: reports/`);
        projectViolations++;
      } else {
        if (!fileExists(projPath, 'reports/bug-reports.md')) {
          report(WARN, projDir, `Missing reports/bug-reports.md (create even if empty)`);
          projectViolations++;
        }
        if (!fileExists(projPath, 'reports/deployment-report.md')) {
          report(WARN, projDir, `Missing reports/deployment-report.md (create even if empty)`);
          projectViolations++;
        }
      }

      // Check for technical debt file
      // Exception: v1 projects with no phase files at all are fresh bootstraps — debt file is not required yet
      const allProjectFiles = readdirSync(projPath);
      const anyPhaseFiles = allProjectFiles.filter(f => /^phase-\d+/.test(f));
      const debtFiles = allProjectFiles.filter(f => /^phase-\d+-technical-debt/.test(f));
      const isFreshV1 = /^v1-/.test(projDir) && anyPhaseFiles.length === 0;
      if (debtFiles.length === 0 && !isFreshV1) {
        report(WARN, projDir, `No technical debt file found (phase-N-technical-debt-to-vX.md)`);
        projectViolations++;
      } else {
        for (const debtFile of debtFiles) {
          if (!/to-v\d+\.md$/.test(debtFile)) {
            report(WARN, projDir, `Technical debt file missing version suffix: ${debtFile} (expected: phase-N-technical-debt-to-vX.md)`);
          } else {
            // Validate that target version = current version + 1
            const versionMatch = projDir.match(/^v(\d+)-/);
            const targetMatch = debtFile.match(/to-v(\d+)\.md$/);
            if (versionMatch && targetMatch) {
              const currentVersion = parseInt(versionMatch[1], 10);
              const targetVersion = parseInt(targetMatch[1], 10);
              if (targetVersion !== currentVersion + 1) {
                report(WARN, projDir, `Debt file version target mismatch: ${debtFile} targets v${targetVersion} but project is v${currentVersion} (expected to-v${currentVersion + 1}.md)`);
              }
            }
          }
        }
      }

      // Validate BUG-NNN sequence
      const bugFile = join(projPath, 'reports', 'bug-reports.md');
      const bugIds = extractIds(bugFile, /ISSUE-[a-z0-9-]+-\d+/gi);
      validateSequentialIds(bugIds, 'ISSUE', projDir);

      // Validate TD-NN sequence
      for (const debtFile of debtFiles) {
        const debtPath = join(projPath, debtFile);
        const tdIds = extractIds(debtPath, /TECH-[a-z0-9-]+-\d+/gi);
        validateSequentialIds(tdIds, 'TECH', projDir);
      }

      // Check header depth in README
      checkHeaderDepth(join(projPath, 'README.md'), projDir);

      // Check phase files for header depth and code blocks
      const phaseFiles = readdirSync(projPath).filter(f => /^phase-\d+-.*\.md$/.test(f));
      for (const pf of phaseFiles) {
        checkHeaderDepth(join(projPath, pf), projDir);
        checkFencedCodeBlocks(join(projPath, pf), projDir);
      }

      // Scan for unknown elements in project dir
      scanUnknownElements(projPath, projDir);

      if (projectViolations === 0) {
        passCount++;
      }
    }
  }
}

// ─── Formalize unknowns as TD entries ───────────────────────────────────────
function formalizeUnknowns() {
  if (unknowns.length === 0) return;

  const debtPath = join(
    APPS_ROOT,
    'core-standard', 'development', 'v1-core-standard', 'phase-2-technical-debt-to-v2.md'
  );

  if (!existsSync(debtPath)) {
    console.log(`${ERROR} Cannot formalize: debt file not found at ${debtPath}`);
    return;
  }

  let content = readFileSync(debtPath, 'utf-8');

  // Find next TD number
  const existing = [...content.matchAll(/^### TD-(\d+)/gm)];
  let nextNum = existing.length > 0
    ? Math.max(...existing.map(m => parseInt(m[1], 10))) + 1
    : 1;

  const summaryMarker = '## Technical Debt Summary';
  const summaryIdx = content.indexOf(summaryMarker);

  let newEntries = '';
  const tableRows = [];

  for (const u of unknowns) {
    // Dedup: skip if this element+project combination is already in the debt file
    const dedupKey = `Unknown element: ${u.element} in ${u.project}`;
    if (content.includes(dedupKey)) continue;

    const id = `TD-${String(nextNum).padStart(2, '0')}`;
    newEntries += `\n---\n\n### ${id} — Unknown element: ${u.element} in ${u.project}\n\n`;
    newEntries += `**Discovered:** ${new Date().toISOString().slice(0, 10)} — unknown element scan — check-structure.mjs\n`;
    newEntries += `**File:** \`${relative(APPS_ROOT, join(u.projPath, u.element))}\`\n`;
    newEntries += `**Issue:** Element \`${u.element}\` is present but not covered by the standard.\n`;
    newEntries += `**Impact:** Normative candidate ignored — pull cycle never triggers.\n`;
    newEntries += `**Risk:** Low\n\n`;
    newEntries += `- [ ] Decide: Ignore / Move to standard location / Formalize as new convention\n\n`;
    newEntries += `**Effort:** 10 min\n`;

    tableRows.push(`| ${id} | Unknown element: ${u.element} in ${u.project} | 10 min | 📋 Open |`);
    nextNum++;
  }

  // Insert before summary table
  if (summaryIdx !== -1) {
    content = content.slice(0, summaryIdx) + newEntries + '\n' + content.slice(summaryIdx);
    // Append rows to table
    content = content.replace(
      /(\| TD-\d+ \|[^\n]+\|\n)(?!\| TD)/gm,
      (match) => match
    );
    // Append rows at end of table
    const lastRow = content.match(/(\| TD-\d+ \|[^\n]+\|)\n\n/);
    if (lastRow) {
      content = content.replace(lastRow[0], lastRow[1] + '\n' + tableRows.join('\n') + '\n\n');
    }
  } else {
    content += newEntries;
  }

  writeFileSync(debtPath, content, 'utf-8');
  console.log(`\n${OK} ${unknowns.length} unknown(s) formalized as TD entries in:\n   ${debtPath}\n`);
}

// ─── Output ─────────────────────────────────────────────────────────────────
function printReport() {
  console.log('\n═══════════════════════════════════════════════════════════');
  console.log('  Applications Structure Validator');
  console.log('═══════════════════════════════════════════════════════════\n');

  if (violations.length === 0 && unknowns.length === 0) {
    console.log(`${OK} All ${projectCount} project(s) pass validation.\n`);
    return;
  }

  // Group by project
  const byProject = {};
  for (const v of violations) {
    if (!byProject[v.project]) byProject[v.project] = [];
    byProject[v.project].push(v);
  }

  for (const [project, projViolations] of Object.entries(byProject)) {
    const hasError = projViolations.some(v => v.severity === ERROR);
    const icon = hasError ? ERROR : WARN;
    console.log(`${icon} ${project}`);
    for (const v of projViolations) {
      console.log(`   ${v.severity} ${v.message}`);
    }
    console.log();
  }

  const errorCount = violations.filter(v => v.severity === ERROR).length;
  const warnCount = violations.filter(v => v.severity === WARN).length;

  // Unknown elements section
  if (unknowns.length > 0) {
    console.log(`${UNKNOWN} NORMATIVE CANDIDATES — elements not covered by the standard\n`);
    for (const u of unknowns) {
      console.log(`   ${UNKNOWN} [${u.project}] \`${u.element}\``);
    }
    console.log();
    if (FORMALIZE) {
      formalizeUnknowns();
    } else {
      console.log(`  → Run with --formalize to auto-create TD entries in core-standard debt file.
  → See \`core-squad/ocm-*.md\` for agent coordination instructions (non-structural, user-orchestrated)\n`);
    }
  }

  console.log('───────────────────────────────────────────────────────────');
  console.log(`  Projects: ${projectCount} | Passed: ${passCount} | Failed: ${projectCount - passCount}`);
  console.log(`  Errors: ${errorCount} | Warnings: ${warnCount} | Unknowns: ${unknowns.length}`);
  console.log('═══════════════════════════════════════════════════════════\n');

  if (errorCount > 0) {
    process.exit(1);
  }
}

scanApplications();
printReport();

// ─── Usage hint ─────────────────────────────────────────────────────────────
// node check-structure.mjs [path-to-core-ferule]
// node check-structure.mjs [path-to-core-ferule] --formalize
//
// Note: HEARTBEAT.md, phase-*.md, llms.txt, ocm-*.md are intentionally ignored
// — they are documentation/coordination files, not structural elements.
