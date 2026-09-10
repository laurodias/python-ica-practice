# Exercise 03 — Data Processing

## Problem

Implement:

```python
def top_n_services(services: list[str], n: int) -> list[str]:
```

You are given a list of service names representing deployment events. Return the `n` most frequently deployed services, ordered from most deployments to least deployments.

### Rules

- Service names are case-sensitive and should be treated exactly as provided.
- If two services have the same deployment count, the service that reached that count first should appear first.
- If `n` is greater than the number of distinct services, return all distinct services.
- If `n <= 0`, return an empty list.
- If `services` is empty, return an empty list.
- Do not modify the input list.
- Do not use third-party libraries.

### Example

```python
services = [
    "api",
    "web",
    "api",
    "worker",
    "web",
    "api",
    "worker",
]

# top_n_services(services, 2)
# -> ["api", "web"]
```

### Tie example

```python
services = [
    "api",
    "web",
    "worker",
    "web",
    "worker",
    "api",
]

# All three have 2 deployments.
# "api" reached 2 first, then "web", then "worker".
# top_n_services(services, 2)
# -> ["api", "web"]
```

## Before coding

Think about:

1. What data structure will you use to count deployments?
2. How will you preserve the required tie-breaking order?
3. What is the expected time complexity?
4. What is the expected space complexity?

## Assessment focus

This exercise introduces a small step beyond simple frequency counting. Focus on choosing appropriate Python data structures and explaining your approach before optimizing it.

Do not worry about advanced algorithms yet. A straightforward, correct solution is preferred.
