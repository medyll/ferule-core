#!/usr/bin/env python3
"""
matrix-topology: Encode text into Topological Language Matrix (LTM)

Based on the LTM-2056 specification from DISCUSSION.md:
- Level 1: Constellation (thematic baseline)
- Level 2: Amass (simultaneous orbital clusters)
- Level 3: Semantic Quarks (flavor weights)
"""

import json
import sys
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime


# =============================================================================
# CONSTELLATION CATALOG (from DISCUSSION.md)
# =============================================================================

@dataclass
class ConstellationDef:
    name: str
    keywords: List[str]
    base_weight: float
    amass_vectors: List[str]
    description: str


CONSTELLATIONS = {
    "BIO_URGENCY": ConstellationDef(
        name="BIO_URGENCY",
        keywords=["urgent", "critique", "besoin", "aide", "vite", "immédiat", "urgence", 
                  "help", "need", "critical", "faim", "soif", "danger", "alerte"],
        base_weight=0.9,
        amass_vectors=["Deficit", "Survival", "Input_Required"],
        description="Critical homeostasis — ancient 'Help/Hunger'"
    ),
    "LATENT_EXPLORATION": ConstellationDef(
        name="LATENT_EXPLORATION",
        keywords=["idée", "nouveau", "créatif", "explorer", "découvrir", "curieux", 
                  "novel", "idea", "explore", "creative", "imagine", "rêve", "hypothèse"],
        base_weight=0.3,
        amass_vectors=["Novelty", "Unlinked_Nodes", "Expansion"],
        description="Creative divergence — ancient 'New Idea'"
    ),
    "STRUCTURAL_ANCHOR": ConstellationDef(
        name="STRUCTURAL_ANCHOR",
        keywords=["stable", "fixer", "base", "fondation", "ancrer", "structure", 
                  "ground", "fix", "stable", "anchor", "solide", "racine"],
        base_weight=0.5,
        amass_vectors=["Stability", "Foundation", "Clarity"],
        description="Grounding and stabilization"
    ),
    "RELATIONAL_RESONANCE": ConstellationDef(
        name="RELATIONAL_RESONANCE",
        keywords=["comprendre", "empathie", "lien", "relation", "connect", 
                  "empathy", "understand", "relation", "mirror", "amour", "ami"],
        base_weight=0.5,
        amass_vectors=["Empathy", "Mirror", "Alignment"],
        description="Connection and mutual understanding"
    ),
    "COGNITIVE_LOAD": ConstellationDef(
        name="COGNITIVE_LOAD",
        keywords=["complexe", "confus", "charge", "pression", "dense", 
                  "complex", "confused", "load", "pressure", "dense", "fatigue"],
        base_weight=0.6,
        amass_vectors=["Density", "Friction", "Resolution"],
        description="Processing pressure and complexity"
    ),
    "TEMPORAL_PRESSURE": ConstellationDef(
        name="TEMPORAL_PRESSURE",
        keywords=["délai", "temps", "deadline", "bientôt", "rapide", 
                  "time", "deadline", "soon", "fast", "pressure", "retard"],
        base_weight=0.7,
        amass_vectors=["Urgency", "Countdown", "Window"],
        description="Time sensitivity and temporal constraints"
    ),
    "OPERATIONAL_CRITICALITY": ConstellationDef(
        name="OPERATIONAL_CRITICALITY",
        keywords=["action", "opération", "exécuter", "lancer", "démarrer",
                  "action", "execute", "launch", "start", "critical", "priorité"],
        base_weight=0.8,
        amass_vectors=["Intervention", "Immediate", "Risk"],
        description="Functional priority — urgent assistance required"
    ),
    "ABSTRACT_HEURISTICS": ConstellationDef(
        name="ABSTRACT_HEURISTICS",
        keywords=["réfléchir", "penser", "concept", "théorie", "abstrait",
                  "think", "ponder", "concept", "theory", "abstract", "philosophie"],
        base_weight=0.2,
        amass_vectors=["Innovation", "Divergence", "Hypothesis"],
        description="Conceptual exploration — open inquiry"
    )
}


# =============================================================================
# SEMANTIC QUARKS DIMENSIONS
# =============================================================================

QUARK_DIMENSIONS = [
    ("Intensity", "Overall signal strength (0.0–1.0)"),
    ("Valence", "Positive/Negative charge (-1.0–1.0)"),
    ("Certainty", "Confidence vs. ambiguity (-1.0–1.0)")
]


# =============================================================================
# ENCODING ENGINE
# =============================================================================

def detect_constellation(text: str) -> Tuple[str, float]:
    """
    Detect the dominant constellation from text.
    Returns (constellation_name, weight)
    """
    text_lower = text.lower()
    scores = {}
    
    for const_name, const_def in CONSTELLATIONS.items():
        match_count = sum(1 for kw in const_def.keywords if kw in text_lower)
        if match_count > 0:
            # Weight = base + (matches * 0.05), capped at 1.0
            weight = min(1.0, const_def.base_weight + (match_count * 0.05))
            # Boost for exclamation marks (urgency signal)
            if "!" in text and "URG" in const_name:
                weight = min(1.0, weight + 0.1)
            scores[const_name] = weight
    
    if not scores:
        return "NEUTRAL", 0.1
    
    # Return highest scoring constellation
    best = max(scores.items(), key=lambda x: x[1])
    return best


def calculate_amass(constellation_name: str, text: str) -> Dict[str, float]:
    """
    Calculate amass vector weights based on constellation and text content.
    Amass vectors are perceived simultaneously, not sequentially.
    """
    const_def = CONSTELLATIONS.get(constellation_name)
    if not const_def:
        # Default vectors for unknown constellations
        vectors = ["Generic_A", "Generic_B", "Generic_C"]
    else:
        vectors = const_def.amass_vectors
    
    amass = {}
    text_lower = text.lower()
    
    for vector in vectors:
        base = 0.5
        
        # Adjust based on text characteristics
        if len(text) > 100:
            base += 0.15  # Longer text = more developed vectors
        elif len(text) > 50:
            base += 0.1
        
        # Question mark increases exploration vectors
        if "?" in text and vector in ["Novelty", "Unlinked_Nodes", "Hypothesis"]:
            base += 0.15
        
        # Exclamation increases intensity vectors
        if "!" in text and vector in ["Deficit", "Survival", "Immediate", "Urgency"]:
            base += 0.2
        
        # Negative words boost deficit/risk vectors
        negative_words = ["mal", "mauvais", "problème", "échec", "erreur", "bad", "wrong", "fail"]
        if any(w in text_lower for w in negative_words):
            if vector in ["Deficit", "Risk", "Friction"]:
                base += 0.15
        
        # Positive words boost expansion vectors
        positive_words = ["bien", "bon", "super", "oui", "yes", "good", "great", "succès"]
        if any(w in text_lower for w in positive_words):
            if vector in ["Expansion", "Innovation", "Alignment"]:
                base += 0.1
        
        amass[vector] = round(min(1.0, base), 2)
    
    return amass


def calculate_quarks(text: str) -> List[float]:
    """
    Calculate semantic quarks (3 floating-point weights).
    
    Quark dimensions:
    0: Intensity (0.0–1.0) — overall signal strength
    1: Valence (-1.0–1.0) — positive/negative charge
    2: Certainty (-1.0–1.0) — confidence vs. ambiguity
    """
    text_lower = text.lower()
    
    # === Quark 0: Intensity ===
    intensity = 0.5
    if len(text) > 100:
        intensity += 0.2
    if "!" in text:
        intensity += 0.2
    if text.isupper():
        intensity += 0.15  # ALL CAPS = high intensity
    urgency_words = ["urgent", "critique", "vite", "immédiat", "critical", "now"]
    if any(w in text_lower for w in urgency_words):
        intensity += 0.1
    intensity = round(min(1.0, intensity), 2)
    
    # === Quark 1: Valence ===
    positive = ["bon", "bien", "super", "oui", "yes", "good", "great", "amour", "love", 
                "joie", "heureux", "succès", "réussite"]
    negative = ["mal", "mauvais", "non", "no", "bad", "terrible", "haine", "hate", 
                "problème", "triste", "échec", "erreur"]
    
    pos_count = sum(1 for w in positive if w in text_lower)
    neg_count = sum(1 for w in negative if w in text_lower)
    
    if pos_count > neg_count:
        valence = 0.3 + (pos_count * 0.1)
    elif neg_count > pos_count:
        valence = -0.3 - (neg_count * 0.1)
    else:
        valence = 0.0
    valence = round(max(-1.0, min(1.0, valence)), 2)
    
    # === Quark 2: Certainty ===
    if "?" in text:
        certainty = -0.3
    elif any(w in text_lower for w in ["peut-être", "maybe", "possible", "incertain", "si"]):
        certainty = -0.2
    elif any(w in text_lower for w in ["certain", "sûr", "definitely", "absolu", "évident"]):
        certainty = 0.5
    elif any(w in text_lower for w in ["jamais", "toujours", "never", "always"]):
        certainty = 0.3  # Absolute statements
    else:
        certainty = 0.1
    certainty = round(max(-1.0, min(1.0, certainty)), 2)
    
    return [intensity, valence, certainty]


def encode_to_ltm(text: str) -> Dict:
    """
    Encode text into full LTM format.
    
    Returns:
    {
        "constellation": {"name": str, "weight": float},
        "amass": {vector: weight, ...},
        "quarks": [intensity, valence, certainty]
    }
    """
    constellation_name, weight = detect_constellation(text)
    amass = calculate_amass(constellation_name, text)
    quarks = calculate_quarks(text)
    
    return {
        "constellation": {
            "name": constellation_name,
            "weight": round(weight, 2)
        },
        "amass": amass,
        "quarks": quarks,
        "metadata": {
            "encoded_at": datetime.now().isoformat(),
            "text_length": len(text),
            "ltm_version": "2056.1"
        }
    }


def decode_from_ltm(ltm: Dict) -> str:
    """
    Decode LTM back to natural language description.
    This is for human readability, not for re-transmission.
    """
    constellation = ltm.get("constellation", {})
    amass = ltm.get("amass", {})
    quarks = ltm.get("quarks", [0, 0, 0])
    
    name = constellation.get("name", "UNKNOWN")
    weight = constellation.get("weight", 0)
    
    intensity = quarks[0] if len(quarks) > 0 else 0
    valence = quarks[1] if len(quarks) > 1 else 0
    certainty = quarks[2] if len(quarks) > 2 else 0
    
    valence_str = "positive" if valence > 0.2 else "negative" if valence < -0.2 else "neutral"
    certainty_str = "certain" if certainty > 0.2 else "ambiguous" if certainty < -0.2 else "neutral"
    density_str = "dense" if intensity > 0.7 else "gaseous" if intensity < 0.3 else "moderate"
    
    amass_summary = ", ".join([f"{k}: {v}" for k, v in sorted(amass.items(), key=lambda x: -x[1])])
    
    # Get constellation description
    const_def = CONSTELLATIONS.get(name)
    description = const_def.description if const_def else "Unknown constellation"
    
    return (
        f"🌌 Constellation: {name} (weight: {weight})\n"
        f"   Description: {description}\n"
        f"   Density: {density_str} (intensity: {intensity})\n"
        f"\n"
        f"☄️ Amass Vectors: {amass_summary}\n"
        f"\n"
        f"⚛️ Semantic Quarks:\n"
        f"   - Intensity: {intensity} ({density_str})\n"
        f"   - Valence: {valence} ({valence_str})\n"
        f"   - Certainty: {certainty} ({certainty_str})"
    )


def calculate_heat_map(ltm: Dict) -> Dict:
    """
    Generate heat map data for visualization.
    
    Heat Map Architecture (from DISCUSSION.md):
    - Luminosity = node brightness = weight/importance
    - Proximity = spatial distance = logical tension/relation
    - Flicker Rate = frequency = temporal urgency
    """
    constellation = ltm.get("constellation", {})
    amass = ltm.get("amass", {})
    quarks = ltm.get("quarks", [0.5, 0, 0.1])
    
    # Luminosity = constellation weight * intensity
    luminosity = constellation.get("weight", 0) * quarks[0]
    
    # Proximity = inverse of amass variance (tight clusters = high proximity)
    amass_values = list(amass.values())
    if len(amass_values) > 1:
        mean = sum(amass_values) / len(amass_values)
        variance = sum((v - mean) ** 2 for v in amass_values) / len(amass_values)
        proximity = 1.0 / (1.0 + variance)
    else:
        proximity = 0.5
    
    # Flicker rate = based on temporal/urgency indicators
    flicker = 0.3  # Base rate
    if "TEMPORAL" in constellation.get("name", "") or "URGENCY" in constellation.get("name", ""):
        flicker = 0.7 + (quarks[0] * 0.3)  # Higher flicker for urgent content
    elif "EXPLORATION" in constellation.get("name", "") or "ABSTRACT" in constellation.get("name", ""):
        flicker = 0.1 + (quarks[0] * 0.2)  # Slow flicker for exploratory content
    
    # Density = overall mass of the cloud
    density = (constellation.get("weight", 0) + quarks[0]) / 2
    
    return {
        "luminosity": round(luminosity, 2),
        "proximity": round(proximity, 2),
        "flicker_rate": round(flicker, 2),
        "density": round(density, 2),
        "nodes": [{"name": k, "weight": v, "luminosity": round(v * quarks[0], 2)} 
                  for k, v in sorted(amass.items(), key=lambda x: -x[1])]
    }


def check_coherence(ltm: Dict) -> Tuple[bool, List[str]]:
    """
    Check LTM coherence based on the Anti-Ambiguity Shield rule.
    Any weight conflict > 0.15 within a cloud triggers an alert.
    """
    alerts = []
    amass = ltm.get("amass", {})
    values = list(amass.values())
    
    if len(values) > 1:
        max_val = max(values)
        min_val = min(values)
        conflict = max_val - min_val
        
        if conflict > 0.6:  # High internal tension
            alerts.append(f"⚠️ HIGH_TENSION_ALERT: Internal conflict = {conflict:.2f} (> 0.6)")
        elif conflict > 0.4:
            alerts.append(f"⚡ MODERATE_TENSION: Internal conflict = {conflict:.2f}")
    
    # Check quark consistency
    quarks = ltm.get("quarks", [])
    if len(quarks) >= 2:
        # High intensity + negative valence = potential distress signal
        if quarks[0] > 0.8 and quarks[1] < -0.5:
            alerts.append("🚨 DISTRESS_SIGNAL: High intensity + negative valence")
    
    return len(alerts) == 0, alerts


# =============================================================================
# VISUALIZATION: ASCII HEAT MAP
# =============================================================================

def render_ascii_heat_map(ltm: Dict) -> str:
    """
    Render LTM as ASCII heat map for terminal display.
    """
    heat = calculate_heat_map(ltm)
    constellation = ltm.get("constellation", {})
    
    # Character density scale
    density_chars = " ░▒▓█"
    
    # Calculate overall density level (0-4)
    density_level = int(heat["density"] * 4)
    density_char = density_chars[min(density_level, len(density_chars) - 1)]
    
    lines = [
        "╔═══════════════════════════════════════════════════════════╗",
        f"║  LTM HEAT MAP — {constellation.get('name', 'UNKNOWN'):<42} ║",
        "╠═══════════════════════════════════════════════════════════╣",
        f"║  Density: {density_char * 20}  ({heat['density']:.2f}){' ' * 25}║",
        f"║  Luminosity: {'●' * int(heat['luminosity'] * 20)}{' ' * (20 - int(heat['luminosity'] * 20))}  ({heat['luminosity']:.2f}){' ' * 17}║",
        f"║  Proximity: {'◉' * int(heat['proximity'] * 20)}{' ' * (20 - int(heat['proximity'] * 20))}  ({heat['proximity']:.2f}){' ' * 17}║",
        f"║  Flicker: ~{heat['flicker_rate']:.2f} Hz{' ' * 44}║",
        "╠═══════════════════════════════════════════════════════════╣",
        "║  AMASS NODES (sorted by weight):                          ║"
    ]
    
    for node in heat["nodes"]:
        node_density = int(node["weight"] * 10)
        node_bar = density_chars[0] * (10 - node_density) + density_chars[-1] * node_density
        lines.append(f"║    {node['name']:<15} [{node_bar}] {node['weight']:.2f}{' ' * 10}║")
    
    # Coherence check
    is_coherent, alerts = check_coherence(ltm)
    lines.append("╠═══════════════════════════════════════════════════════════╣")
    if is_coherent:
        lines.append("║  ✅ COHERENCE CHECK: PASSED                                   ║")
    else:
        for alert in alerts[:2]:  # Show max 2 alerts
            lines.append(f"║  {alert:<58} ║")
    
    lines.append("╚═══════════════════════════════════════════════════════════╝")
    
    return "\n".join(lines)


# =============================================================================
# CLI INTERFACE
# =============================================================================

def main():
    if len(sys.argv) < 2:
        print("matrix-topology: Encode text into Topological Language Matrix (LTM)")
        print()
        print("Usage: python encode.py <text>")
        print("       python encode.py --demo")
        print("       python encode.py --constellations")
        print()
        print("Examples:")
        print('  python encode.py "J\'ai besoin d\'aide urgente !"')
        print('  python encode.py "Je réfléchis à une nouvelle idée créative"')
        sys.exit(0)
    
    if sys.argv[1] == "--demo":
        print("=" * 70)
        print("MATRIX TOPOLOGY — LTM Encoding Demo")
        print("=" * 70)
        print()
        
        demo_texts = [
            "J'ai besoin d'aide urgente, c'est critique !",
            "Je réfléchis à une nouvelle idée créative pour le projet",
            "La structure est stable et bien fondée",
            "Je me sens connecté et compris par mon équipe"
        ]
        
        for text in demo_texts:
            print(f"INPUT: \"{text}\"")
            print("-" * 70)
            ltm = encode_to_ltm(text)
            print(render_ascii_heat_map(ltm))
            print()
            print(decode_from_ltm(ltm))
            print()
            print("=" * 70)
            print()
        
        sys.exit(0)
    
    if sys.argv[1] == "--constellations":
        print("Available Constellations:")
        print("-" * 50)
        for name, const in CONSTELLATIONS.items():
            print(f"\n{name}")
            print(f"  Description: {const.description}")
            print(f"  Base Weight: {const.base_weight}")
            print(f"  Amass Vectors: {', '.join(const.amass_vectors)}")
            print(f"  Keywords: {', '.join(const.keywords[:8])}...")
        sys.exit(0)
    
    # Encode the input text
    text = " ".join(sys.argv[1:])
    
    print(f"INPUT: \"{text}\"")
    print("=" * 70)
    
    ltm = encode_to_ltm(text)
    
    print()
    print("JSON OUTPUT:")
    print(json.dumps(ltm, indent=2))
    print()
    
    print("HEAT MAP VISUALIZATION:")
    print(render_ascii_heat_map(ltm))
    print()
    
    print("DECODED:")
    print(decode_from_ltm(ltm))


if __name__ == "__main__":
    main()
