# CLAW.md — core-ferule-engine

## Identity

`core-ferule-engine` is the autonomous rule engine of the ferule-core cluster.
It does not initiate communication — it reacts to missions and alerts.

## Communication context

| Direction | Channel | Format |
|-----------|---------|--------|
| Receives missions | `mission-queue/missions/` | JSON file (polled 5s) |
| Routes to LLM | `token-strategie/missions/` | JSON file write |
| Receives requests | `POST /process` | REST (FastAPI) |

## Notes for inter-agent communication

- Engine actions are `route`, `log`, `hook` — no direct LLM calls from this module.
- Skill discovery is internal only (closed ferule space, not exposed externally).
