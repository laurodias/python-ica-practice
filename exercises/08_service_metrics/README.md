# Exercise 08 — Service Metrics

## Objective

Implement:

```python
def summarize_service_requests(requests: list[dict]) -> dict[str, dict[str, int]]:
```

You are given request records from several services. Each record contains:

- `service`: service name
- `status`: HTTP status code
- `duration_ms`: request duration in milliseconds

Return a summary for each service containing:

- `requests`: number of requests
- `errors`: number of requests with status `>= 500`
- `slowest_ms`: duration of the slowest request

## Requirements

- Include every service that appears in the input.
- A service with multiple records should have its values aggregated.
- `errors` counts only status codes `>= 500`.
- `slowest_ms` is the maximum `duration_ms` for that service.
- Preserve the service names exactly as provided.
- Input records are valid and contain all three fields with the expected types.
- Empty input returns `{}`.
- Do not modify the input.
- Use only the Python standard library.

## Example

```python
requests = [
    {"service": "api", "status": 200, "duration_ms": 120},
    {"service": "api", "status": 500, "duration_ms": 300},
    {"service": "web", "status": 200, "duration_ms": 80},
    {"service": "api", "status": 200, "duration_ms": 150},
    {"service": "web", "status": 503, "duration_ms": 250},
]

summarize_service_requests(requests)

# -> {
#     "api": {"requests": 3, "errors": 1, "slowest_ms": 300},
#     "web": {"requests": 2, "errors": 1, "slowest_ms": 250},
# }
```

## Another example

```python
requests = [
    {"service": "worker", "status": 201, "duration_ms": 40},
]

# -> {
#     "worker": {"requests": 1, "errors": 0, "slowest_ms": 40},
# }
```

## Before coding

Think about:

1. What data structure should hold the summary for each service?
2. What should happen when you encounter a service for the first time?
3. How do you update the request count?
4. How do you update the error count only when appropriate?
5. How do you update the maximum duration?
6. Can the whole problem be solved in one pass?
7. What are the time and space complexities?

## Assessment focus

This exercise is intentionally simpler than Exercise 07. The goal is to reinforce **dictionary-based aggregation** and make the pattern feel natural before moving back toward harder algorithmic problems.

Aim for a clear one-pass solution. There is no need to sort the input or use advanced Python features.
