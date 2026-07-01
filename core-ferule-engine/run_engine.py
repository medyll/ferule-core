# run_engine.py — Core Ferule Engine entry point (removed)
# The engine is now a pure Python library (RuleEngine class).
# Use it directly in your own scripts:
#
#   from core.engine import RuleEngine
#   engine = RuleEngine()
#   result = engine.process({"id": "m1", "mission": "..."})
#
# No API server, no file bus, no background processes.

raise SystemExit(
    "run_engine.py is deprecated. "
    "The Core Ferule Engine is now a library only. "
    "Import RuleEngine from core.engine directly."
)
