#!/usr/bin/env python3
"""
LLM-Powered Indicator Generator for Structural Mapping

This module uses an LLM to dynamically generate indicators based on
the organizational context, rather than relying on pre-defined templates.

The nomenclature follows: ind-[group]-[name5]
- group: 3 letters (category)
- name5: 5 letters (specific name)
"""

import json
import sys
import os
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime


# =============================================================================
# GROUP CATALOG (3-letter categories)
# =============================================================================

GROUP_DEFINITIONS = {
    # Power & Decision
    "pvr": "Pouvoir interne — décision, autonomie, autorité",
    "dec": "Décision — processus décisionnel, validation",
    "aut": "Autonomie — liberté d'action, indépendance",
    
    # Influence & Communication
    "ray": "Rayonnement — influence externe, visibilité",
    "com": "Communication — flux d'information, transmission",
    "inf": "Influence — capacité à persuader, orienter",
    
    # Knowledge & Skills
    "sem": "Sémantique — connaissances, expertise",
    "tec": "Technique — compétences techniques, savoir-faire",
    "aca": "Académique — publications, recherche",
    
    # Resources & Finance
    "fin": "Finance — budget, trésorerie, investissement",
    "res": "Ressources — allocation, gestion des moyens",
    "mat": "Matériel — équipements, infrastructure",
    
    # Human & Culture
    "hum": "Humain — recrutement, développement, bien-être",
    "cul": "Culture — valeurs, ambiance, cohésion",
    "men": "Mentorat — formation, accompagnement",
    
    # Product & Strategy
    "prd": "Produit — vision, roadmap, features",
    "str": "Stratégie — orientation long terme, positioning",
    "inn": "Innovation — R&D, nouveauté, disruption",
    
    # Operations
    "ops": "Opérations — exécution, delivery, process",
    "log": "Logistique — organisation, flux, supply",
    "qua": "Qualité — standards, validation, conformité",
    
    # Network & Relations
    "rel": "Relations — partenariats, réseau externe",
    "col": "Collaboration — travail d'équipe, synergies",
    "all": "Alliances — coopérations stratégiques",
}


# =============================================================================
# LLM PROMPT TEMPLATES
# =============================================================================

INDICATOR_GENERATION_PROMPT = """
Tu es un expert en analyse organisationnelle. Ta tâche est de générer des indicateurs de pouvoir et d'influence adaptés au contexte fourni.

## Contexte de l'organisation
{context}

## Domaine détecté
{domain}

## Règles de nomenclature
Chaque indicateur suit le format: `ind-[group]-[name5]`
- `group`: 3 lettres minuscules (catégorie)
- `name5`: 5 lettres minuscules (nom spécifique)

## Groups disponibles (3 lettres)
{groups}

## Tâche
Génère EXACTEMENT {num_indicators} indicateurs pertinents pour cette organisation.

Pour chaque indicateur, fournis:
1. L'ID complet (ex: ind-pvr-ildec)
2. Le nom lisible (ex: Liberté Décisionnelle)
3. La définition (1 phrase)
4. L'échelle (ex: 0-3 ou 0-5)
5. Un exemple de ce qui vaut le score max

## Format de réponse attendu (JSON strict)
{{
    "indicators": [
        {{
            "group": "pvr",
            "name": "ildec",
            "label": "Liberté Décisionnelle",
            "definition": "Autonomie et impact dans les décisions",
            "scale": "0-3",
            "max_example": "Décide seul des orientations majeures"
        }}
    ],
    "rationale": "Explication du choix de ces indicateurs pour ce contexte"
}}

Réponds UNIQUEMENT avec le JSON, pas de texte autour.
"""

DOMAIN_ANALYSIS_PROMPT = """
Analyse ce contexte organisationnel et identifie le domaine principal.

## Contexte
{context}

## Domaines possibles
- media: Journal, presse, communication, influence médiatique
- tech_startup: Startup tech, SaaS, produit digital, équipe technique
- research_lab: Recherche académique, publications, thèses, subventions
- art_collective: Art, création, exposition, production culturelle
- healthcare: Santé, médical, patients, soins
- education: Éducation, formation, étudiants, pédagogie
- nonprofit: Association, ONG, impact social, bénévolat
- manufacturing: Production, usine, supply chain, industriel
- finance: Banque, investissement, trading, assurance
- other: Autre domaine non listé

## Tâche
Identifie le domaine le plus pertinent et explique pourquoi.

## Format de réponse (JSON strict)
{{
    "domain": "domaine_identifié",
    "confidence": 0.0-1.0,
    "reasoning": "Pourquoi ce domaine",
    "specificities": ["aspect1", "aspect2", "spécificités du contexte"]
}}

Réponds UNIQUEMENT avec le JSON.
"""


# =============================================================================
# MOCK LLM (for standalone testing without API)
# =============================================================================

class MockLLM:
    """
    Simule un LLM pour générer des indicateurs sans appel API.
    Utilise des patterns et heuristics basés sur le contexte.
    """
    
    def __init__(self):
        self.domain_indicators = {
            "media": [
                {"group": "pvr", "name": "ildec", "label": "Liberté Décisionnelle", "definition": "Autonomie éditoriale et impact décisionnel", "scale": "0-3"},
                {"group": "ray", "name": "ifrme", "label": "Force Rayonnement", "definition": "Influence médiatique et visibilité externe", "scale": "0-3"},
                {"group": "sem", "name": "ipcon", "label": "Privatisation Connaissances", "definition": "Rétention d'expertise et d'information", "scale": "0-3"},
                {"group": "sem", "name": "fdcom", "label": "Diffusion Compétences", "definition": "Transmission horizontale des savoirs", "scale": "0-3"},
            ],
            "tech_startup": [
                {"group": "fin", "name": "cashr", "label": "Cash Runway Control", "definition": "Contrôle sur la trésorerie et le burn rate", "scale": "0-3"},
                {"group": "tec", "name": "archi", "label": "Architecture Ownership", "definition": "Maîtrise des choix techniques majeurs", "scale": "0-3"},
                {"group": "prd", "name": "visio", "label": "Product Vision", "definition": "Influence sur la roadmap produit", "scale": "0-3"},
                {"group": "hum", "name": "growt", "label": "Growth Influence", "definition": "Impact sur le recrutement et la culture", "scale": "0-3"},
            ],
            "research_lab": [
                {"group": "aca", "name": "publi", "label": "Publication Lead", "definition": "Leadership sur les publications académiques", "scale": "0-3"},
                {"group": "fin", "name": "grant", "label": "Grant Acquisition", "definition": "Capacité à obtenir des financements", "scale": "0-3"},
                {"group": "men", "name": "studt", "label": "Student Mentorship", "definition": "Encadrement des doctorants et jeunes chercheurs", "scale": "0-3"},
                {"group": "col", "name": "netwk", "label": "Collaboration Network", "definition": "Réseau de collaborations externes", "scale": "0-3"},
            ],
            "art_collective": [
                {"group": "creat", "name": "artis", "label": "Direction Artistique", "definition": "Vision et orientation artistique", "scale": "0-3"},
                {"group": "prod", "name": "logis", "label": "Logistique Production", "definition": "Gestion de la production et des délais", "scale": "0-3"},
                {"group": "diff", "name": "visib", "label": "Visibilité Externe", "definition": "Rayonnement et relations presse/galeries", "scale": "0-3"},
                {"group": "fin", "name": "mecen", "label": "Mécénat Finance", "definition": "Accès aux financements et subventions", "scale": "0-3"},
            ],
            "healthcare": [
                {"group": "med", "name": "diagp", "label": "Diagnostic Power", "definition": "Autorité sur les diagnostics et traitements", "scale": "0-3"},
                {"group": "adm", "name": "budgt", "label": "Budget Control", "definition": "Contrôle sur les ressources du service", "scale": "0-3"},
                {"group": "tea", "name": "super", "label": "Supervision", "definition": "Encadrement des équipes soignantes", "scale": "0-3"},
                {"group": "res", "name": "proto", "label": "Protocoles", "definition": "Influence sur les protocoles de soin", "scale": "0-3"},
            ],
            "education": [
                {"group": "ped", "name": "curri", "label": "Curriculum Design", "definition": "Conception des programmes pédagogiques", "scale": "0-3"},
                {"group": "adm", "name": "admin", "label": "Administration", "definition": "Pouvoir administratif et budgétaire", "scale": "0-3"},
                {"group": "men", "name": "stude", "label": "Student Impact", "definition": "Influence directe sur les étudiants", "scale": "0-3"},
                {"group": "res", "name": "resea", "label": "Research Output", "definition": "Production et direction de recherche", "scale": "0-3"},
            ],
            "nonprofit": [
                {"group": "mis", "name": "align", "label": "Mission Alignment", "definition": "Fidélité à la mission et aux valeurs", "scale": "0-3"},
                {"group": "fun", "name": "fundr", "label": "Fundraising", "definition": "Capacité à lever des fonds", "scale": "0-3"},
                {"group": "vol", "name": "volun", "label": "Volunteer Mgmt", "definition": "Gestion et mobilisation des bénévoles", "scale": "0-3"},
                {"group": "imp", "name": "outcm", "label": "Outcome Impact", "definition": "Mesure et communication de l'impact", "scale": "0-3"},
            ],
            "manufacturing": [
                {"group": "ops", "name": "produ", "label": "Production Flow", "definition": "Contrôle sur les flux de production", "scale": "0-3"},
                {"group": "qua", "name": "quali", "label": "Quality Control", "definition": "Autorité sur les standards qualité", "scale": "0-3"},
                {"group": "sup", "name": "chain", "label": "Supply Chain", "definition": "Gestion des fournisseurs et stocks", "scale": "0-3"},
                {"group": "saf", "name": "hsenv", "label": "Health Safety", "definition": "Responsabilité sécurité et environnement", "scale": "0-3"},
            ],
            "finance": [
                {"group": "inv", "name": "alloc", "label": "Asset Allocation", "definition": "Décisions d'allocation d'actifs", "scale": "0-3"},
                {"group": "ris", "name": "mlimit", "label": "Risk Limits", "definition": "Définition des limites de risque", "scale": "0-3"},
                {"group": "cli", "name": "relat", "label": "Client Relations", "definition": "Gestion des relations clients majeurs", "scale": "0-3"},
                {"group": "com", "name": "repor", "label": "Reporting", "definition": "Contrôle sur les rapports et communications", "scale": "0-3"},
            ],
        }
    
    def generate(self, context: str, domain: str, num_indicators: int = 4) -> Dict:
        """
        Génère des indicateurs basés sur le domaine détecté.
        Enrichit avec des éléments spécifiques au contexte.
        """
        indicators = self.domain_indicators.get(domain, self.domain_indicators["media"])[:num_indicators]
        
        # Analyse simplifiée du contexte pour ajuster les labels
        context_lower = context.lower()
        
        # Ajustements basés sur des mots-clés
        adjustments = []
        if "urgent" in context_lower or "crise" in context_lower:
            adjustments.append("Contexte de crise — privilégier indicateurs de décision rapide")
        if "croissance" in context_lower or "growth" in context_lower:
            adjustments.append("Contexte de croissance — indicateurs de scaling importants")
        if "équipe" in context_lower or "team" in context_lower:
            adjustments.append("Dimension équipe forte — indicateurs humains pertinents")
        if "budget" in context_lower or "finance" in context_lower:
            adjustments.append("Contrainte budgétaire — indicateurs financiers critiques")
        
        rationale = f"Indicateurs générés pour le domaine '{domain}'"
        if adjustments:
            rationale += ". " + ". ".join(adjustments)
        
        return {
            "indicators": indicators,
            "rationale": rationale,
            "domain": domain,
            "context_analysis": adjustments
        }
    
    def analyze_domain(self, context: str) -> Dict:
        """
        Analyse le contexte pour détecter le domaine.
        """
        context_lower = context.lower()
        
        domain_scores = {
            "media": sum(1 for kw in ["média", "journal", "presse", "article", "rédaction", "éditorial"] if kw in context_lower),
            "tech_startup": sum(1 for kw in ["startup", "tech", "saas", "produit", "développeur", "cto", "ceo"] if kw in context_lower),
            "research_lab": sum(1 for kw in ["recherche", "labo", "université", "thèse", "publication", "chercheur"] if kw in context_lower),
            "art_collective": sum(1 for kw in ["art", "collectif", "artiste", "exposition", "créatif", "culturel"] if kw in context_lower),
            "healthcare": sum(1 for kw in ["santé", "médical", "hôpital", "patient", "soin", "docteur"] if kw in context_lower),
            "education": sum(1 for kw in ["éducation", "école", "université", "étudiant", "professeur", "formation"] if kw in context_lower),
            "nonprofit": sum(1 for kw in ["association", "ong", "bénévole", "social", "impact", "non-profit"] if kw in context_lower),
            "manufacturing": sum(1 for kw in ["production", "usine", "manufacturing", "supply", "industrie"] if kw in context_lower),
            "finance": sum(1 for kw in ["finance", "banque", "investissement", "trading", "asset"] if kw in context_lower),
        }
        
        best_domain = max(domain_scores.items(), key=lambda x: x[1])
        
        if best_domain[1] == 0:
            return {
                "domain": "other",
                "confidence": 0.3,
                "reasoning": "Aucun domaine clairement identifié — utilisation de templates génériques",
                "specificities": ["Domaine non standard"]
            }
        
        return {
            "domain": best_domain[0],
            "confidence": min(0.9, 0.4 + best_domain[1] * 0.15),
            "reasoning": f"Domaine détecté par {best_domain[1]} mots-clés pertinents",
            "specificities": [f"Score: {best_domain[1]}/5"]
        }


# =============================================================================
# REAL LLM CLIENT (optional — for when API is available)
# =============================================================================

class LLMClient:
    """
    Client LLM réel pour génération d'indicateurs.
    Supporte plusieurs providers.
    """
    
    def __init__(self, provider: str = "mock"):
        self.provider = provider
        self.mock = MockLLM()
    
    def generate_indicators(self, context: str, num_indicators: int = 4) -> Dict:
        """
        Génère des indicateurs via LLM.
        """
        # Analyse du domaine d'abord
        domain_result = self.analyze_domain(context)
        domain = domain_result["domain"]
        
        if self.provider == "mock":
            return self.mock.generate(context, domain, num_indicators)
        
        # TODO: Implémenter appels API réels (OpenAI, Anthropic, etc.)
        # Pour l'instant, fallback sur mock
        return self.mock.generate(context, domain, num_indicators)
    
    def analyze_domain(self, context: str) -> Dict:
        """
        Analyse le contexte pour déterminer le domaine.
        """
        return self.mock.analyze_domain(context)


# =============================================================================
# MAIN GENERATION FUNCTION
# =============================================================================

def generate_indicators_from_context(
    context: str,
    num_indicators: int = 4,
    provider: str = "mock"
) -> Dict:
    """
    Génère des indicateurs adaptés au contexte organisationnel.
    
    Args:
        context: Description de l'organisation
        num_indicators: Nombre d'indicateurs à générer (défaut: 4)
        provider: "mock" ou nom du provider LLM
    
    Returns:
        Dict avec indicators, rationale, domain, etc.
    """
    client = LLMClient(provider)
    return client.generate_indicators(context, num_indicators)


def detect_domain(context: str) -> Dict:
    """
    Détecte le domaine d'une organisation à partir du contexte.
    
    Args:
        context: Description de l'organisation
    
    Returns:
        Dict avec domain, confidence, reasoning, specificities
    """
    client = LLMClient("mock")
    return client.analyze_domain(context)


# =============================================================================
# CLI INTERFACE
# =============================================================================

def main():
    if len(sys.argv) < 2:
        print("LLM Indicator Generator for Structural Mapping")
        print()
        print("Usage:")
        print("  python llm_indicators.py <context>")
        print("  python llm_indicators.py --demo")
        print("  python llm_indicators.py --domains")
        print()
        print("Examples:")
        print('  python llm_indicators.py "Startup tech de 15 personnes — SaaS B2B"')
        print('  python llm_indicators.py "Labo de recherche en IA avec 30 chercheurs"')
        sys.exit(0)
    
    if sys.argv[1] == "--demo":
        print("="*70)
        print("LLM INDICATOR GENERATOR — Demo")
        print("="*70)
        print()
        
        demo_contexts = [
            "Startup tech de 15 personnes — SaaS B2B, enjeux de cash runway",
            "Labo de recherche en IA avec 30 chercheurs et 5 doctorants",
            "Collectif d'artistes contemporains — 8 membres, expositions",
            "Journal indépendant — rédaction de 12 personnes",
            "Hôpital public — service de cardiologie, 50 soignants"
        ]
        
        for context in demo_contexts:
            print(f"CONTEXTE: \"{context}\"")
            print("-"*70)
            
            result = generate_indicators_from_context(context)
            
            print(f"Domaine détecté: {result['domain']}")
            print(f"Rationale: {result['rationale']}")
            print()
            print("Indicateurs générés:")
            for ind in result["indicators"]:
                print(f"  ind-{ind['group']}-{ind['name']}: {ind['label']}")
                print(f"    → {ind['definition']} (échelle: {ind['scale']})")
            print()
            print("="*70)
            print()
        
        sys.exit(0)
    
    if sys.argv[1] == "--domains":
        print("Domaines supportés:")
        print("-"*50)
        for domain, indicators in MockLLM().domain_indicators.items():
            print(f"\n{domain.upper()}")
            print(f"  {len(indicators)} indicateurs disponibles")
            for ind in indicators[:2]:
                print(f"    - ind-{ind['group']}-{ind['name']}: {ind['label']}")
        sys.exit(0)
    
    # Generate for the provided context
    context = " ".join(sys.argv[1:])
    
    print(f"CONTEXTE: \"{context}\"")
    print("="*70)
    
    # Domain detection
    domain_result = detect_domain(context)
    print(f"\n📊 DOMAINE DÉTECTÉ")
    print(f"   Domaine: {domain_result['domain']}")
    print(f"   Confiance: {domain_result['confidence']:.0%}")
    print(f"   Raisonnement: {domain_result['reasoning']}")
    if domain_result.get('specificities'):
        print(f"   Spécificités: {', '.join(domain_result['specificities'])}")
    
    # Indicator generation
    result = generate_indicators_from_context(context)
    
    print(f"\n📋 INDICATEURS GÉNÉRÉS ({len(result['indicators'])})")
    print()
    
    for i, ind in enumerate(result["indicators"], 1):
        print(f"{i}. ind-{ind['group']}-{ind['name']}")
        print(f"   Label: {ind['label']}")
        print(f"   Définition: {ind['definition']}")
        print(f"   Échelle: {ind['scale']}")
        print()
    
    print(f"💡 RATIONALE")
    print(f"   {result['rationale']}")
    
    # JSON output
    print(f"\n📄 JSON OUTPUT")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
