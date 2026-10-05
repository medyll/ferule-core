#!/usr/bin/env python3
"""
structural-mapping: Dynamic organizational power structure mapper

This module generates indicators dynamically based on the subject context.
The nomenclature follows: ind-[group]-[name5]
"""

import json
import re
import sys
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field, asdict
from datetime import datetime


# =============================================================================
# DATA STRUCTURES
# =============================================================================

@dataclass
class Indicator:
    """Represents a normalized indicator (ind-[group]-[name5])."""
    group: str       # 3 letters
    name: str        # 5 letters
    scale: str       # e.g., "0-3"
    definition: str  # Human-readable definition
    
    @property
    def id(self) -> str:
        return f"ind-{self.group}-{self.name}"
    
    def validate(self) -> Tuple[bool, List[str]]:
        """Validate indicator naming conventions."""
        errors = []
        if len(self.group) != 3:
            errors.append(f"Group must be 3 letters, got '{self.group}'")
        if len(self.name) != 5:
            errors.append(f"Name must be 5 letters, got '{self.name}'")
        if not self.group.islower():
            errors.append(f"Group must be lowercase: '{self.group}'")
        if not self.name.islower():
            errors.append(f"Name must be lowercase: '{self.name}'")
        return len(errors) == 0, errors


@dataclass
class Person:
    """Represents a person/entity in the organization."""
    name: str
    role: str
    indicators: Dict[str, int] = field(default_factory=dict)
    links_to: List[str] = field(default_factory=list)
    external_entities: List[str] = field(default_factory=list)
    notes: str = ""
    
    def set_indicator(self, indicator_id: str, value: int):
        self.indicators[indicator_id] = value
    
    def get_indicator(self, indicator_id: str) -> Optional[int]:
        return self.indicators.get(indicator_id)


@dataclass
class Organization:
    """Represents an organization structure with dynamically generated indicators."""
    name: str
    context: str  # Domain/context description
    people: Dict[str, Person] = field(default_factory=dict)
    indicators: Dict[str, Indicator] = field(default_factory=dict)
    analysis_notes: str = ""
    
    def add_person(self, name: str, role: str, 
                   reports_to: Optional[List[str]] = None,
                   external_entities: Optional[List[str]] = None):
        person = Person(name=name, role=role)
        if reports_to:
            person.links_to = reports_to
        if external_entities:
            person.external_entities = external_entities
        self.people[name] = person
    
    def register_indicator(self, group: str, name: str, scale: str, definition: str) -> Indicator:
        indicator = Indicator(group=group, name=name, scale=scale, definition=definition)
        self.indicators[indicator.id] = indicator
        return indicator
    
    def get_indicators_by_group(self, group: str) -> List[Indicator]:
        return [ind for ind in self.indicators.values() if ind.group == group]


# =============================================================================
# DYNAMIC INDICATOR GENERATION
# =============================================================================

# Pre-defined group templates by domain
DOMAIN_TEMPLATES = {
    "media": {
        "groups": {
            "pvr": "Pouvoir interne — autonomie décisionnelle dans l'organisation",
            "ray": "Rayonnement externe — influence médiatique et publique",
            "sem": "Sémantique — flux de connaissances et compétences"
        },
        "example_indicators": [
            ("pvr", "ildec", "Liberté Décisionnelle — autonomie et impact des décisions"),
            ("ray", "ifrme", "Force du Rayonnement Médiatique — apparitions, rôle, groupe hébergeur"),
            ("sem", "ipcon", "Privatisation des Connaissances — rétention d'expertise"),
            ("sem", "fdcom", "Facteur de Diffusion des Compétences — transmission horizontale")
        ]
    },
    "tech_startup": {
        "groups": {
            "fin": "Finance — contrôle des ressources financières",
            "tec": "Technique — ownership des choix architecturaux",
            "hum": "Humain — influence sur les recrutements et la culture",
            "prd": "Produit — vision et roadmap"
        },
        "example_indicators": [
            ("fin", "cashr", "Cash Runway — contrôle des dépenses et burn rate"),
            ("tec", "archi", "Architecture Ownership — validation des choix techniques"),
            ("hum", "growt", "Growth Influence — poids sur les recrutements"),
            ("prd", "visio", "Product Vision — définition de la roadmap")
        ]
    },
    "research_lab": {
        "groups": {
            "acad": "Académique — production scientifique et publications",
            "fund": "Financement — acquisition de grants et fonds",
            "ment": "Mentorat — formation des doctorants et jeunes chercheurs",
            "coll": "Collaboration — réseau et partenariats externes"
        },
        "example_indicators": [
            ("acad", "publi", "Publication Lead — premier auteur sur les papiers"),
            ("fund", "grant", "Grant Acquisition — apporte les financements"),
            ("ment", "studt", "Student Mentorship — forme les doctorants"),
            ("coll", "netwk", "Collaboration Network — ouvre les portes externes")
        ]
    },
    "art_collective": {
        "groups": {
            "creat": "Créatif — direction artistique et vision",
            "prod": "Production — logistique et réalisation",
            "diff": "Diffusion — visibilité et réseaux de distribution",
            "fin": "Finance — ressources et mécénat"
        },
        "example_indicators": [
            ("creat", "artis", "Direction Artistique — vision et cohérence"),
            ("prod", "logis", "Logistique — réalisation concrète des projets"),
            ("diff", "visib", "Visibilité — réseaux et exposition"),
            ("fin", "mecen", "Mécénat — apporte les ressources financières")
        ]
    }
}


def detect_domain(context: str) -> str:
    """Detect the domain from context description."""
    context_lower = context.lower()
    
    domain_keywords = {
        "media": ["média", "journal", "presse", "tv", "radio", "éditorial", "journaliste"],
        "tech_startup": ["startup", "tech", "logiciel", "développeur", "produit", "cto"],
        "research_lab": ["recherche", "labo", "université", "doctorant", "publication", "scientifique"],
        "art_collective": ["art", "collectif", "artiste", "créatif", "exposition", "galerie"],
        "molecule": ["molécule", "atome", "liaison", "alcaloïde", "chimie", "purique"]
    }
    
    scores = {}
    for domain, keywords in domain_keywords.items():
        scores[domain] = sum(1 for kw in keywords if kw in context_lower)
    
    if max(scores.values()) == 0:
        return "generic"
    
    return max(scores.items(), key=lambda x: x[1])[0]


def generate_indicators_for_domain(domain: str) -> List[Indicator]:
    """Generate a base set of indicators for a given domain."""
    if domain not in DOMAIN_TEMPLATES:
        domain = "generic"
    
    template = DOMAIN_TEMPLATES.get(domain, DOMAIN_TEMPLATES["media"])
    indicators = []
    
    for group, name, definition in template["example_indicators"]:
        indicators.append(Indicator(
            group=group,
            name=name,
            scale="0-3",
            definition=definition
        ))
    
    return indicators


def generate_indicators_from_context(context: str, subject_description: str) -> List[Indicator]:
    """
    Generate indicators dynamically based on context analysis.
    
    In production, this would call an LLM to analyze the subject and propose
    relevant indicators. For now, it uses domain templates + heuristics.
    """
    domain = detect_domain(context)
    base_indicators = generate_indicators_for_domain(domain)
    
    # Heuristics for adjustments based on subject description
    desc_lower = subject_description.lower()
    
    # If the subject mentions specific power dynamics, adjust
    if any(w in desc_lower for w in ["hiérarchie", "pouvoir", "décision", "chef"]):
        # Ensure power indicators exist
        if not any(i.group == "pvr" for i in base_indicators):
            base_indicators.append(Indicator("pvr", "ildec", "0-3", "Liberté Décisionnelle"))
    
    # If the subject mentions knowledge/skills flow
    if any(w in desc_lower for w in ["savoir", "connaissance", "compétence", "transmettre"]):
        if not any(i.group == "sem" for i in base_indicators):
            base_indicators.append(Indicator("sem", "ipcon", "0-3", "Privatisation des Connaissances"))
            base_indicators.append(Indicator("sem", "fdcom", "0-3", "Facteur de Diffusion des Compétences"))
    
    # If the subject mentions external influence
    if any(w in desc_lower for w in ["influence", "rayonnement", "externe", "médiatique"]):
        if not any(i.group == "ray" for i in base_indicators):
            base_indicators.append(Indicator("ray", "ifrme", "0-3", "Force du Rayonnement"))
    
    return base_indicators


# =============================================================================
# OUTPUT GENERATORS
# =============================================================================

def generate_matrix(org: Organization) -> str:
    """Generate a markdown synthesis table."""
    if not org.people:
        return "(organization empty)"
    
    # Build header from indicators
    indicator_ids = list(org.indicators.keys())
    header = "| Person | Role | " + " | ".join(indicator_ids) + " |\n"
    separator = "|--------|------|" + "|".join([":---:"] * len(indicator_ids)) + "|\n"
    
    rows = []
    for name, person in sorted(org.people.items()):
        values = [str(v) if (v := person.get_indicator(ind_id)) is not None else "-" for ind_id in indicator_ids]
        rows.append(f"| {name} | {person.role} | " + " | ".join(values) + " |")
    
    return header + separator + "\n".join(rows)


def generate_tree(org: Organization, root_name: Optional[str] = None) -> str:
    """Generate a hierarchical tree visualization."""
    if not org.people:
        return "(empty organization)"
    
    # Find root: person who doesn't report to anyone
    if root_name:
        root = org.people.get(root_name)
        if not root:
            return f"(root '{root_name}' not found)"
    else:
        roots = [p for p in org.people.values() if not p.links_to]
        if not roots:
            roots = list(org.people.values())[:1]
        root = roots[0]
    
    def build_tree(person: Person, prefix: str = "", is_last: bool = True, is_root: bool = False) -> str:
        # Get first indicator value for display
        first_ind = next(iter(org.indicators.keys()), None)
        first_val = person.get_indicator(first_ind) if first_ind else None
        indicator_str = f"[{first_val}] " if first_val is not None else ""
        
        if is_root:
            line = f"{indicator_str}{person.name} ({person.role})\n"
            new_prefix = ""
        else:
            connector = "└── " if is_last else "├── "
            line = f"{prefix}{connector}{indicator_str}{person.name} ({person.role})\n"
            new_prefix = prefix + ("    " if is_last else "│   ")
        
        # Find subordinates
        subordinates = [p for p in org.people.values() if person.name in p.links_to]
        
        for i, sub in enumerate(subordinates):
            is_last_sub = (i == len(subordinates) - 1)
            line += build_tree(sub, new_prefix, is_last_sub, is_root=False)
        
        return line
    
    return build_tree(root, is_root=True)


def mermaid_id(name: str) -> str:
    """Mermaid node ids accept only [A-Za-z0-9_]."""
    return re.sub(r"\W", "_", name, flags=re.ASCII)


def generate_mermaid(org: Organization) -> str:
    """Generate Mermaid JS diagram code."""
    lines = ["graph TD"]
    
    # Add nodes
    for name, person in org.people.items():
        safe_name = mermaid_id(name)
        label = f"{name}<br/>({person.role})"
        
        # Add top 2 indicator values
        for ind_id in list(org.indicators.keys())[:2]:
            val = person.get_indicator(ind_id)
            if val is not None:
                short_name = ind_id.replace("ind-", "")
                label += f"<br/>{short_name}:{val}"
        
        lines.append(f"    {safe_name}[\"{label}\"]")
    
    # Add edges
    for person in org.people.values():
        safe_name = mermaid_id(person.name)
        for reports_to in person.links_to:
            safe_reports_to = mermaid_id(reports_to)
            lines.append(f"    {safe_name} --> {safe_reports_to}")
    
    return "\n".join(lines)


def export_json(org: Organization) -> str:
    """Export organization as JSON."""
    data = {
        "name": org.name,
        "context": org.context,
        "generated_at": datetime.now().isoformat(),
        "people": [
            {
                "name": p.name,
                "role": p.role,
                "indicators": p.indicators,
                "reports_to": p.links_to,
                "external_entities": p.external_entities,
                "notes": p.notes
            }
            for p in org.people.values()
        ],
        "indicators": {
            ind_id: {
                "group": ind.group,
                "name": ind.name,
                "scale": ind.scale,
                "definition": ind.definition
            }
            for ind_id, ind in org.indicators.items()
        },
        "analysis_notes": org.analysis_notes
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def generate_analysis_report(org: Organization) -> str:
    """Generate a narrative analysis report."""
    report = [
        f"# Analyse Structurelle: {org.name}",
        "",
        f"**Contexte:** {org.context}",
        f"**Généré le:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Indicateurs Détectés",
        ""
    ]
    
    # Group indicators by category
    groups = {}
    for ind_id, ind in org.indicators.items():
        if ind.group not in groups:
            groups[ind.group] = []
        groups[ind.group].append(ind)
    
    for group, indicators in sorted(groups.items()):
        report.append(f"### Groupe `{group}`")
        for ind in indicators:
            report.append(f"- **{ind.id}**: {ind.definition} (échelle: {ind.scale})")
        report.append("")
    
    report.append("## Dynamiques Observées")
    report.append("")
    
    # Analyze patterns
    if org.people:
        # Find highest/lowest on each indicator
        for ind_id in org.indicators.keys():
            values = [(p.name, p.get_indicator(ind_id)) for p in org.people.values() if p.get_indicator(ind_id) is not None]
            if values:
                highest = max(values, key=lambda x: x[1])
                lowest = min(values, key=lambda x: x[1])
                if highest[1] != lowest[1]:
                    report.append(f"- **{ind_id}**: {highest[0]} ({highest[1]}) vs {lowest[0]} ({lowest[1]})")
    
    report.append("")
    if org.analysis_notes:
        report.append("## Notes d'Analyse")
        report.append("")
        report.append(org.analysis_notes)
    
    return "\n".join(report)


# =============================================================================
# DEMO: CAFFEINE REFERENCE CASE
# =============================================================================

# Molecular domain: the 3 axes (power / knowledge flow / external reach) are
# transposed to a molecule. Actors are structural groups, not people.
DOMAIN_TEMPLATES["molecule"] = {
    "groups": {
        "rea": "Réactivité — quel groupe dicte le comportement de la molécule",
        "ele": "Électronique — rétention vs partage des électrons",
        "ext": "Externe — interactions avec le solvant, les récepteurs",
        "met": "Métabolisme — fragilité face aux enzymes"
    },
    "example_indicators": [
        ("rea", "sitac", "Site Actif — poids dans la reconnaissance et la réactivité"),
        ("ext", "hbond", "Liaison Externe — accepteur/donneur H, polarité exposée"),
        ("ele", "local", "Localisation Électronique — doublets retenus hors système π"),
        ("ele", "delox", "Délocalisation — participation au système π conjugué"),
        ("met", "labil", "Labilité Métabolique — cible de transformation enzymatique")
    ]
}


def demo_cafeine() -> Organization:
    """Create the caffeine reference case (1,3,7-trimethylxanthine, PubChem CID 2519).

    Scores are qualitative (0-3). They must be checked against computed
    descriptors (PubChem / RDKit) — that check is the point of the case.
    """
    org = Organization(
        name="Caféine",
        context="Molécule — 1,3,7-triméthylxanthine, C8H10N4O2, alcaloïde purique"
    )

    for group, name, definition in DOMAIN_TEMPLATES["molecule"]["example_indicators"]:
        org.register_indicator(group, name, "0-3", definition)

    def add(name, role, scores, reports_to=None, external=None, notes=""):
        org.add_person(name, role, reports_to=reports_to, external_entities=external)
        org.people[name].indicators = dict(zip(
            ["ind-rea-sitac", "ind-ext-hbond", "ind-ele-local", "ind-ele-delox", "ind-met-labil"],
            scores
        ))
        org.people[name].notes = notes

    add("Noyau xanthine", "Squelette purique bicyclique plan", [3, 1, 0, 3, 0],
        external=["Récepteurs adénosine A1/A2A (mimétisme purine)"],
        notes="Le squelette mime l'adénosine : antagonisme des récepteurs A1/A2A")
    add("Cycle imidazole", "Cycle à 5 (N7, C8, N9)", [2, 2, 1, 3, 0],
        reports_to=["Noyau xanthine"])
    add("Cycle pyrimidinedione", "Cycle à 6 (N1, C2, N3, C6)", [2, 2, 1, 3, 0],
        reports_to=["Noyau xanthine"])
    add("N9", "Azote imidazole non substitué", [2, 3, 2, 1, 0],
        reports_to=["Cycle imidazole"],
        external=["Eau (solvatation)", "Site de protonation (pKa ≈ 0,6)"],
        notes="Doublet sp2 dans le plan, hors système π : principal accepteur H")
    add("N7-CH3", "Méthyle sur azote imidazole", [1, 0, 0, 2, 1],
        reports_to=["Cycle imidazole"],
        external=["CYP1A2 → théophylline (~4 %)"])
    add("C6=O", "Carbonyle", [2, 2, 1, 2, 0],
        reports_to=["Cycle pyrimidinedione"],
        external=["Accepteur H"])
    add("C2=O", "Carbonyle", [1, 2, 1, 2, 0],
        reports_to=["Cycle pyrimidinedione"],
        external=["Accepteur H"])
    add("N1-CH3", "Méthyle sur azote amide", [1, 0, 0, 2, 2],
        reports_to=["Cycle pyrimidinedione"],
        external=["CYP1A2 → théobromine (~12 %)"])
    add("N3-CH3", "Méthyle sur azote amide", [1, 0, 0, 2, 3],
        reports_to=["Cycle pyrimidinedione"],
        external=["CYP1A2 → paraxanthine (~84 %)"])

    org.analysis_notes = """
**Observation clé :** découplage pouvoir / rayonnement, comme dans une organisation.
- Noyau xanthine : sitac 3, hbond 1 — il « décide » (forme reconnue par le récepteur) sans interagir lui-même.
- N9 : hbond 3 — principal porte-parole vers l'extérieur (solvant, protonation).

**Flux électronique :**
- Cycles et noyau : delox 3 — le savoir est partagé (système π conjugué).
- N9 : local 2 — doublet retenu hors du système π, d'où son rôle d'accepteur.

**Fragilité :** les trois méthyles sont les points faibles (labil). N3-CH3 domine :
la N3-déméthylation par CYP1A2 donne la paraxanthine, métabolite majoritaire.

**À vérifier :** confronter les scores aux descripteurs calculés (TPSA, accepteurs/donneurs H,
charges partielles) via PubChem CID 2519 ou RDKit.
"""

    return org


# =============================================================================
# CLI INTERFACE
# =============================================================================

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        print("=" * 60)
        print("STRUCTURAL MAPPING — Caféine Demo")
        print("=" * 60)
        print()
        
        org = demo_cafeine()
        
        print("## Contexte")
        print(f"**Organisation:** {org.name}")
        print(f"**Domaine:** {detect_domain(org.context)}")
        print(f"**Indicateurs:** {len(org.indicators)}")
        print()
        
        print("## Matrice de Synthèse")
        print()
        print(generate_matrix(org))
        print()
        
        print("## Arborescence Hiérarchique")
        print()
        print("```")
        print(generate_tree(org))
        print("```")
        print()
        
        print("## Diagramme Mermaid")
        print()
        print("```mermaid")
        print(generate_mermaid(org))
        print("```")
        print()
        
        print("## Rapport d'Analyse")
        print()
        print(generate_analysis_report(org))
        print()
        
        print("## Export JSON")
        print()
        print("```json")
        print(export_json(org))
        print("```")
        
    else:
        print("Usage: python matrix.py [--demo]")
        print()
        print("Options:")
        print("  --demo    Run the caffeine reference case")
        print()
        print("Example:")
        print("  python matrix.py --demo")


if __name__ == "__main__":
    main()
