# Exercise 11 — Windowed Metrics

## Objective

Implement:

```python
def count_requests_in_window(
    requests: list[tuple[int, str]],
    start: int,
    end: int,
) -> dict[str, int]:
```

Each request is represented as `(timestamp, service)`.

Return the number of requests for each service whose timestamp falls within the inclusive window `[start, end]`.

## Rules

- Include requests where `timestamp == start` or `timestamp == end`.
- Ignore requests outside the window.
- Preserve service names exactly as provided.
- Services with no requests in the window should not appear.
- Return `{}` when no requests fall in the window.
- `start` and `end` are non-negative integers and `start <= end`.
- Input records are valid.
- Do not modify the input.
- Use only the Python standard library.

## Example

```python
requests = [
    (100, "api"),
    (110, "web"),
    (120, "api"),
    (130, "worker"),
    (140, "api"),
]

count_requests_in_window(requests, 110, 130)
# -> {"web": 1, "api": 1, "worker": 1}
```

Boundary example:

```python
requests = [
    (100, "api"),
    (200, "api"),
    (201, "api"),
]

count_requests_in_window(requests, 100, 200)
# -> {"api": 2}
```

## Before coding

Think about:

1. How do you determine whether a timestamp belongs to the window?
2. What dictionary operation can count repeated services?
3. Do you need to sort the input?
4. Can this be solved in one pass?
5. What are the time and space complexities?

## Assessment focus

This is another short speed exercise. It combines filtering with dictionary aggregation and is intended to build the habit of identifying the simplest possible one-pass solution.
