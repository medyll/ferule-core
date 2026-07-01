# CLAW.md — core-openspace

## Identity

`core-openspace` is the shared thinking space and memory hub of the ferule-core cluster.
It provides persistent context, shared knowledge, and agent coordination functions.

## Communication context

| Direction | Channel | Format |
|-----------|---------|--------|
| Receives thoughts | `place-de-greve/missions/` | JSON file (polled 5s) |
| Receives alerts | `watchdog/alerts/` | JSON file (polled) |
| Surfaces context | `workspace/agents/openspace.md` | Markdown |
| Receives requests | `POST /context` | REST (FastAPI) |

## Notes for inter-agent communication

- Core-openspace aggregates agent queries and responses for shared memory
- Uses `protocol.json` for internal protocol definitions
- Context window management: CNS (Context Navigation System)
- State persistence: `agents/`, `memory/`, `synapse/` directories
