# Technical Debt — v1-core-workflow → v2

**Source:** v1-core-workflow
**Target Version:** V2
**Date:** 2026-04-13

---

## Overview

Technical debt accumulated during V1 that must be resolved before V2.

---

## Debt Items

| ID | Date | Category | Description | Priority | Status |
|----|------|----------|-------------|----------|--------|
| TD-001 | 2026-04-13 | Config | `config/` directory formalized as normative candidate — needs standard integration | Medium | Open |
| TD-002 | 2026-04-13 | Structure | 7 transient unknowns formalized (artifacts, references, source, etc.) — review if any should be normative | Low | Open |
| TD-003 | 2026-04-13 | Integration | `engine.mjs` reads `./bmad/config.yaml` — needs update to read `config/engine.yaml` | Medium | Open |

---

## V2 Planned

- [ ] Integrate `config/` pattern into core-standard (new section: "Centralized Workspace Config")
- [ ] Update `engine.mjs` to use centralized config paths
- [ ] Test `workflow init` on a fresh project
- [ ] Document cross-workflow hooks in workspace.yaml
