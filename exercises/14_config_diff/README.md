# Exercise 14 — Configuration Diff

Implement:

```python
def changed_settings(old: dict[str, str], new: dict[str, str]) -> list[str]:
```

Return the names of settings whose value changed between `old` and `new`.

Also treat a setting that exists in only one dictionary as changed.

Rules:
- Return each changed setting name once.
- Return names in alphabetical order.
- Unchanged settings are excluded.
- Empty dictionaries are valid.
- Do not modify either input dictionary.
- Standard library only.

Example:

```python
old = {"region": "eu-west-1", "replicas": "3", "debug": "false"}
new = {"region": "eu-west-1", "replicas": "5", "timeout": "30"}

# -> ["debug", "replicas", "timeout"]
```

**Focus:** sets/dictionary keys, comparing two data sets, sorting the final result.
