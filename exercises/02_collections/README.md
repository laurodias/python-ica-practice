# Exercise 02 — Frequency Analysis

## Objective

Analyze application log messages and identify the most common error.

## Requirements

Implement `most_common_error(logs)` in `solution.py`.

Each log message has this format:

```text
<LEVEL> <MESSAGE>
```

For example:

```text
INFO Application started
ERROR Database connection failed
WARNING High memory usage
ERROR Database connection failed
ERROR Timeout connecting to Redis
```

The function must:

1. Consider only entries whose level is exactly `ERROR`.
2. Extract the complete message after `ERROR `.
3. Return the error message that occurs most frequently.
4. If multiple error messages have the same highest frequency, return the first one that reached that frequency.
5. Return `None` if there are no `ERROR` entries.

## Examples

```python
logs = [
    "INFO Application started",
    "ERROR Database connection failed",
    "WARNING High memory usage",
    "ERROR Database connection failed",
    "ERROR Timeout connecting to Redis",
]

most_common_error(logs)
# "Database connection failed"
```

Tie handling:

```python
logs = [
    "ERROR Disk full",
    "ERROR Network timeout",
    "ERROR Network timeout",
    "ERROR Disk full",
]

most_common_error(logs)
# "Disk full"
```

Both messages occur twice, but `Disk full` reached the highest frequency first.

```python
most_common_error([])
# None
```

## Constraints

- Do not use third-party libraries.
- The input may contain thousands of log entries.
- Do not assume the error messages are known in advance.
- Preserve the exact error message; do not modify its casing.
- Aim for a single pass through the logs.

## Assessment mindset

Before coding, decide what data structure should track frequencies and how you will preserve the required tie-breaking behavior.
