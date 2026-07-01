# Core-Workflow — USER-NOTES

**Last Updated:** 2026-04-13

---

## User Instructions

- Ce module est le moteur workflow pour tout `core-ferule/`.
- Les commandes utilisent le préfixe `workflow` (pas `bmad`) pour éviter la confusion.
- La config centralisée est dans `config/` — ne pas dupliquer dans chaque projet.
- Le SKILL.md original de bmad-method reste dans `skills/bmad-method/` — il n'est pas supprimé.

---

## Décisions

| Date | Décision | Raison |
|------|----------|--------|
| 2026-04-13 | Migration vers core-workflow/ | Centraliser le moteur et la config |
| 2026-04-13 | Commandes renommées `workflow` | Identité OpenClaw claire |
| 2026-04-13 | Config dans `config/` | Zone unique pour tout le workspace |

---

## TODO

- [ ] Tester `workflow init` sur un projet fictif
- [ ] Vérifier que `engine.mjs` fonctionne avec les nouveaux chemins
- [ ] Documenter l'intégration avec core-ferule-engine
