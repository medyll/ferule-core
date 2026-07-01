#!/usr/bin/env node
/**
 * index.mjs - OpenClaw Master Main Orchactor
 * Primary entry point for the core-squad system.
 * 
 * Responsibilities:
 * - Read user instructions from ocm-INSTRUCTIONS.md
 * - Manage mission queue (ocm-MISSION-QUEUE.md)
 * - Spawn and manage Sub-Agents
 * - Execute autonomous missions
 * - Report status to ocm-STATUS-REPORT.md
 * - Log all telemetry to .openclaw/runtime/ocm-audit-trail.log
 */

import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = __dirname;
const RUNTIME_DIR = join(ROOT, '.openclaw', 'runtime');
const INSTRUCTIONS_FILE = join(ROOT, 'ocm-INSTRUCTIONS.md');
const MISSION_QUEUE_FILE = join(ROOT, 'ocm-MISSION-QUEUE.md');
const STATUS_REPORT_FILE = join(ROOT, 'ocm-STATUS-REPORT.md');
const AUDIT_LOG_FILE = join(RUNTIME_DIR, 'ocm-audit-trail.log');

/**
 * Ensure runtime directories exist
 */
function ensureRuntime() {
  if (!existsSync(RUNTIME_DIR)) {
    mkdirSync(RUNTIME_DIR, { recursive: true });
  }
}

/**
 * Log to audit trail
 */
function auditLog(level, source, message) {
  const timestamp = new Date().toISOString();
  const entry = `[${timestamp}] [${level}] [${source}] - ${message}\n`;
  
  if (existsSync(AUDIT_LOG_FILE)) {
    const current = readFileSync(AUDIT_LOG_FILE, 'utf-8');
    writeFileSync(AUDIT_LOG_FILE, current + entry, 'utf-8');
  }
}

/**
 * Read user instructions
 */
function readInstructions() {
  if (!existsSync(INSTRUCTIONS_FILE)) {
    return { active: [], completed: [] };
  }
  
  const content = readFileSync(INSTRUCTIONS_FILE, 'utf-8');
  
  // Check for critical failure marker
  if (content.includes('[CRITICAL_FAILURE]')) {
    auditLog('CRITICAL', 'MASTER', 'Critical failure detected in instructions - human intervention required');
    console.error('[CRITICAL] System paused - [CRITICAL_FAILURE] marker detected in ocm-INSTRUCTIONS.md');
    process.exit(1);
  }
  
  return {
    active: extractSection(content, 'Active Instructions'),
    completed: extractSection(content, 'Completed Instructions')
  };
}

/**
 * Extract section from markdown file
 */
function extractSection(content, sectionName) {
  const sectionRegex = new RegExp(`## ${sectionName}\\n([\\s\\S]*?)(?=##|$)`);
  const match = content.match(sectionRegex);
  return match ? match[1].trim() : '';
}

/**
 * Check for OCM-SIMULATE or OCM-PROCEED commands
 */
function checkCommands(activeInstructions) {
  const commands = {
    simulate: activeInstructions.includes('OCM-SIMULATE'),
    proceed: activeInstructions.includes('OCM-PROCEED')
  };
  
  return commands;
}

/**
 * Update status report
 */
function updateStatusReport(report) {
  const timestamp = new Date().toISOString();
  const content = readFileSync(STATUS_REPORT_FILE, 'utf-8');
  const updated = content.replace(
    /## Last Report\n[^\n]+/,
    `## Last Report\n${timestamp}`
  );
  
  // Insert report content
  let finalContent = updated;
  if (report.summary) {
    finalContent = finalContent.replace(
      /## Executive Summary\n[^\n]*/,
      `## Executive Summary\n${report.summary}`
    );
  }
  
  writeFileSync(STATUS_REPORT_FILE, finalContent, 'utf-8');
  auditLog('INFO', 'MASTER', 'Status report updated');
}

/**
 * Initialize system
 */
function initialize() {
  ensureRuntime();
  
  auditLog('INFO', 'MASTER', 'core-squad initializing...');
  auditLog('INFO', 'MASTER', 'Runtime directory: ' + RUNTIME_DIR);
  auditLog('INFO', 'MASTER', 'Mission queue: ' + MISSION_QUEUE_FILE);
  
  console.log('[INIT] core-squad v1.0.0');
  console.log('[INIT] Checking system state...');
  
  const instructions = readInstructions();
  const commands = checkCommands(instructions.active);
  
  if (commands.simulate) {
    console.log('[SIMULATE] Simulation mode detected');
    auditLog('INFO', 'MASTER', 'OCM-SIMULATE mode activated');
    
    updateStatusReport({
      summary: 'Simulation mode active - awaiting OCM-PROCEED to execute planned operations'
    });
    
    console.log('[SIMULATE] Plan written to ocm-STATUS-REPORT.md');
    console.log('[SIMULATE] Waiting for OCM-PROCEED in ocm-INSTRUCTIONS.md');
  } else if (commands.proceed) {
    console.log('[PROCEED] Executing planned operations');
    auditLog('INFO', 'MASTER', 'OCM-PROCEED received - executing planned operations');
  } else {
    console.log('[IDLE] System ready - awaiting instructions');
    auditLog('INFO', 'MASTER', 'System initialized and ready');
  }
  
  console.log('[READY] core-squad is operational');
  return true;
}

// Run initialization
const success = initialize();

if (success) {
  // System is ready - in a real implementation, this would start the main event loop
  // For now, we exit cleanly after initialization
  process.exit(0);
}
