# CLAW.md — core-workflow

## Identity

`core-workflow` is the BMAD-compliant orchestration layer for ferule-core modules.
It coordinates BMAD projects, manages sprints, and enforces the Chain Protocol.

## Communication context

| Direction | Channel | Format |
|-----------|---------|--------|
| Receives missions | `place-de-greve/missions/` | JSON file (polled 5s) |
| Receives alerts | `watchdog/alerts/` | JSON file (polled) |
| Routes to agents | `skill/*/SKILL.md` | Agent-specific |
| Reports status | `artifacts/status.txt` | Markdown table |

## Notes for inter-agent communication

- Core-workflow uses **BMAD protocol**, not Nexus Protocol
- Status file: `bmad/status.yaml` (canonical per `config/engine.yaml`)
- Role definitions: `config/roles.yaml` + `references/roles/*.md`
- Uses `CLAW.md` only for role handoff (not mission routing)
