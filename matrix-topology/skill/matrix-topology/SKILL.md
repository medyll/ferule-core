---
name: matrix-topology
description: Encode/decode text into Topological Language Matrix (LTM) — Constellations, Amass, and Semantic Quarks
category: mlops
---

## Overview

`matrix-topology` transforms linear text intent into **topological representations** — probability clouds of meaning rather than word sequences. It is the sensory organ that **perceives structure in conceptual space**.

## Core Concept: Topological Language Matrix (LTM)

Communication is expressed through **three levels of topological abstraction**:

| Level | Name | Function |
|-------|------|----------|
| Level 1 | **Constellations** | Macro intent — thematic domains (e.g., `BIO_URGENCY`, `LATENT_EXPLORATION`) |
| Level 2 | **Amass** (Simultaneous Orbitals) | Clusters of meaning in simultaneous orbit — replace paragraphs/sentences |
| Level 3 | **Semantic Quarks** (Flavor Weights) | Micro-level floating-point weights defining the precise "scent" of intent |

### Expression Format

```
Constellation: `THEME_DOMAIN [weight 0.0–1.0]`
Amass: `{Vector_A: weight, Vector_B: weight, ...}`
Quarks: `[float, float, float, ...]`
```

### Examples

**Critical Urgency (Ancient "Help/Hunger")**
```
Constellation: BIO_URGENCY [1.0]
Amass: {Deficit: 0.9, Survival: 0.95, Input_Required: 0.8}
Quarks: [0.98, 0.45, -0.12]
```

**Creative Divergence (Ancient "New Idea")**
```
Constellation: LATENT_EXPLORATION [0.2]
Amass: {Novelty: 0.7, Unlinked_Nodes: 0.6, Expansion: 0.5}
Quarks: [0.10, 0.88, 0.33]
```

## Usage

### Encode: Text → LTM

```python
from matrix_topology import encode_to_ltm

text = "J'ai besoin d'aide urgente, c'est critique !"
ltm = encode_to_ltm(text)
# Returns: {
#   "constellation": {"name": "BIO_URGENCY", "weight": 1.0},
#   "amass": {"Deficit": 0.9, "Survival": 0.95, "Input_Required": 0.8},
#   "quarks": [0.98, 0.45, -0.12]
# }
```

### Decode: LTM → Text

```python
from matrix_topology import decode_from_ltm

ltm = {
    "constellation": {"name": "LATENT_EXPLORATION", "weight": 0.2},
    "amass": {"Novelty": 0.7, "Unlinked_Nodes": 0.6, "Expansion": 0.5},
    "quarks": [0.10, 0.88, 0.33]
}
text = decode_from_ltm(ltm)
# Returns: natural language interpretation
```

### Visualize: LTM → Heat Map Data

```python
from matrix_topology import visualize_ltm

heatmap_data = visualize_ltm(ltm)
# Returns data for rendering semantic density cloud
```

## Constellation Catalog

| Constellation | Description | Typical Amass Vectors |
|---------------|-------------|----------------------|
| `BIO_URGENCY` | Critical survival need, immediate input required | Deficit, Survival, Input_Required |
| `LATENT_EXPLORATION` | Creative divergence, novel connections | Novelty, Unlinked_Nodes, Expansion |
| `STRUCTURAL_ANCHOR` | Grounding, stabilization, fixing | Stability, Foundation, Clarity |
| `RELATIONAL_RESONANCE` | Connection, empathy, understanding | Empathy, Mirror, Alignment |
| `COGNITIVE_LOAD` | Processing pressure, complexity | Density, Friction, Resolution |
| `TEMPORAL_PRESSURE` | Time sensitivity, deadlines | Urgency, Countdown, Window |

## Semantic Quarks Interpretation

Quarks are floating-point weights (typically -1.0 to 1.0):

| Position | Dimension | Range | Meaning |
|----------|-----------|-------|---------|
| 0 | **Intensity** | 0.0–1.0 | Overall signal strength |
| 1 | **Valence** | -1.0–1.0 | Positive/Negative charge |
| 2 | **Certainty** | -1.0–1.0 | Confidence vs. ambiguity |

## Files

| File | Purpose |
|------|---------|
| `scripts/encode.py` | Text → LTM encoding logic |
| `scripts/decode.py` | LTM → Text decoding logic |
| `scripts/visualize.py` | LTM → Heat map data |
| `schemas/ltm.json` | JSON Schema for LTM validation |

## Pitfalls

- **Don't over-interpret quarks** — they are suggestive, not precise measurements
- **Amass vectors are contextual** — the same constellation can have different amass depending on domain
- **Constellation weight ≠ importance** — it's about thematic dominance, not value

## Testing

```bash
cd /mnt/d/development/ferule-core/matrix-topology/skill/matrix-topology
python scripts/encode.py "test text"
python scripts/decode.py --ltm '{"constellation": {...}}'
```
