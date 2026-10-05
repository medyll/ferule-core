# CLAW.md — core-squad

## Identity

`core-squad` is the central orchestrator and coordination layer of the ferule-core cluster.
It coordinates communication between other core modules and external agents.

## Communication context

| Direction | Channel | Format |
|-----------|---------|--------|
| Receives missions | `place-de-greve/missions/` | JSON file (polled 5s) |
| Routes to modules | `core-*/nexus-protocol/CLAW.md` | Module-specific |
| Surfaces status | `production-dashboard.md` | Markdown table |

## Notes for inter-agent communication

- Core-squad does NOT have its own actions — it routes to other modules
- Uses `domain-registry.json` to map mission prefixes to project paths
- Produces consolidated status reports (e.g., `production-dashboard.md`)
- Alert aggregation target: `core-squad/nexus-protocol/` (appended markdown)
