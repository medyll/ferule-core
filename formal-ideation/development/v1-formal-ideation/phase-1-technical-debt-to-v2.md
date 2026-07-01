# TECHNICAL DEBT — Idéation V1 → V2

> Items identifiés lors de l'initialisation V1 qui doivent être adressés en V2.

---

### TD-01 — Format des Idées Non Défini

**Discovered :** 2026-04-11 — Initial scaffold — Agent  
**File :** `README.md`  
**Issue :** Aucun format standard pour capturer les idées (titre, tags, statut, contenu ?)  
**Impact :** Idées capturées de manière incohérente  
**Risk :** Medium

- [ ] Définir un template d'idée (titre, tags, statut, date, contenu)
- [ ] Créer un exemple dans `ideas/`
- [ ] Documenter dans `README.md`

**Effort :** 20 min

---

### TD-02 — Relation avec Maturation Non Clarifiée

**Discovered :** 2026-04-11 — Initial scaffold — Agent  
**File :** `USER-NOTES.md`  
**Issue :** La relation entre Idéation et Maturation n'est pas définie (coexistence ? remplacement ?)  
**Impact :** Confusion utilisateur, risque de doublon  
**Risk :** High

- [ ] Tester les deux systèmes en parallèle
- [ ] Recueillir feedback utilisateur
- [ ] Décider : coexistence, remplacement, ou fusion
- [ ] Documenter dans `USER-NOTES.md`

**Effort :** 1h (tests + décision)

---

### TD-03 — Pas de Workflow de Maturation des Idées

**Discovered :** 2026-04-11 — Initial scaffold — Agent  
**File :** `README.md`  
**Issue :** Comment une idée passe de "brute" à "mûre" ? Aucun workflow défini.  
**Impact :** Idées stagnent, pas de progression  
**Risk :** Medium

- [ ] Définir les statuts (germination → en croissance → mature → archivée)
- [ ] Définir les transitions entre statuts
- [ ] Créer un fichier de suivi de progression

**Effort :** 30 min

---

### TD-04 — Pas de Liens avec BMAD

**Discovered :** 2026-04-11 — Initial scaffold — Agent  
**File :** `README.md`  
**Issue :** Comment une idée devient un projet BMAD ? Aucun lien défini.  
**Impact :** Idées et projets déconnectés  
**Risk :** Low

- [ ] Définir le critère de passage "idée → projet"
- [ ] Créer un fichier de liaison `bmad-links.md`
- [ ] Documenter le workflow

**Effort :** 20 min

---

### TD-05 — Index des Idées Manquant

**Discovered :** 2026-04-11 — Initial scaffold — Agent  
**File :** `ideas/`  
**Issue :** Comment retrouver une idée ? Aucun index, tags, ou recherche.  
**Impact :** Idées perdues, duplication  
**Risk :** Medium

- [ ] Créer un index `ideas/INDEX.md`
- [ ] Définir un système de tags
- [ ] Optionnel : Script de recherche

**Effort :** 30 min

---

## Technical Debt Summary

| ID | Item | Effort | Status |
|----|------|--------|--------|
| TD-01 | Format des idées non défini | 20 min | 📋 Open |
| TD-02 | Relation avec Maturation non clarifiée | 1h | 📋 Open |
| TD-03 | Pas de workflow de maturation | 30 min | 📋 Open |
| TD-04 | Pas de liens avec BMAD | 20 min | 📋 Open |
| TD-05 | Index des idées manquant | 30 min | 📋 Open |

---

## Notes

- **Priorité :** TD-02 (relation avec Maturation) — bloquant pour la suite
- **Garde-fou :** Ne pas toucher à Maturation tant que TD-02 n'est pas résolu
