# structural-mapping — BLUEPRINT

> **Date:** 2026-04-12  
> **Origine:** Rationalized from `DISCUSSION.md` (Gemini conversation on organizational power mapping)  
> **Philosophie:** Le système génère ses propres indicateurs — il n'y a pas de métriques universelles

---

## Overview

`structural-mapping` est un **générateur de cartographie organisationnelle dynamique**. Il ne se contente pas d'appliquer des indicateurs prédéfinis — il **analyse le sujet et fait émerger la nomenclature adaptée** au domaine, à la culture et aux flux spécifiques de l'organisation observée.

---

## Core Concept: Nomenclature Dynamique

### Format: `ind-[groupe]-[nom5]`

| Segment | Règle | Exemple |
|---------|-------|---------|
| `ind` | Préfixe fixe — identifie une métrique | `ind` |
| `[groupe]` | Catégorie du domaine (3 lettres minuscules) | `pvr`, `ray`, `sem`, `fin`, `tec`, `hum` |
| `[nom5]` | Nom spécifique (5 lettres minuscules fixes) | `ildec`, `ifrme`, `ipcon`, `fdcom` |

### Principe Fondamental

**Les indicateurs ne sont pas prédéfinis.** Ils émergent de l'analyse du sujet selon 3 axes :

1. **Structure de pouvoir** — Qui décide ? Qui influence ?
2. **Flux de connaissances** — Qui sait quoi ? Qui transmet ?
3. **Rayonnement externe** — Qui porte la parole au-dehors ?

---

## Indicateurs de Référence (Cas Franc-Tireur)

Ces 4 indicateurs sont le **résultat** de l'analyse de Franc-Tireur, pas un template universel :

| ID | Groupe | Nom | Échelle | Définition |
|----|--------|-----|---------|------------|
| `ind-pvr-ildec` | `pvr` (pouvoir interne) | `ildec` (Liberté Décisionnelle) | 0–3 | Autonomie et impact décisionnel dans l'organisation |
| `ind-ray-ifrme` | `ray` (rayonnement externe) | `ifrme` (Force du Rayonnement Médiatique) | 0–3 | Influence médiatique externe — apparitions, rôle, puissance du groupe hébergeur |
| `ind-sem-ipcon` | `sem` (sémantique/connaissance) | `ipcon` (Privatisation des Connaissances) | 0–3 | Degré de rétention ou d'exclusivité de l'expertise |
| `ind-sem-fdcom` | `sem` (sémantique/connaissance) | `fdcom` (Facteur de Diffusion des Compétences) | 0–3 | Capacité à transmettre et horizontaliser le savoir-faire |

### Échelle de Référence

| Score | Signification |
|-------|---------------|
| 0 | Exécutant — aucune autonomie |
| 1 | Opérationnel — scope décisionnel limité |
| 2 | Stratégique — influence significative, pas d'autorité finale |
| 3 | Décideur — autonomie totale et impact |

---

## Génération Dynamique d'Indicateurs

### Processus en 3 Phases

```
┌─────────────────────────────────────────────────────────────┐
│ PHASE 1 : Analyse du Domaine                                │
│ - Quel est le contexte ? (média, tech, recherche, art...)   │
│ - Quels sont les enjeux de pouvoir spécifiques ?            │
│ - Quels types de flux existent ? (info, argent, compétence) │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 2 : Émergence des Groupes                             │
│ - Identifier 3-5 catégories pertinentes                     │
│ - Nommer chaque groupe (3 lettres)                          │
│ - Définir le périmètre sémantique de chaque groupe          │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 3 : Définition des Indicateurs                        │
│ - Pour chaque groupe, définir 1-3 indicateurs (5 lettres)   │
│ - Spécifier l'échelle et la méthode d'évaluation            │
│ - Documenter la sémantique exacte                           │
└─────────────────────────────────────────────────────────────┘
```

### Exemple: Startup Tech

Pour une startup de 15 personnes, les indicateurs pourraient être :

| ID | Définition |
|----|------------|
| `ind-fin-cashr` | Cash runway control — qui décide des dépenses ? |
| `ind-tech-archi` | Architecture ownership — qui valide les choix techniques ? |
| `ind-hum-growt` | Growth influence — qui pèse sur les recrutements ? |
| `ind-prod-vision` | Product vision — qui définit la roadmap ? |

### Exemple: Labo de Recherche

| ID | Définition |
|----|------------|
| `ind-acad-publ` | Publication lead — qui est premier auteur ? |
| `ind-fund-grant` | Grant acquisition — qui apporte les financements ? |
| `ind-ment-stud` | Student mentorship — qui forme les doctorants ? |
| `ind-collab-net` | Collaboration network — qui ouvre les portes externes ? |

---

## Outputs

| Output | Format | Usage |
|--------|--------|-------|
| **Matrice de synthèse** | Tableau Markdown | Vue compacte de tous les acteurs sur tous les indicateurs |
| **Arborescence** | `.md` hiérarchique | Structure de commandement avec valeurs d'indicateurs |
| **Mermaid** | Code block | Visualisation graphique modifiable |
| **JSON structuré** | `.json` | Export pour traitement programmatique |
| **Rapport d'analyse** | `.md` long | Narrative des dynamiques de pouvoir détectées |

---

## Rôle dans Meta-Cognition

Au sein de `core-ferule`, `structural-mapping` est **l'organe de perception des structures de pouvoir** :

| Capteur | Ce qu'il perçoit | Langage de sortie |
|---------|------------------|-------------------|
| `structural-mapping` | Structures de pouvoir, influence, flux de connaissance | `ind-[groupe]-[nom5]` |
| `matrix-topology` | Espace conceptuel, topologie de l'intention | LTM (Constellation/Amass/Quarks) |

`core-cognition` lit les deux formats via un rapport capteur unifié.

---

## Key Observations (Patterns Récurrents)

| Pattern | Signification |
|---------|---------------|
| **Inverse interne/externe** | Un acteur peut avoir fort pouvoir interne mais faible rayonnement (ou l'inverse) — ex: Barbier vs Fourest |
| **Knowledge hoarding** | `ipcon` élevé + `fdcom` bas = goulot d'étranglement cognitif |
| **Profil équilibré** | Scores similaires sur tous les indicateurs = généraliste |
| **Profil spécialisé** | Variations extrêmes = rôle de niche, potentiellement fragile |
| **Découplage titre/pouvoir** | Un "Directeur" peut avoir `ildec:1` si exécution-only — le titre ne fait pas le pouvoir |

---

## Current State

| Composant | Status |
|-----------|--------|
| Nomenclature `ind-[groupe]-[nom5]` | ✅ Définie |
| Cas de référence (Franc-Tireur) | ✅ Complet (5 personnes, 4 indicateurs) |
| Générateur dynamique d'indicateurs | ⏳ À implémenter |
| Moteur d'inférence LLM | ⏳ À implémenter |
| Skill Hermes | ✅ Scaffold créé |
| Dashboard de visualisation | ✅ Version initiale |

---

## Next: Core-Standard Link

**Lien à venir avec `core-standard`** — le système devra :
1. Respecter les contraintes de cohérence du core
2. Produire des rapports lisibles par `core-cognition`
3. S'intégrer dans la boucle de perception → cognition → action de la férule

---

## Pitfalls

- **Ne pas figer les indicateurs** — Franc-Tireur a produit `pvr/ray/sem`, mais un labo produirait `acad/fund/collab`
- **Ne pas confondre titre et pouvoir** — évaluer l'impact réel, pas l'intitulé du poste
- **Contexte avant tout** — les indicateurs sont relatifs à l'organisation, pas absolus
- **Dynamique temporelle** — les indicateurs peuvent shift pendant les crises ou réorganisations
