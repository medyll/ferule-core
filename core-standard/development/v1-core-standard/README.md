# Core Standards V1 — Formatting & Structure Standard

**Date:** 2026-04-10
**Status:** Phase 1 ✅ Complete | Phase 2 ✅ Complete

## Sources

- Applications README: `ferule-core/README.md`
- User Notes: `ferule-core/core-standard/USER-NOTES.md`
- Existing applications: `mission-queue/`, `core-squad/`

## Overview

V1 establishes the authoritative formatting and structure standard for all applications under `ferule-core/`. Consolidates conventions from existing applications into a single versioned standard, resolves inconsistencies, and provides enforcement tooling.

## Structure

| File | Content |
|------|---------|
| [phase-1-repair.md](phase-1-repair.md) | Standard consolidation — audit, resolve inconsistencies, enforcement tools |
| [phase-2-technical-debt-to-v2.md](phase-2-technical-debt-to-v2.md) | Outstanding standardization debt |
| [reports/bug-reports.md](reports/bug-reports.md) | Bug log |
| [reports/deployment-report.md](reports/deployment-report.md) | Deployment summary |

## Summary Table

| Step | Task | Effort | Depends on | Status |
|------|------|--------|------------|--------|
| **1.1** | Audit existing application structures for conformance | 15 min | — | ✅ |
| **1.2** | Resolve inconsistencies — define unified spec | 15 min | 1.1 | ✅ |
| **1.3** | Create `.markdownlint.json` for workspace-wide linting | 10 min | 1.2 | ✅ |
| **1.4** | Create `check-structure.mjs` validator script | 30 min | 1.2 | ✅ |
| **1.5** | Create `PROMPT-TEMPLATES.md` for agent startup | 15 min | 1.2 | ✅ |
| **1.6** | Propagate standard to existing applications | 30 min | 1.3–1.5 | ✅ |

## Current System State

| Component | Status |
|-----------|--------|
| Standard document | ✅ Defined |
| Linting tool | ✅ `.markdownlint.json` created |
| Structure validator | ✅ `check-structure.mjs` created |
| Prompt templates | ✅ `PROMPT-TEMPLATES.md` created |
| Application conformance | ✅ Assessed |
