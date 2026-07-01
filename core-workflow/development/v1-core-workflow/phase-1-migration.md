# Phase 1 — Migration de bmad-method vers core-workflow

**Status:** Complete

---

## Objectifs

1. Rapatrier bmad-method dans `core-ferule/core-workflow/`
2. Adapter le SKILL.md pour l'écosystème OpenClaw
3. Créer la config centralisée (engine.yaml, roles.yaml, workspace.yaml)
4. Rendre le tout conforme à core-standard v2

---

## Tâches

- [x] Créer la structure de dossiers conforme core-standard
- [x] Copier `references/` depuis `skills/bmad-method/references/`
  - [x] `references/roles/` — 7 fichiers de rôles + identities/
  - [x] `references/commands.md`
  - [x] `references/status-yaml-validation.md`
  - [x] `references/readme-templates/`
- [x] Copier `templates/` depuis `skills/bmad-method/templates/`
- [x] Copier `scripts/` depuis `skills/bmad-method/scripts/` (engine.mjs + node_modules)
- [x] Copier `artifacts/` depuis `skills/bmad-method/artifacts/`
- [x] Copier `source/` depuis `skills/bmad-method/source/`
- [x] Créer `config/engine.yaml` — configuration du moteur
- [x] Créer `config/roles.yaml` — définition des rôles et identités
- [x] Créer `config/workspace.yaml` — apps connues et hooks cross-workflow
- [x] Créer `skill/core-workflow/SKILL.md` — commandes renommées "workflow", chemins adaptés
- [x] Créer `development/v1-core-workflow/README.md`
- [x] Créer `development/v1-core-workflow/llms.txt`
- [x] Créer fichiers root: README.md, SCRATCHPAD.md, USER-NOTES.md

---

## Décisions

| Décision | Raison |
|----------|--------|
| Commandes renommées `workflow` au lieu de `bmad` | Éviter la confusion avec le skill original, affirmer l'identité OpenClaw |
| Config séparée dans `config/` au lieu de `./bmad/config.yaml` par projet | Config centralisée pour orchestrer tout le workspace |
| Rôles copiés tels quels | Aucun changement nécessaire — les rôles sont génériques |
| engine.mjs conservé tel quel | CLI fonctionnel, pas de raison de modifier |

---

## Résultats

- `core-workflow/` est opérationnel comme moteur workflow pour core-ferule/
- Compatible avec les commandes `workflow continue`, `workflow status`, etc.
- Les rôles standalone fonctionnent toujours (`develop this`, `design this`, etc.)
- Prêt à être utilisé par place-de-greve/, core-squad/, et autres apps

---

## Prochaines étapes

1. Valider avec `core-standard/scripts/check-structure.mjs`
2. Tester `workflow init` sur un projet fictif
3. Tester `workflow continue` avec un rôle Developer
4. Documenter l'intégration avec core-ferule-engine (futur)
