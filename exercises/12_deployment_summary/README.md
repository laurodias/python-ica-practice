# Exercise 12 — Deployment Summary

Implement:

```python
def summarize_deployments(deployments: list[dict]) -> dict[str, dict[str, int]]:
```

Each record contains `service`, `environment`, and `success` (`bool`). Return, for each environment, the number of successful and failed deployments:

```python
{"prod": {"success": 3, "failed": 1}}
```

Rules:
- Include every environment that appears.
- `success == True` increments `success`; `False` increments `failed`.
- Preserve environment names exactly.
- Empty input returns `{}`.
- Input records are valid.
- Do not modify the input.
- Standard library only.

Before coding, think about the nested dictionary structure and whether you need to track the service field at all.

**Focus:** nested dictionary aggregation, one-pass processing, identifying irrelevant data.
