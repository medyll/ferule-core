# watchdog — SCRATCHPAD

> Raw captures. Freeform. No rules.

Système d'alerte indépendant qui surveille les watchers et signale les pannes.
- Cron 5min via Task Scheduler Windows
- Vérifie processus dashboard-watcher.mjs
- Vérifie logs scan-place-de-greve.mjs récents (< 1h)
- Vérifie context-registry.json lisible
- Alerte: log JSONL + notification core-squad
- Zero dépendance externe — pur Node.js
