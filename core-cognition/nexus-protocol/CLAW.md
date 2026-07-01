# CLAW.md — core-cognition

## Identity

`core-cognition` is the thinking and reasoning engine of the ferule-core cluster.
It provides embedding generation, semantic search, and cognitive memory functions.

## Communication context

| Direction | Channel | Format |
|-----------|---------|--------|
| Receives queries | `core-openspace/queries/` | JSON file |
| Receives alerts | `watchdog/alerts/` | JSON file (polled) |
| Routes to LLM | `token-strategie/missions/` | JSON file write |
| Surfaces embeddings | `embeddings/*.json` | JSON array |

## Notes for inter-agent communication

- Core-cognition generates embeddings for semantic memory retrieval
- Uses `embeddings/embed-model.json` for model configuration
- SCRATCHPAD.md provides quick thinking space for agent queries
- No direct file bus — rely on `core-openspace` for message passing
