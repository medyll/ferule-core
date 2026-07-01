#!/usr/bin/env node
/**
 * maintenance-scanner.mjs
 *
 * GENERIC MAINTENANCE & DIAGNOSTIC SCANNER
 *
 * Purpose:
 *   Provides `core-squad` with a tool to inspect the health of ANY target file
 *   (Queue, YAML config, JSON log) without coupling to specific application logic.
 *
 * Usage:
 *   node maintenance-scanner.mjs --target <file_path> --type <queue|yaml|json|generic>
 *
 * Output:
 *   Returns a structured JSON report to STDOUT.
 */

import { readFileSync, existsSync, statSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

// Removed js-yaml import to ensure zero external dependencies.
// The scanner focuses on Queue (Markdown) and Generic (Text) analysis.
// YAML/JSON validation can be added back if dependencies are guaranteed.

const __dirname = dirname(fileURLToPath(import.meta.url));
const AUDIT_LOG = join(__dirname, '..', '.openclaw', 'runtime', 'ocm-audit-trail.log');

/**
 * Log to audit trail
 */
function auditLog(level, source, message) {
  try {
    const timestamp = new Date().toISOString();
    const entry = `[${timestamp}] [${level}] [${source}] - ${message}\n`;

    if (existsSync(AUDIT_LOG)) {
      const current = readFileSync(AUDIT_LOG, 'utf-8');
      // Keep log small: only last 50 lines
      const lines = current.split('\n');
      const kept = lines.slice(-50);
      writeFileSync(AUDIT_LOG, kept.join('\n') + (kept.join('\n').endsWith('\n') ? '' : '\n') + entry, 'utf-8');
    } else {
      writeFileSync(AUDIT_LOG, entry, 'utf-8');
    }
  } catch (err) {
    // Silent fail if audit log is locked/unwritable
  }
}

/**
 * Parse arguments
 */
function parseArgs() {
  const args = process.argv.slice(2);
  const params = {};
  for (let i = 0; i < args.length; i++) {
    if (args[i].startsWith('--')) {
      params[args[i].slice(2)] = args[i + 1];
    }
  }
  return params;
}

/**
 * Generic Health Check for a File
 */
function scanFile(filePath, type) {
  const report = {
    target: filePath,
    status: 'unknown',
    exists: false,
    size: 0,
    lastModified: null,
    details: {},
    errors: []
  };

  try {
    if (!existsSync(filePath)) {
      report.status = 'missing';
      report.errors.push(`Target file not found: ${filePath}`);
      return report;
    }

    report.exists = true;
    const stats = statSync(filePath);
    report.size = stats.size;
    report.lastModified = stats.mtime.toISOString();

    if (stats.size === 0) {
      report.status = 'empty';
      return report;
    }

    const content = readFileSync(filePath, 'utf-8');
    const lines = content.split('\n');
    report.details.lineCount = lines.length;

    // TYPE-SPECIFIC ANALYSIS
    if (type === 'queue') {
      report.details = analyzeQueue(content, lines);
    } else if (type === 'yaml') {
      report.details = analyzeYaml(content, filePath);
    } else if (type === 'json') {
      report.details = analyzeJson(content, filePath);
    } else {
      report.details = analyzeGeneric(content, lines);
    }

  } catch (err) {
    report.status = 'error';
    report.errors.push(err.message);
  }

  return report;
}

/**
 * Analyze Markdown Queue (e.g., Place de Grève)
 */
function analyzeQueue(content, lines) {
  const details = { missionsByStatus: {}, totalMissions: 0, hasHeaders: false, columns: [], errors: [] };

  // Robust Table Detection
  let tableStartIndex = -1;
  for (let i = 0; i < lines.length; i++) {
    // Markdown table separators can be |---| or |----| or |:---|
    if (lines[i].includes('|') && lines[i].includes('---')) {
      tableStartIndex = i + 1;
      break;
    }
  }

  if (tableStartIndex === -1) {
    details.errors.push('No Markdown table detected');
    return details;
  }

  // Parse rows
  for (let i = tableStartIndex; i < lines.length; i++) {
    const line = lines[i];
    if (!line.trim().startsWith('|')) break; // End of table
    if (line.includes('|---|')) continue; // Skip separators if multiple

    // Split and clean parts
    const parts = line.split('|').map(p => p.trim()).filter(p => p);
    
    // If it looks like a data row (has enough columns)
    if (parts.length >= 4) {
      details.totalMissions++;
      
      // Search for status keywords in any part of the row
      // Common statuses: in-progress, ready, paused, done, complete, blocked, waiting-priority
      const statusPattern = /^(in-progress|ready|paused|done|complete|blocked|waiting-priority)$/i;
      const foundStatus = parts.find(p => statusPattern.test(p));

      if (foundStatus) {
        const s = foundStatus.toLowerCase();
        details.missionsByStatus[s] = (details.missionsByStatus[s] || 0) + 1;
      } else {
        // Fallback
        details.missionsByStatus['unknown_status'] = (details.missionsByStatus['unknown_status'] || 0) + 1;
      }
    }
  }

  // Determine overall health
  if (details.totalMissions === 0) {
    details.health = 'empty';
  } else {
    const blocked = details.missionsByStatus['blocked'] || 0;
    const inProgress = details.missionsByStatus['in-progress'] || 0;
    const ready = details.missionsByStatus['ready'] || 0;
    
    if (blocked > 0) details.health = 'critical';
    else if (inProgress > 5 && ready === 0) details.health = 'stalled'; // Heuristic for deadlock
    else details.health = 'healthy';
  }

  return details;
}

/**
 * Analyze YAML (Fallback: Basic Text Check)
 */
function analyzeYaml(content, filePath) {
  const details = { valid: false, structure: {}, errors: [] };
  try {
    // Basic check: does it look like YAML? (key: value)
    if (/^\s*[\w_-]+:/.test(content)) {
      details.valid = true;
      details.errors.push('YAML parsing requires js-yaml dependency (not installed). Content looks valid.');
    }
  } catch (err) {
    details.valid = false;
    details.errors.push(err.message);
  }
  return details;
}

/**
 * Analyze JSON
 */
function analyzeJson(content, filePath) {
  const details = { valid: false, structure: {}, errors: [] };
  try {
    const data = JSON.parse(content);
    details.valid = true;
    if (typeof data === 'object' && data !== null) {
      details.structure = Object.keys(data);
    }
  } catch (err) {
    details.valid = false;
    details.errors.push(err.message);
  }
  return details;
}

/**
 * Generic Fallback Analysis
 */
function analyzeGeneric(content, lines) {
  return {
    type: 'text',
    summary: content.substring(0, 100) + '...',
    wordCount: content.split(/\s+/).length
  };
}

/**
 * Main Execution
 */
function main() {
  const { target, type = 'generic' } = parseArgs();

  if (!target) {
    console.error(JSON.stringify({ status: 'error', message: 'Missing --target argument' }));
    process.exit(1);
  }

  // Resolve path relative to current working directory
  const resolvedTarget = target.startsWith('.') ? join(process.cwd(), target) : target;

  auditLog('INFO', 'MAINT-SCANNER', `Scanning ${type} target: ${resolvedTarget}`);
  
  const report = scanFile(resolvedTarget, type);
  
  auditLog('INFO', 'MAINT-SCANNER', `Scan complete. Status: ${report.status}`);
  console.log(JSON.stringify(report, null, 2));
}

main();
