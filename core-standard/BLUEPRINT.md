# core-standard — BLUEPRINT

**Version:** 2.0
**Date:** 2026-04-11
**Status:** Normative — governs all core-ferule modules

---

## Overview

`core-standard` is the **normative engine** for the `core-ferule` (now `ferule-core`) ecosystem. It defines structure, formatting, and governance rules that every application must follow. It is self-improving: when unknown elements exhibit normative value, the standard rewrites itself to incorporate them.

## Architecture

### Pull/Push Cycle

```
Applications (real usage)
    ↓
core-standard observes unknown elements
    ↓
[core-normalize] evaluates normative value
    ↓
Standard rewrites itself (core-ferule/README.md, check-structure.mjs)
    ↓
[core-diffuse] propagates updated norm to applications
```

### Commands

| Command | Trigger | Purpose |
|---------|---------|---------|
| `[core-bootstrap]` | BLUEPRINT exists, no development/ | Scaffold v1 project automatically |
| `[core-rationalize]` | Human request | Convert SCRATCHPAD → BLUEPRINT |
| `[core-atlas]` | Human request | Document ecosystem state |
| `[core-validate]` | Auto after validate | Run structure/compliance checks |
| `[core-normalize]` | Auto after validate | Evaluate & integrate unknown elements |
| `[core-status]` | Human request | Report norm version & conformity |
| `[core-diffuse]` | Human request | Propagate rules to external apps |

## Key Files

| File | Role |
|------|------|
| `scripts/check-structure.mjs` | Structure validator — scans all apps for conformance |
| `USER-NOTES.md` | Norm version, conformance rules, preferences |
| `skill/core-standard/SKILL.md` | Command definitions (8 commands) |
| `development/v1-core-standard/` | V1 scaffold — formatting & structure standard |
| `development/v2-core-standard/` | V2 — self-improving norm, pull cycle |

## Normative Criteria

An unknown element is integrated into the standard if ≥2 criteria met:

| Criterion | Question |
|-----------|----------|
| Structure | Does it define a format, structure, or convention? |
| Reusability | Could other applications benefit from this pattern? |
| Intent | Is it deliberate (not accidental/temporary)? |
| Completeness | Does it have enough content to formalize? |

## Current State

| Component | Status |
|-----------|--------|
| V1 (formatting & structure) | ✅ Complete |
| V2 (self-improving norm) | ✅ Complete |
| V3 (technical debt) | 📋 Open |
| Validator (`check-structure.mjs`) | ✅ Active |
| Application conformance | 🔄 Ongoing |
