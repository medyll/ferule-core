# SCRATCHPAD — core-openspace

---

## Session de conception — 2026-04-12

### 1. Diagnostic OCM

- `ocm-INSTRUCTIONS.md` = canal monolithique, modèle 1-à-1 entre apps
- Pas d'orchestration multi-projet possible avec ce modèle
- Chaque nouvelle relation inter-app crée un nouveau fichier ad hoc → entropie
- Décision : ne pas patcher OCM. Créer une app dédiée au bus de protocole.

---

### 2. Design — centralisé vs distribué

Rejeté : channels par projet
- distribué, verbeux, chaque app gère sa propre messagerie
- "old school" — pas différent de OCM en pratique

Retenu : protocole déclaré en un point unique
- les apps s'enregistrent via `capabilities` dans `protocol.json`
- le routage dérive de cette déclaration, pas des apps
- une seule source de vérité pour "qui écoute quoi"

---

### 3. Naming

Écartés :
- `context-registry` — appartient à Place de Grève (domaine différent)
- `openspace-bus` — trop technique, évoque une infrastructure réseau
- `openspace-relay` — relay implique une couche intermédiaire passive

Retenu : `core-openspace`
- cohérent avec le préfixe `core-` des apps système
- "openspace" = espace commun de déclaration, pas un bus caché

---

### 4. Principe fondateur

Un protocole brut qui s'exprime en un point.

- Les apps déclarent `emit:X` (ce qu'elles produisent) et `handle:X` (ce qu'elles consomment)
- Ces déclarations vivent dans `protocol.json`, pas dans les apps elles-mêmes
- Le dispatcher lit `protocol.json` et route — il n'a aucune logique propre
- Toute modification du routage passe par `protocol.json` : traçable, auditable, unique

Formule retenue : "les apps ne s'écrivent plus de fichiers-messages ad hoc — elles déclarent leurs événements et handlers via ce protocole."

---

## Proposition métier

### Le scratchpad comme norme core-standards

**Problème observé pendant cette session :**
Le scratchpad a été créé vide par convention, mais les décisions de conception (OCM, naming, design pattern) ont été produites en conversation — elles n'ont pas de trace dans le projet.
Sans ce remplissage explicite, un agent futur ne sait pas pourquoi `core-openspace` existe, pourquoi OCM a été rejeté, pourquoi le design est centralisé.

**Proposition :**

| Élément | Contenu |
|---------|---------|
| Moment de création | Au démarrage de toute session de conception — avant le scaffold, pas après |
| Qui alimente | L'humain décide du contenu, l'agent transcrit à la demande |
| Contenu minimal | (1) le problème qui a déclenché le projet, (2) les options rejetées + raison, (3) la décision retenue + principe |

**Règle proposée pour core-standard §14 :**

> Si une session de conception précède le scaffold, `SCRATCHPAD.md` doit être alimenté en fin de session avec au minimum : diagnostic d'origine, options rejetées, décision retenue. Un scratchpad vide après scaffold est un signal d'alerte — les décisions de conception ont été perdues.

**Format minimal recommandé (pas imposé) :**

```
## Session — YYYY-MM-DD
### Problème
### Options rejetées
### Décision retenue
### Principe fondateur
```

**Note :** Ce n'est pas un log — c'est une capture de raisonnement. Le BLUEPRINT formalise, le SCRATCHPAD garde la trace brute du "pourquoi".
