# PHASE 1 — Initialisation V1

> Scaffold de l'application, définition du scope, et expérimentation sans risque pour Maturation.

---

### 1.1 — Définir le Scope Exact

**File :** `USER-NOTES.md`  
**Problem :** Le scope n'est pas encore défini (remplacement ? coexistence ? externalisation ?)  
**Risk :** Confusion entre Idéation et Maturation

- [ ] Clarifier : Idéation remplace-t-il Maturation ?
- [ ] Clarifier : Ou coexistence des deux ?
- [ ] Clarifier : Ou externalisation du PRD de BMAD-method ?
- [ ] Documenter la décision dans `USER-NOTES.md`

**Effort :** 15 min  
**Status :** 📋 En attente (décision utilisateur)

---

### 1.2 — Documenter les Différences avec Maturation

**File :** `README.md`  
**Problem :** Risque de doublon ou confusion avec Maturation  
**Risk :** Utilisateur ne sait pas où aller

- [ ] Lister les fonctionnalités de Maturation
- [ ] Lister les fonctionnalités prévues pour Idéation
- [ ] Identifier les chevauchements
- [ ] Documenter les différences dans `README.md`

**Effort :** 15 min  
**Status :** 📋 En attente

---

### 1.3 — Créer les Premiers Fichiers d'Idées

**File :** `ideas/` (à créer)  
**Problem :** Aucune idée capturée pour l'instant  
**Risk :** Application vide, pas de test réel

- [ ] Définir le format des fichiers d'idées
- [ ] Créer le dossier `ideas/`
- [ ] Capturer 1-3 idées test
- [ ] Tester le workflow

**Effort :** 30 min  
**Status :** 📋 En attente

---

### 1.4 — Tester le Workflow avec l'Utilisateur

**File :** N/A  
**Problem :** L'application n'a pas été testée en conditions réelles  
**Risk :** Mauvaise adoption, retour en arrière

- [ ] Utilisateur capture une idée dans Idéation
- [ ] Utilisateur compare avec Maturation
- [ ] Recueillir le feedback
- [ ] Ajuster si besoin

**Effort :** 30 min  
**Status :** 📋 En attente

---

### 1.5 — Décider : Fusion, Remplacement, ou Coexistence

**File :** `USER-NOTES.md`  
**Problem :** La relation avec Maturation n'est pas tranchée  
**Risk :** Deux systèmes parallèles, confusion

- [ ] Après tests (1.4), décider :
  - **Option A :** Coexistence (les deux restent)
  - **Option B :** Remplacement (Idéation → Maturation)
  - **Option C :** Fusion (meilleurs des deux)
- [ ] Documenter la décision
- [ ] Planifier la migration si nécessaire

**Effort :** 15 min  
**Status :** 📋 En attente

---

## Summary

| Step | Task | Effort | Status |
|------|------|--------|--------|
| **1.1** | Définir le scope exact | 15 min | 📋 En attente |
| **1.2** | Documenter différences avec Maturation | 15 min | 📋 En attente |
| **1.3** | Créer premiers fichiers d'idées | 30 min | 📋 En attente |
| **1.4** | Tester le workflow | 30 min | 📋 En attente |
| **1.5** | Décider fusion/remplacement/coexistence | 15 min | 📋 En attente |

---

## Guard-Rail

**Règle absolue :** Ne pas toucher à Maturation (`D:\boulot\dev\maturation\`, skill `maturation`) tant que la décision n'est pas prise (1.5).
