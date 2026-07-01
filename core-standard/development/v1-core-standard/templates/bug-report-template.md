# TEMPLATE — Bug Report

> Standard structure for reports/bug-reports.md.
> See `applications/README.md` §4 — Bug Report Structure.

---

```markdown
### BUG-NNN — <Short Title>

**Date:** YYYY-MM-DD HH:MM
**Severity:** 🔴 Critical | 🟡 Medium | 🟢 Low
**File:** `path/to/file.ext`
**Function:** `functionName()`
**Discovered by:** <Agent name>

**Symptom:**
- Bullet list of observable symptoms

**Root Cause:**
One paragraph explaining why it happens.

**Impact:**
- What breaks or degrades because of this bug

**Test Case:**
```
Input: ...
Expected: ...
Actual: ...
```

**Fix Required:**
Description of the fix, with code snippets if applicable.

**Status:** ✅ Fixed | ⏳ Open
**Deployed:** YYYY-MM-DD ~HH:MM — <who fixed it>
```

---

## Summary Table (end of file)

| Bug | Severity | Status | Fixed By |
|-----|----------|--------|----------|
