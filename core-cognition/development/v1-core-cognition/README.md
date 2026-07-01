# core-cognition — V1

> **Date:** 2026-04-12
> **Status:** 📋 Planned
> **Version:** v1-core-cognition

## Overview

`core-cognition` is the ear of OpenClaw. It receives raw intent from any source (human, TUI, VSCode), interprets the need via `machinery`, and routes to the correct domain handler through Place de Grève.

> Logs are cognition. If core-ferule sees its own logs, that is metacognition.

## Sources

- `core-ferule/core-cognition/USER-NOTES.md`
- `core-ferule/core-cognition/SCRATCHPAD.md`
- `core-ferule/machinery/development/v1-machinery/classifier.mjs`

## Structure

| File | Description |
|------|-------------|
| `llms.txt` | Machine-readable index |
| `README.md` | This file |
| `USER-NOTES.md` | User instructions |
| `reports/bug-reports.md` | Bug tracking |
| `reports/deployment-report.md` | Deployment summary |

## Dependencies

| Dependency | Role |
|------------|------|
| `machinery/classifier.mjs` | Intent classification |
| `place-de-greve/domain-registry.json` | Domain source of truth |
| Place de Grève V6 | Queue handler |
