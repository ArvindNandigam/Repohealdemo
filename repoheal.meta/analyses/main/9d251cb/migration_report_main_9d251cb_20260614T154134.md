# RepoHeal Migration Document

**Immutable**: this document is an append-only migration record and must not be modified after creation.
**Repository**: ArvindNandigam/Repohealdemo
**Generated**: 2026-06-14T15:41:48.003232+00:00

---

| Metric | Score |
|--------|------:|
| **Repository Health** | 44/100 |
| **Migration Risk** | 59/100 (MEDIUM) |
| **Average Confidence** | 0.95 |
- ⚠ pandas: failed
- ⚠ numpy: failed
- ⚠ requests: failed


---

# Migration Assessment

**Repository**: ArvindNandigam/Repohealdemo
**Generated**: 2026-06-14T15:41:48.003232+00:00
**Overall Health Score**: 44/100
**Migration Risk Score**: 59/100
**Migration Risk Level**: MEDIUM
**Migration Intelligence Status**: DEGRADED

## Executive Summary

- Critical findings: 0
- Deprecated APIs: 0
- Breaking changes: 1

**Migration Intelligence Status**: DEGRADED
**Note**: Primary intelligence provider had errors, but local fallback provided data.
**Error**: pandas: failed
**Intelligence Source**: local_kb

---

## Intelligence Warnings

- pandas: failed
- numpy: failed
- requests: failed

---

## Dependency Inventory

| Dependency | Installed | Latest | Status | Type |
| --- | --- | --- | --- | --- |
| numpy | 2.4.6 | 2.4.6 | declared | third-party |
| pandas | 3.0.3 | 3.0.3 | declared | third-party |
| requests | 2.34.2 | 2.34.2 | declared | third-party |

---

## Deprecated APIs

None found.

---

## Breaking Changes

### numpy.asscalar
- Library: numpy
- Installed version: 2.4.6
- Latest version: 2.4.6
- Status: breaking
- Files using: test_python.py
- Functions using: calculate_statistics
- Deprecated in: 1.16.0
- Removed in: 1.24.0

---

## Migration Paths
- `numpy.asscalar` -> `numpy.ndarray.item` (deprecated_in_favor_of, confidence: 0.95)

---

## Risk Assessment

### numpy.asscalar
- Risk score: 56/100 (medium)
- Affected files: 1 (50.0%)
- Breaking severity: high
- Replacement confidence: 0.95
- Call chain depth: 1

---

## Recommended Actions
- [HIGH] `numpy.asscalar` (confidence: 0.95): Migrate numpy.asscalar with `numpy.ndarray.item` to avoid potential breakage. Impacted files: 1
