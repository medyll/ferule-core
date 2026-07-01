# 🔮 Ferule-Core

> **point d'entrée → [adaptabilité] → point de sortie**

> **Espace de recherche pour une férule autonome**

Deux langages formels pour exprimer la cognition et la structure organisationnelle, avec visualisation 3D interactive.

---

## 🎯 Nouveautés (v2)

### ✨ Moteur LLM pour Indicateurs Dynamiques
- **Génération automatique** d'indicateurs adaptés au contexte
- **9 domaines supportés** : media, tech_startup, research_lab, art_collective, healthcare, education, nonprofit, manufacturing, finance
- **Nomenclature standardisée** : `ind-[group]-[name5]`
- **Mock LLM intégré** pour testing sans API

### 🌌 Visualisation 3D des Nuages Sémantiques
- **Three.js** pour rendu 3D interactif
- **Constellation sphère** avec effet glow
- **Particules en orbite** pour les vecteurs Amass
- **Anneaux Quarks** animés
- **Contrôles** : rotation, zoom, pan

---

## 🗺️ Architecture

```
ferule-core/
├── README.md                       # Ce fichier
├── test.py                         # Suite de tests (7 tests ✅)
│
├── dashboard.html                  # Interface 2D complète
├── dashboard-3d.html               # Visualisation 3D avec Three.js ✨
│
├── matrix-topology/                # Langage Topologique Matriciel (LTM)
│   ├── BLUEPRINT.md
│   ├── sources/
│   │   └── DISCUSSION.md           # Conversation originelle
│   └── skill/matrix-topology/
│       ├── SKILL.md
│       ├── scripts/
│       │   └── encode.py           # Texte → LTM (19 KB)
│       └── schemas/ltm.json
│
└── structural-mapping/             # Cartographie dynamique
    ├── BLUEPRINT.md
    ├── sources/
    │   └── DISCUSSION.md
    └── skill/structural-mapping/
        ├── SKILL.md
        ├── scripts/
        │   ├── matrix.py           # Génération matrices
        │   └── llm_indicators.py   # LLM indicators ✨
        └── schemas/structure.json
```

---

## 🌌 Matrix Topology

Traduit l'intention textuelle en **représentations topologiques 3D**.

### Constellations Disponibles

| Constellation | Déclencheurs | Densité |
|--------------|--------------|---------|
| `BIO_URGENCY` | urgent, critique, besoin, aide | Dense |
| `LATENT_EXPLORATION` | idée, nouveau, créatif | Gazeuse |
| `STRUCTURAL_ANCHOR` | stable, base, fondation | Modérée |
| `RELATIONAL_RESONANCE` | comprendre, empathie, lien | Modérée |
| `COGNITIVE_LOAD` | complexe, confus, pression | Dense |
| `TEMPORAL_PRESSURE` | délai, temps, deadline | Dense |
| `OPERATIONAL_CRITICALITY` | action, exécuter, lancer | Dense |
| `ABSTRACT_HEURISTICS` | réfléchir, concept, théorie | Gazeuse |

### Usage

```bash
# Demo complète
python3 matrix-topology/skill/matrix-topology/scripts/encode.py --demo

# Encoder un texte
python3 matrix-topology/skill/matrix-topology/scripts/encode.py "J'ai besoin d'aide urgente !"

# Lister les constellations
python3 matrix-topology/skill/matrix-topology/scripts/encode.py --constellations
```

### Output LTM

```json
{
  "constellation": { "name": "BIO_URGENCY", "weight": 1.0 },
  "amass": { "Deficit": 0.7, "Survival": 0.7, "Input_Required": 0.5 },
  "quarks": [0.8, 0.0, 0.1]
}
```

---

## 🏛️ Structural Mapping

Génère dynamiquement des **indicateurs de pouvoir** adaptés au contexte.

### Nomenclature : `ind-[group]-[name5]`

| Segment | Règle | Exemple |
|---------|-------|---------|
| `ind` | Préfixe fixe | `ind` |
| `[group]` | 3 lettres (catégorie) | `pvr`, `fin`, `tec` |
| `[name5]` | 5 lettres (nom) | `ildec`, `cashr`, `archi` |

### Domaines Supportés

| Domaine | Indicateurs Exemples |
|---------|---------------------|
| **media** | `ind-pvr-ildec`, `ind-ray-ifrme`, `ind-sem-ipcon`, `ind-sem-fdcom` |
| **tech_startup** | `ind-fin-cashr`, `ind-tec-archi`, `ind-prd-visio`, `ind-hum-growt` |
| **research_lab** | `ind-aca-publi`, `ind-fin-grant`, `ind-men-studt`, `ind-col-netwk` |
| **art_collective** | `ind-creat-artis`, `ind-prod-logis`, `ind-diff-visib`, `ind-fin-mecen` |
| **healthcare** | `ind-med-diagp`, `ind-adm-budgt`, `ind-tea-super`, `ind-res-proto` |
| **education** | `ind-ped-curri`, `ind-adm-admin`, `ind-men-stude`, `ind-res-resea` |
| **nonprofit** | `ind-mis-align`, `ind-fun-fundr`, `ind-vol-volun`, `ind-imp-outcm` |
| **manufacturing** | `ind-ops-produ`, `ind-qua-quali`, `ind-sup-chain`, `ind-saf-hsenv` |
| **finance** | `ind-inv-alloc`, `ind-ris-mlimit`, `ind-cli-relat`, `ind-com-repor` |

### Usage

```bash
# Demo LLM indicators
python3 structural-mapping/skill/structural-mapping/scripts/llm_indicators.py --demo

# Générer pour un contexte
python3 structural-mapping/skill/structural-mapping/scripts/llm_indicators.py "Startup tech de 15 personnes"

# Lister les domaines
python3 structural-mapping/skill/structural-mapping/scripts/llm_indicators.py --domains

# Demo Franc-Tireur (matrix.py)
python3 structural-mapping/skill/structural-mapping/scripts/matrix.py --demo
```

---

## 🎛️ Dashboards

### Dashboard 2D (`dashboard.html`)

Interface complète avec :
- Encodage LTM avec visualisation heat map
- Barres de progression pour Quarks
- Matrices interactives
- Export JSON

**Ouverture :**
```bash
# Linux/WSL
xdg-open /mnt/d/development/ferule-core/dashboard.html

# Windows (depuis WSL)
explorer.exe /mnt/d/development/ferule-core/dashboard.html
```

### Dashboard 3D (`dashboard-3d.html`) ✨

Visualisation 3D interactive avec Three.js :
- **Sphère de constellation** avec glow
- **Particules en orbite** (vecteurs Amass)
- **Anneaux Quarks** animés
- **Contrôles souris** : drag (rotate), scroll (zoom), right-drag (pan)
- **Stats en temps réel** : density, luminosity, proximity, flicker rate

**Ouverture :**
```bash
# Linux/WSL
xdg-open /mnt/d/development/ferule-core/dashboard-3d.html

# Windows (depuis WSL)
explorer.exe /mnt/d/development/ferule-core/dashboard-3d.html
```

---

## 🧪 Testing

```bash
# Suite complète (7 tests)
python3 test.py
```

**Résultats attendus :**
```
🧪 TEST: Matrix Topology — Demo Mode        ✅
🧪 TEST: Matrix Topology — Single Text       ✅
🧪 TEST: Matrix Topology — List Constellations ✅
🧪 TEST: Structural Mapping — Franc-Tireur   ✅
🧪 TEST: LLM Indicators — Demo Mode          ✅
🧪 TEST: Dashboard HTML                      ✅
🧪 TEST: Dashboard 3D HTML                   ✅

🎉 ALL TESTS PASSED! (7/7)
```

---

## 🚀 Roadmap

### Phase 1 : Skills Opérationnels ✅
- [x] matrix-topology avec encode.py
- [x] structural-mapping avec matrix.py
- [x] LLM indicator generator (llm_indicators.py)
- [x] JSON Schemas de validation
- [x] Dashboards 2D et 3D

### Phase 2 : Language Protocol 🔄
- [ ] API unifiée Python pour les deux langages
- [x] Détection de domaine automatique
- [ ] Intégration LLM réel (OpenAI, Anthropic)
- [ ] Validation croisée inter-LLM

### Phase 3 : Dashboard Avancé 🔄
- [x] Interface 2D complète
- [x] Visualisation 3D avec Three.js
- [ ] Export Mermaid dynamique
- [ ] Historique des transformations
- [ ] Visualisation 3D des structures organisationnelles

### Phase 4 : Intégration Ferule ⏳
- [ ] Adapter outputs pour core-cognition
- [ ] Lien avec core-standard
- [ ] Tests d'intégration complets

---

## 📚 Sources

- **matrix-topology** : `matrix-topology/sources/DISCUSSION.md` — Conversation Gemini sur LTM
- **structural-mapping** : `structural-mapping/sources/DISCUSSION.md` — Conversation Franc-Tireur

---

## 📝 Notes Techniques

### Heat Map Architecture (LTM)

| Métrique | Calcul | Signification |
|----------|--------|---------------|
| **Luminosity** | `constellation.weight × intensity` | Importance/priorité |
| **Proximity** | `1 / (1 + variance(amass))` | Cohérence interne |
| **Flicker Rate** | Basé sur urgence | Fréquence temporelle |
| **Density** | Moyenne luminosity/proximity | Gravité du message |

### Coherence Check

- **Conflict > 0.6** : HIGH_TENSION_ALERT
- **Conflict > 0.4** : MODERATE_TENSION
- **Conflict < 0.4** : COHERENCE_OK

---

## 🎮 Quick Start

```bash
cd /mnt/d/development/ferule-core

# 1. Tester Matrix Topology
python3 matrix-topology/skill/matrix-topology/scripts/encode.py "J'ai une idée créative !"

# 2. Tester Structural Mapping LLM
python3 structural-mapping/skill/structural-mapping/scripts/llm_indicators.py "Labo de recherche en IA"

# 3. Lancer la suite de tests
python3 test.py

# 4. Ouvrir le dashboard 3D
explorer.exe dashboard-3d.html
```

---

**Statut:** Phase 1 ✅ — Phase 2 🔄 — Dashboards ✅ — 3D Visualization ✅
