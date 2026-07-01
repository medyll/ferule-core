# Core Standard V2

> **Date:** 2026-04-12
> **Status:** Phase 1 ✅ | Phase 2 ✅ — V2 fully consolidated, V3 TD backlog ready

## Sources

- V1 Debt: [`../v1-core-standard/phase-2-technical-debt-to-v2.md`](../v1-core-standard/phase-2-technical-debt-to-v2.md)
- Phase 1: [`phase-1-repair.md`](phase-1-repair.md)
- Phase 2: [`phase-2-technical-debt-to-v3.md`](phase-2-technical-debt-to-v3.md)

## Overview

V2 resolves the 7 open normative TDs from V1, closes all 15 unknown-element TDs, and formalizes 2 new conventions (protocol.json, domain-registry.json). Phase 1 + Phase 2 complete.

## Structure

| File | Content |
|------|---------|
| [phase-1-repair.md](phase-1-repair.md) | 8 steps — all ✅ done |
| [phase-2-technical-debt-to-v3.md](phase-2-technical-debt-to-v3.md) | 4 steps — all ✅ done |

## Current System State

| Component | Status |
|-----------|--------|
| structure.md | ✅ V2 updated (7 new sections: §3.1, §3.2, §8.1, §13.2, §13.3, §16, §17) |
| behaviour.md | ✅ V2 updated (status-dashboard.md generation rule) |
| check-structure.mjs | ✅ V2 updated (KNOWN_FILES: 11 items, KNOWN_DIRS: 10 items) |
| V1 debt file | ✅ All 25/25 TDs closed with V2 references |
| V2 TD backlog | ✅ 4/4 TDs done (protocol.json, domain-registry, transient closure, app-level TD) |
| V2 scaffold | ✅ Complete (README, llms.txt, phases, reports) |
