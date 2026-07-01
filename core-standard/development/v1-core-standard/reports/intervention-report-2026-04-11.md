# Rapport d'Intervention — core-standard — 2026-04-11

**Date:** 2026-04-11
**Status:** ✅ Remediated
**Author:** Claude Sonnet 4.6

---

## Objectif

Évaluer si `core-standard` est en capacité de jouer son rôle : détecter, forcer et propager la cohérence des normes sur toutes les applications.

---

## 1. Composants analysés

| Composant | Localisation |
|---|---|
| Skill déployé | `~/.claude/skills/core-standard/SKILL.md` |
| Skill workspace | `ferule-core/core-standard/skill/core-standard/SKILL.md` |
| Script validateur | `ferule-core/core-standard/scripts/check-structure.mjs` |
| Standard | `ferule-core/README.md` (sections 1–17) |
| Phase 1 | `development/v1-core-standard/phase-1-repair.md` |
| Dette technique | `development/v1-core-standard/phase-2-technical-debt-to-v2.md` |

---

## 2. Désynchronisation skill déployé ↔ workspace

Le skill déployé dans `~/.claude/skills/` était en retard sur le workspace.

| Commande | Skill déployé (avant) | Skill workspace |
|---|---|---|
| `core-bootstrap` | ✅ (ancienne version scaffold) | ✅ (version corrigée) |
| `core-validate` | ✅ | ✅ |
| `core-formalize` | ✅ | ✅ |
| `core-normalize` | ❌ absent | ✅ présent |
| `core-status` | ✅ | ✅ |

**Fix appliqué:** skill déployé remplacé par la version workspace (complète, avec `core-normalize`).

---

## 3. Lacunes du script `check-structure.mjs`

### Avant intervention

| Règle standard | Section | Statut |
|---|---|---|
| `skill/<app>/SKILL.md` requis | §15 | ❌ non vérifié |
| `reports/deployment-report.md` requis | §1,§6 | ❌ non vérifié |
| Cohérence version cible dette (`to-v<N+1>`) | §11 | ❌ non vérifié |
| Dedup dans `--formalize` | — | ❌ absent |

### Fixes appliqués

- ✅ Ajout check `skill/<app>/SKILL.md` (app-level, §15)
- ✅ Ajout check `reports/deployment-report.md`
- ✅ Ajout validation version cible dans filename dette
- ✅ Ajout dedup dans `formalizeUnknowns()` (skip si entrée déjà présente)

---

## 4. Conflit `core-bootstrap` vs §15

Le `core-bootstrap` générait un `SKILL.md` à la racine de l'app (`<app>/SKILL.md`).
§15 exige `skill/<app-name>/SKILL.md`.

**Fix appliqué:** scaffold diagram et instructions corrigés dans workspace SKILL.md.

---

## 5. Chemin d'invocation

Les commandes `[core-validate]` et `[core-formalize]` référençaient un chemin relatif
`core-standard/scripts/check-structure.mjs` — introuvable si CWD ≠ `workspace/ferule-core/`.

**Fix appliqué:** chemin absolu spécifié dans le skill.

---

## 6. Dette technique — duplication

TD-11 à TD-38 contenaient 27 entrées dont 15 doublons (3 cycles de formalize successifs sans dedup).

**Fix appliqué:**
- TD-11 à TD-22 conservés (entrées uniques)
- TD-23 ajouté (`bmad` in openclaw-master — seul élément nouveau dans les doublons)
- TD-24 à TD-38 supprimés (doublons purs)
- Table de synthèse reconstruite

---

## 7. Fichiers créés/modifiés

| Fichier | Action |
|---|---|
| `reports/intervention-report-2026-04-11.md` | ✅ Créé |
| `reports/bug-reports.md` | ✅ Existait déjà |
| `reports/deployment-report.md` | ✅ Existait déjà |
| `scripts/check-structure.mjs` | ✅ Modifié (4 fixes) |
| `skill/core-standard/SKILL.md` (workspace) | ✅ Modifié (bootstrap + invocation) |
| `~/.claude/skills/core-standard/SKILL.md` (déployé) | ✅ Synchronisé |
| `phase-2-technical-debt-to-v2.md` | ✅ Déduplication TD-23 à TD-38 |

---

## 8. État post-intervention

| Vérification | Statut |
|---|---|
| Skill déployé = workspace | ✅ |
| `skill/` validé par script | ✅ |
| `deployment-report.md` validé | ✅ |
| Version cible dette validée | ✅ |
| Dedup `--formalize` actif | ✅ |
| Bootstrap scaffold conforme §15 | ✅ |
| Dette sans doublons | ✅ |
| reports/ présent dans core-standard | ✅ |
