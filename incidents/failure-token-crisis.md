



**Attention  :**
- `token-strategie` est une brique **OpenClaw core**, pas un module applicatif de `ferule-core`
- La ferule **n'appelle pas** token-strategie, elle ne l**contient pas**   `token-strategie`
- Il n'a aucun rôle dans la ferule, ni aucun rapport avec la ferule — il devrait être géré au niveau de `openclaw`

**Conséquence :** Token-strategie est mal positionné dès le départ.

---
