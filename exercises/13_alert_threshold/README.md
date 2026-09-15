# Exercise 13 — Alert Threshold

Implement:

```python
def find_alerting_services(metrics: list[dict], threshold: float) -> list[str]:
```

Each metric record contains `service` and `error_rate`. Return service names whose **average** error rate across all their records is strictly greater than `threshold`.

Rules:
- Calculate one average per service.
- Return each alerting service once.
- Preserve the order in which services first appear in the input.
- A service exactly at the threshold does not alert.
- Empty input returns `[]`.
- Input records are valid.
- Do not modify the input.
- Standard library only.

Before coding, think about what information must be accumulated before an average can be calculated. You do not need to sort anything.

**Focus:** aggregation where the final decision depends on multiple records; separating accumulation from evaluation.
