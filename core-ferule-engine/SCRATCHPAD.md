# core-ferule-engine — SCRATCHPAD

> **Date:** 2026-04-17
> **Status:** Conceptuel → À rationaliser en BLUEPRINT
> **Author:** OpenClaw Session

---

## Rôle Prévut

**core-ferule-engine** est le **moteur métier** de la Férule.

### Responsabilités

1. **Routing & Interprétation** — Point d'entrée unique pour les requêtes vers la Férule
2. **Exécution de Règles** — Moteur Python (`run_engine.py`)
3. **Modèles de Données** — Structures partagées (`core/models/`)
4. **Workflows** — Enchaînements d'actions (`core/workflows/`)
5. **Interfaces** — Points de connexion externes (`core/interfaces/`)

---

## Architecture Actuelle

```
core-ferule-engine/
├── run_engine.py              ← Moteur Python (à documenter)
├── requirements.txt           ← Dépendances Python
├── core/
│   ├── rules/                 ← Règles métier (à documenter)
│   ├── models/                ← Modèles de données (à documenter)
│   └── workflows/             ← Workflows (à documenter)
├── interfaces/                ← Interfaces externes (à documenter)
├── nexus-protocol/            ← Protocole de communication
├── scripts/                   ← Scripts utilitaires
├── skill/
│   └── ferule-core/           ← Skill d'entrée (À CRÉER)
│       └── SKILL.md
└── SCRATCHPAD.md              ← Ce fichier
```

---

## À Faire (Technical Debt)

### 1. **Skill d'Entrée** (PRIORITAIRE)

Créer `skill/ferule-core/SKILL.md` :
- Point d'entrée unique pour la Férule
- Écoute, interprète, route vers :
  - `core-squad` → Missions, Place de Grève
  - `core-standard` → Normes, taxonomie
  - `watchdog` → Health checks

### 2. **Documenter le Moteur Python**

`run_engine.py` :
- Quel est son rôle exact ?
- Comment est-il déclenché ?
- Quelles règles exécute-t-il ?

### 3. **Documenter `core/`**

Chaque sous-dossier :
- `core/rules/` → Quelles règles ? Format ?
- `core/models/` → Quels modèles ? Schéma ?
- `core/workflows/` → Quels workflows ? Déclencheurs ?

### 4. **Documenter `interfaces/`**

- Quelles interfaces ?
- Vers quels systèmes externes ?

---

## Lien avec core-standard

**core-standard** est la **norme** → `check-structure.mjs`, commands, documentation.

**core-ferule-engine** est le **moteur** → Exécution, routing, règles métier.

**Séparation :**
- core-standard → "Quoi" (normes)
- core-ferule-engine → "Comment" (exécution)

---

## Bootstrap Prévu

Une fois ce SCRATCHPAD rationalisé en BLUEPRINT :

```
node core-standard/scripts/check-structure.mjs --bootstrap
```

Générera :
- `USER-NOTES.md` (dérivé du BLUEPRINT)
- `skill/ferule-core/SKILL.md` (auto-généré)
- `development/v1-core-ferule-engine/` (scaffold complet)
- Phase files (si debt identifiée)

---

## Notes de Session (2026-04-17)

**Décisions :**
- `core-ferule-engine` garde son nom (pas de renommage)
- Skill d'entrée sera dans `core-ferule-engine/skill/ferule-core/`
- `core-cognition/` et `embeddings/` sont gardés (conceptuel mais légitime)
- `incidents/` est légitime (archive killing-joe.md)
- `heart-flow/` gardé (non branché)
- `watchdog/alerts/` → à supprimer

**Prochaine action :**
1. Rationaliser ce SCRATCHPAD → BLUEPRINT
2. Lancer core-bootstrap
3. Tester le flux skill/ferule-core → routing

---

*TODO: Documenter run_engine.py, core/rules/, core/models/, core/workflows/, interfaces/*
