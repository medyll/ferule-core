# core-openspace

> **Date:** 2026-04-12
> **Status:** 📋 Planned — v1 scaffold
> **Author:** Mydde

`core-openspace` is the inter-application protocol bus for `core-ferule`.
It is the single declaration point for all communication between core core-ferule.

---

## Role

Apps do not write ad hoc message files to each other.
They declare their events, handlers, and routing rules here — in `protocol.json`.

---

## Participants

| App | Domain |
|-----|--------|
| `place-de-greve` | Mission queue — task intake and dispatch |
| `core-squad` | Agent team management |
| `core-standards` | Norm governance |
| `core-cognition` | Reasoning and analysis |
| `formal-ideation` | Ideation and brainstorming |
| `openclaw-maintenance` | System health and repair |

---

## Design

- Protocol is declared in `protocol.json` — authoritative source for event types, participants, and routing rules.
- No app implements its own inter-app messaging. All cross-app communication is routed via declared handlers.
- Replaces the `ocm-INSTRUCTIONS.md` pattern (manual file-based messaging).

---

## Structure

| Path | Content |
|------|---------|
| `protocol.json` | Protocol declaration — participants, event types, routing rules |
| `USER-NOTES.md` | Operational guide |
| `SCRATCHPAD.md` | Freeform capture |
| `skill/core-openspace/SKILL.md` | Application skill |
| `bmad/CLAW.md` | BMAD context |
| `development/v1-core-openspace/` | v1 development scaffold |
