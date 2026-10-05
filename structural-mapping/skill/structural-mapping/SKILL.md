---
name: structural-mapping
description: Mappeur dynamique de structures organisationnelles — génère ses propres indicateurs `ind-[groupe]-[nom5]` adaptés au sujet
category: mlops
---

## Overview

`structural-mapping` est un **générateur de cartographie organisationnelle dynamique**. Il ne se contente pas d'appliquer des indicateurs prédéfinis — il **analyse le sujet et fait émerger la nomenclature adaptée** au domaine, à la culture et aux flux spécifiques de l'organisation observée.

## Core Concept: Nomenclature `ind-[groupe]-[nom5]`

| Segment | Règle | Exemple |
|---------|-------|---------|
| `ind` | Préfixe fixe — identifie une métrique | `ind` |
| `[groupe]` | Catégorie du domaine (3 lettres minuscules) | `pvr`, `ray`, `sem`, `fin`, `tec` |
| `[nom5]` | Nom spécifique (5 lettres minuscules fixes) | `ildec`, `ifrme`, `ipcon`, `fdcom` |

### Principe Fondamental

**Les indicateurs ne sont pas prédéfinis.** Ils émergent de l'analyse du sujet selon 3 axes :

1. **Structure de pouvoir** — Qui décide ? Qui influence ?
2. **Flux de connaissances** — Qui sait quoi ? Qui transmet ?
3. **Rayonnement externe** — Qui porte la parole au-dehors ?

## Usage

### Mode 1 : Démarrage Rapide (Template par Domaine)

```python
from structural_mapping import create_structure, generate_indicators_for_domain

# Détection automatique du domaine
org = create_structure("Ma Startup", context="Startup tech de 15 personnes — SaaS B2B")

# Génération des indicateurs adaptés au domaine tech
indicators = generate_indicators_for_domain("tech_startup")
for ind in indicators:
    org.register_indicator(ind.group, ind.name, ind.scale, ind.definition)

# Ajout des personnes
org.add_person("Alice Dupont", "CEO & Co-founder")
org.add_person("Bob Martin", "CTO & Co-founder", reports_to=["Alice Dupont"])

# Assignation des valeurs
org.people["Alice Dupont"].indicators = {
    "ind-fin-cashr": 3,
    "ind-prod-visio": 3,
    "ind-hum-growt": 2
}
```

### Mode 2 : Génération Dynamique (Recommandé)

```python
from structural_mapping import generate_indicators_from_context, create_structure

context = "Startup tech de 15 personnes — SaaS B2B, enjeux de cash runway et recrutement"
subject = "Structure de décision technique et produit"

# Génération automatique des indicateurs adaptés
indicators = generate_indicators_from_context(context, subject)

org = create_structure("Ma Startup", context=context)
for ind in indicators:
    org.register_indicator(ind.group, ind.name, ind.scale, ind.definition)
```

### Mode 3 : Manuel (Contrôle Total)

```python
from structural_mapping import create_structure

org = create_structure("Mon Organisation", context="...")

# Enregistrement manuel des indicateurs
org.register_indicator("pvr", "ildec", "0-3", "Liberté Décisionnelle — autonomie et impact")
org.register_indicator("ray", "ifrme", "0-3", "Force du Rayonnement — influence externe")

# Ajout des personnes avec indicateurs
org.add_person("Nom", "Rôle", reports_to=["Manager"], external_entities=["Entreprise X"])
org.people["Nom"].set_indicator("ind-pvr-ildec", 3)
```

### Génération des Outputs

```python
from structural_mapping import (
    generate_matrix,
    generate_tree,
    generate_mermaid,
    export_json,
    generate_analysis_report
)

# Matrice de synthèse
print(generate_matrix(org))

# Arborescence hiérarchique
print(generate_tree(org))

# Diagramme Mermaid (visualisable dans GitHub, Notion, etc.)
print(generate_mermaid(org))

# Export JSON pour traitement programmatique
json_data = export_json(org)

# Rapport d'analyse narrative
report = generate_analysis_report(org)
```

## Domain Templates

Le module inclut des templates pré-définis pour différents domaines :

| Domaine | Groupes | Indicateurs Exemples |
|---------|---------|---------------------|
| **media** | `pvr`, `ray`, `sem` | `ildec`, `ifrme`, `ipcon`, `fdcom` |
| **tech_startup** | `fin`, `tec`, `hum`, `prd` | `cashr`, `archi`, `growt`, `visio` |
| **research_lab** | `acad`, `fund`, `ment`, `coll` | `publi`, `grant`, `studt`, `netwk` |
| **art_collective** | `creat`, `prod`, `diff`, `fin` | `artis`, `logis`, `visib`, `mecen` |

## Référence: Cas Caféine

Molécule (1,3,7-triméthylxanthine, PubChem CID 2519). Les acteurs sont des groupes structuraux, pas des personnes. 9 acteurs, 5 indicateurs :

| Groupe | ind-rea-sitac | ind-ext-hbond | ind-ele-local | ind-ele-delox | ind-met-labil |
|--------|:---:|:---:|:---:|:---:|:---:|
| Noyau xanthine | 3 | 1 | 0 | 3 | 0 |
| Cycle imidazole | 2 | 2 | 1 | 3 | 0 |
| Cycle pyrimidinedione | 2 | 2 | 1 | 3 | 0 |
| N9 | 2 | 3 | 2 | 1 | 0 |
| C6=O | 2 | 2 | 1 | 2 | 0 |
| C2=O | 1 | 2 | 1 | 2 | 0 |
| N1-CH3 | 1 | 0 | 0 | 2 | 2 |
| N3-CH3 | 1 | 0 | 0 | 2 | 3 |
| N7-CH3 | 1 | 0 | 0 | 2 | 1 |

**Observation clé:** Découplage pouvoir/rayonnement — le noyau xanthine « décide » (sitac:3, forme reconnue par les récepteurs de l'adénosine) sans interagir lui-même (hbond:1) ; N9 porte la parole vers l'extérieur (hbond:3).

**Vérité de terrain:** les scores sont qualitatifs et doivent être confrontés aux descripteurs calculés (PubChem, RDKit). C'est ce qui rend le cas testable.

## Échelle de Référence

| Score | Signification |
|-------|---------------|
| 0 | Exécutant — aucune autonomie |
| 1 | Opérationnel — scope décisionnel limité |
| 2 | Stratégique — influence significative, pas d'autorité finale |
| 3 | Décideur — autonomie totale et impact |

## Files

| File | Purpose |
|------|---------|
| `scripts/matrix.py` | Moteur principal — génération dynamique, outputs |
| `schemas/structure.json` | JSON Schema pour validation |
| `sources/DISCUSSION.md` | Conversation originelle (Gemini) — source de vérité |

## Patterns Récurrents (Observations)

| Pattern | Signification |
|---------|---------------|
| **Inverse interne/externe** | Fort pouvoir interne ≠ fort rayonnement externe (et vice versa) |
| **Knowledge hoarding** | `ipcon` élevé + `fdcom` bas = goulot d'étranglement cognitif |
| **Profil équilibré** | Scores similaires = généraliste |
| **Profil spécialisé** | Variations extrêmes = rôle de niche, potentiellement fragile |
| **Découplage titre/pouvoir** | Un "Directeur" peut avoir `ildec:1` si exécution-only |

## Pitfalls

- **Ne pas figer les indicateurs** — la caféine a produit `rea/ele/ext/met`, mais un labo produirait `acad/fund/collab`
- **Ne pas confondre titre et pouvoir** — évaluer l'impact réel, pas l'intitulé du poste
- **Contexte avant tout** — les indicateurs sont relatifs à l'organisation, pas absolus
- **Dynamique temporelle** — les indicateurs peuvent shift pendant les crises ou réorganisations

## Testing

```bash
cd /mnt/d/development/ferule-core/structural-mapping/skill/structural-mapping

# Demo Caféine
python3 scripts/matrix.py --demo

# Vérifier la détection de domaine
python3 -c "
from scripts.matrix import detect_domain, generate_indicators_from_context
print(detect_domain('Startup tech SaaS'))
print(generate_indicators_from_context('tech', 'CTO, developers, product roadmap'))
"
```

## Next: Core-Standard Link

**Lien à venir avec `core-standard`** — le système devra :
1. Respecter les contraintes de cohérence du core
2. Produire des rapports lisibles par `core-cognition`
3. S'intégrer dans la boucle de perception → cognition → action de la férule
