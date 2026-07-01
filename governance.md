# Applications — Governance

> Part C of the Applications norm. Defines how the norm itself is managed.
> Governed by `core-standard`. See [README.md](./README.md) for index.

---

## 18. Norm Governance

> This document set is governed by `core-standard`. Do not edit directly — changes must be proposed and versioned through `application-core/core-standard/`.

### Pull Cycle

Changes to the norm originate from real application practices:

1. An unknown element is detected by `check-structure.mjs`
2. It is evaluated for normative value via `[core-normalize]`
3. If normative → integrated into `structure.md`, `behaviour.md`, or `governance.md`
4. If transient → logged as TD entry in `core-standard/development/v1-core-standard/phase-2-technical-debt-to-v2.md`

### Version Governance

| File | Role |
|------|------|
| `README.md` | Index — entry point only |
| `structure.md` | Part A — structural rules |
| `behaviour.md` | Part B — behavioural rules |
| `governance.md` | Part C — norm governance |
| `core-standard/scripts/check-structure.mjs` | Automated validator |
| `core-standard/development/v1-core-standard/templates/` | Document templates |
