# Exercise 07 — Dependency Resolution

## Objective

Implement:

```python
def resolve_startup_order(services: dict[str, list[str]]) -> list[str]:
```

Given a mapping where each service lists the services it depends on, return a valid order in which all services can be started.

A service may start only after all of its dependencies have started.

## Requirements

- Return every service exactly once.
- A service with no dependencies can appear first.
- If multiple valid orders exist, any valid order is acceptable.
- Dependencies may refer to services that are not keys in the input. Treat those dependency names as services that also need to be included in the result, with no dependencies of their own.
- If the dependency graph contains a cycle, return an empty list.
- An empty input returns an empty list.
- Do not modify the input.
- Use only the Python standard library.

## Examples

```python
resolve_startup_order({
    "api": ["db", "cache"],
    "worker": ["db"],
    "db": [],
    "cache": [],
})
# A valid answer could be:
# ["db", "cache", "api", "worker"]
```

```python
resolve_startup_order({
    "api": ["db"],
    "db": [],
})
# -> ["db", "api"]
```

Dependencies not explicitly defined:

```python
resolve_startup_order({
    "api": ["external-db"],
})
# -> ["external-db", "api"]
```

Cycle:

```python
resolve_startup_order({
    "api": ["db"],
    "db": ["api"],
})
# -> []
```

## Assessment focus

This exercise is about algorithm design rather than Python syntax. Think about:

1. How to represent the dependency state.
2. How to identify services that are ready to start.
3. How to detect that progress is impossible because of a cycle.
4. What the time and space complexity of your approach will be.

Try to design the algorithm on paper before coding.

## Suggested thinking questions

- What does it mean for a service to be "ready"?
- If `api` depends on `db` and `cache`, what needs to happen before `api` can be added to the result?
- How can you keep track of dependencies that have already been satisfied?
- How would you know that a cycle exists without explicitly searching for the word `cycle`?

## Constraints

- No third-party libraries.
- Keep the function self-contained.
- Preserve the input data.
