# Exercise 15 — Top Error Services

Implement:

```python
def top_error_services(logs: list[dict], n: int) -> list[str]:
```

Each record contains `service` and `status`. Count only records with `status >= 500` and return the `n` services with the most errors.

Rules:
- Sort by descending error count.
- For ties, preserve the order in which each service first appears as an error.
- Return each service at most once.
- If `n <= 0`, return `[]`.
- If `n` exceeds the number of services with errors, return all of them.
- Empty input returns `[]`.
- Input records are valid.
- Do not modify the input.
- Standard library only.

Example:

```python
logs = [
    {"service": "api", "status": 500},
    {"service": "web", "status": 503},
    {"service": "api", "status": 502},
    {"service": "worker", "status": 500},
    {"service": "web", "status": 500},
]

# top_error_services(logs, 2)
# -> ["api", "web"]
```

**Focus:** combine filtering, counting, tie-breaking, and sorting. This is a good timed-assessment exercise.
