---
name: core-cognition
description: |-
  OpenClaw listener and intent interpreter. Receives raw intent from any source (human, TUI, VSCode), interprets the need, classifies it via machinery, and routes to the correct domain handler through Place de Grève.
  Supports explicit commands and natural language detection.
argument-hint: "idee, livre, projet, status, maturation, or free text"
user-invocable: true
---

# core-cognition — OpenClaw Listener

## Purpose

`core-cognition` is the ear of OpenClaw. It listens, interprets, and routes.

Two modes:
- **Explicit command** — domain resolved immediately, no classification needed
- **Natural language** — classifier.mjs determines the domain

## Commands (Explicit Mode)

Commands are derived from `domain-registry.json` — any domain with a `prefix` is a valid command.
Adding a domain to the registry automatically creates a new command.

| Command | Domain | Example |
|---------|--------|---------|
| `[idee]` | `capture` | `[idee] app de gestion de notes` |
| `[livre]` | `authoring` | `[livre] roman sur l'IA et la mémoire` |
| `[projet]` | `development` | `[projet] idae-machine avancement` |
| `[status]` | `core-squad` | `[status]` |
| `[maturation]` | `maturation` | `[maturation] concept de marketplace` |

## Natural Language Detection (Dynamic Mode)

If no explicit command is given, `core-cognition` detects intent from free text.

### Detected patterns

| Pattern | Domain inferred |
|---------|----------------|
| `"idée [nouvelle] ..."` | `capture` ou `authoring` selon contexte |
| `"projet <nom> [consulter|avancer|status]"` | `development` |
| `"où en sont mes projets"` | `core-squad` |
| `"livre / roman / écrire ..."` | `authoring` |
| `"relancer / restart / watcher"` | `core-squad` |

### Ambiguity protocol

1. Run `classifier.mjs` against the intent
2. If `confidence >= 0.6` → submit to Place de Grève directly
3. If ambiguous → confirm with user: *"Je classe ça dans `[domain]`. Correct ?"*
4. Submit with resolved `context:domain`

## Sequence (any mode)

1. Read `place-de-greve/domain-registry.json` — available domains
2. Resolve domain (explicit command OR classifier)
3. Confirm if ambiguous
4. Submit mission to Place de Grève with `context:domain`

## What core-cognition does NOT do

- It does not manage missions — Place de Grève does
- It does not execute work — domain handlers do
- It does not store state — machinery is stateless

## Key Files

| File | Role |
|------|------|
| `machinery/development/v1-machinery/classifier.mjs` | Intent classifier |
| `place-de-greve/domain-registry.json` | Domain source of truth — drives commands |
| `place-de-greve.md` | Mission queue |
