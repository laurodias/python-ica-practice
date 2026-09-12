# Exercise 10 — Log Summary

## Objective

Implement:

```python
def summarize_logs(logs: list[str]) -> dict[str, int]:
```

Each log line has the format:

```text
<TIMESTAMP> <LEVEL> <SERVICE>
```

where `LEVEL` is one of `INFO`, `WARN`, or `ERROR`.

Return a dictionary containing the number of `ERROR` events for each service.

## Rules

- Count only records whose level is exactly `ERROR`.
- The service name is the third field.
- Ignore non-ERROR records.
- Preserve service names exactly as provided.
- If a service has no errors, it should not appear in the result.
- Return `{}` when there are no errors.
- Input lines are valid.
- Do not modify the input.
- Use only the Python standard library.

## Example

```python
logs = [
    "100 INFO api",
    "110 ERROR api",
    "120 ERROR web",
    "130 WARN api",
    "140 ERROR api",
    "150 ERROR web",
]

summarize_logs(logs)
# -> {"api": 2, "web": 2}
```

## Another example

```python
logs = [
    "100 INFO api",
    "110 WARN web",
]

# -> {}
```

## Before coding

Think about:

1. What dictionary structure do you need?
2. What fields do you need from each line?
3. When should a service be added to the dictionary?
4. Can this be solved in one pass?
5. What are the time and space complexities?

## Assessment focus

This is a deliberately short exercise. The objective is speed and confidence with parsing plus dictionary counting. Aim to solve it quickly and cleanly.
