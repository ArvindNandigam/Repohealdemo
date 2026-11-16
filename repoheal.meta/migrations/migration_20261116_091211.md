# RepoHeal Migration Document

**Immutable**: this document is an append-only migration record and must not be modified after creation.
**Repository**: ArvindNandigam/Repohealdemo
**Generated**: 2026-11-16T09:12:04.871605+00:00

---

| Metric | Score |
|--------|------:|
| **Repository Health** | 50/100 |
| **Migration Risk** | 80/100 (HIGH) |
| **Average Confidence** | 1.00 |


---

# Migration Assessment

**Repository**: ArvindNandigam/Repohealdemo
**Generated**: 2026-11-16T09:12:04.871605+00:00
**Overall Health Score**: 50/100
**Migration Risk Score**: 80/100
**Migration Risk Level**: HIGH
**Migration Intelligence Status**: SUCCESS

## Executive Summary

- Critical findings: 0
- Deprecated APIs: 7
- Breaking changes: 0

---

## Dependency Inventory

| Dependency | Installed | Latest | Status | Type |
| --- | --- | --- | --- | --- |
| numpy | 1.21.0 | 2.5.5 | declared | third-party |
| pandas | 1.3.5 | 3.1.1 | declared | third-party |
| requests | 2.25.1 | 2.34.2 | declared | third-party |

---

## Deprecated APIs

### pandas.DataFrame
- Library: pandas
- Installed version: 1.3.5
- Latest version: 3.0.3
- Status: deprecated
- Files using: test_python.py
- Functions using: load_data

### pandas.append
- Library: pandas
- Installed version: 1.3.5
- Latest version: 3.0.3
- Status: deprecated
- Files using: test_python.py
- Functions using: load_data

### pandas.describe
- Library: pandas
- Installed version: 1.3.5
- Latest version: 3.0.3
- Status: deprecated
- Files using: test_python.py
- Functions using: calculate_statistics

### numpy.array
- Library: numpy
- Installed version: 1.21.0
- Latest version: 2.4.6
- Status: deprecated
- Files using: test_python.py
- Functions using: calculate_statistics

### numpy.asscalar
- Library: numpy
- Installed version: 1.21.0
- Latest version: 2.4.6
- Status: deprecated
- Files using: test_python.py
- Functions using: calculate_statistics

### requests.get
- Library: requests
- Installed version: 2.25.1
- Latest version: 2.34.2
- Status: deprecated
- Files using: test_python.py
- Functions using: fetch_remote_data

### requests.json
- Library: requests
- Installed version: 2.25.1
- Latest version: 2.34.2
- Status: deprecated
- Files using: test_python.py
- Functions using: fetch_remote_data

---

## Breaking Changes

### pandas.DataFrame.append
- Library: pandas
- Installed version: 1.3.5
- Latest version: 3.0.3
- Status: at_risk
- Files using: test_python.py
- Functions using: load_data
- Removed in: pandas.concat

---

## Migration Paths
- `pandas.DataFrame` -> `polars.DataFrame` (replaced_by, confidence: 1.00)
- `pandas.DataFrame.append` -> `pandas.concat` (removed_in, confidence: 1.00)
- `pandas.DataFrame.append` -> `pandas.concat` (deprecated_in_favor_of, confidence: 1.00)
- `pandas.append` -> `pandas.concat` (replaced_by, confidence: 1.00)
- `pandas.append` -> `pandas.concat` (deprecated_in_favor_of, confidence: 1.00)
- `pandas.describe` -> `modin.pandas.DataFrame.describe` (replaced_by, confidence: 1.00)
- `numpy.array` -> `numpy.asarray` (replaced_by, confidence: 1.00)
- `numpy.array` -> `numpy-ts.NDArray` (replaced_by, confidence: 1.00)
- `numpy.asscalar` -> `numpy.ndarray.item` (deprecated_in_favor_of, confidence: 1.00)
- `requests.get` -> `responses.get` (replaced_by, confidence: 1.00)
- `requests.json` -> `requests.Response.json` (deprecated_in_favor_of, confidence: 1.00)

---

## Risk Assessment

### pandas.DataFrame
- Risk score: 48/100 (medium)
- Affected files: 1 (100.0%)
- Breaking severity: low
- Replacement confidence: 1.00
- Call chain depth: 1

### pandas.DataFrame.append
- Risk score: 56/100 (medium)
- Affected files: 1 (100.0%)
- Breaking severity: medium
- Replacement confidence: 1.00
- Call chain depth: 1

### pandas.append
- Risk score: 48/100 (medium)
- Affected files: 1 (100.0%)
- Breaking severity: low
- Replacement confidence: 1.00
- Call chain depth: 1

### pandas.describe
- Risk score: 48/100 (medium)
- Affected files: 1 (100.0%)
- Breaking severity: low
- Replacement confidence: 1.00
- Call chain depth: 1

### numpy.array
- Risk score: 49/100 (medium)
- Affected files: 1 (100.0%)
- Breaking severity: low
- Replacement confidence: 1.00
- Call chain depth: 1

### numpy.asscalar
- Risk score: 49/100 (medium)
- Affected files: 1 (100.0%)
- Breaking severity: low
- Replacement confidence: 1.00
- Call chain depth: 1

### requests.get
- Risk score: 51/100 (medium)
- Affected files: 1 (100.0%)
- Breaking severity: low
- Replacement confidence: 1.00
- Call chain depth: 1

### requests.json
- Risk score: 51/100 (medium)
- Affected files: 1 (100.0%)
- Breaking severity: low
- Replacement confidence: 1.00
- Call chain depth: 1

---

## Recommended Actions
- [HIGH] `pandas.DataFrame.append` (confidence: 1.00): Migrate pandas.DataFrame.append with `pandas.concat` to avoid potential breakage. Impacted files: 1
- [HIGH] `requests.get` (confidence: 1.00): Migrate requests.get to avoid potential breakage. Impacted files: 1
- [HIGH] `requests.json` (confidence: 1.00): Migrate requests.json with `requests.Response.json` to avoid potential breakage. Impacted files: 1
- [HIGH] `numpy.array` (confidence: 1.00): Migrate numpy.array to avoid potential breakage. Impacted files: 1
- [HIGH] `numpy.asscalar` (confidence: 1.00): Migrate numpy.asscalar with `numpy.ndarray.item` to avoid potential breakage. Impacted files: 1
- [HIGH] `pandas.DataFrame` (confidence: 1.00): Migrate pandas.DataFrame to avoid potential breakage. Impacted files: 1
- [HIGH] `pandas.append` (confidence: 1.00): Migrate pandas.append with `pandas.concat` to avoid potential breakage. Impacted files: 1
- [HIGH] `pandas.describe` (confidence: 1.00): Migrate pandas.describe to avoid potential breakage. Impacted files: 1
