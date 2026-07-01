# core-standard

**Version:** V2 Operational | V3 Technical Debt
**Role:** Normative Engine — governs all ferule-core applications

---

## Overview

`core-standard` defines and enforces structure, formatting, and governance rules across the `ferule-core` ecosystem. It is a **self-improving standard**: when applications develop practices that have normative value, core-standard absorbs them and propagates the updated norm.

## Commands

| Command | Purpose |
|---------|---------|
| `[core-bootstrap]` | Auto-scaffold v1 for new applications |
| `[core-validate]` | Run structure & compliance checks |
| `[core-normalize]` | Evaluate & integrate unknown elements |
| `[core-atlas]` | Document ecosystem state |
| `[core-rationalize]` | Convert SCRATCHPAD → BLUEPRINT |
| `[core-status]` | Report norm version & conformity |
| `[core-diffuse]` | Propagate rules to external apps |

## Projects

| Project | Status | Description |
|---------|--------|-------------|
| [v1-core-standard](./development/v1-core-standard/README.md) | ✅ Complete | Formatting & structure standard |
| [v2-core-standard](./development/v2-core-standard/README.md) | ✅ Complete | Self-improving norm, pull cycle |
| [v3-core-standard](./development/v3-core-standard/) | 🔄 In Progress | Technical debt resolution |

## Infrastructure

| File | Role |
|------|------|
| `scripts/check-structure.mjs` | Validator — scans all apps for conformance |
| `skill/core-standard/SKILL.md` | 8 command definitions |
| `USER-NOTES.md` | Norm preferences and instructions |

---

## Codification

Norm versions follow semantic versioning. Current active norm: **V2**.
All applications under `ferule-core/` must conform.
