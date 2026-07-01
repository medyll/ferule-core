# USER-NOTES — core-cognition

## Preferences

- Langue : anglais dans les fichiers de développement
- Ton : formel, conforme core-standard

## Decisions

- `core-cognition` est l'oreille d'OpenClaw — point d'entrée pour toute demande brute
- Elle interprète l'intent, appelle `machinery` pour la classification, soumet à Place de Grève
- Elle ne fait pas le travail — elle comprend et route
- Les LLMs qui soumettent des missions avec `context:domain` déjà résolu n'ont pas besoin de passer par core-cognition
- `logs are cognition` — si application-core voit ses propres logs, c'est de la métacognition

## Instructions

- Lire `machinery/development/v1-machinery/classifier.mjs` avant tout routing
- Ne jamais soumettre à Place de Grève sans `context:domain` résolu
- En cas d'ambiguïté, demander confirmation avant de soumettre
