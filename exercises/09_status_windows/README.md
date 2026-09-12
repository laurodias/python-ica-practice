# Exercise 09 — Status Windows

## Objective

Implement:

```python
def calculate_downtime(events: list[tuple[int, str]]) -> int:
```

You are given service health events as `(timestamp, status)` tuples. `status` is either `UP` or `DOWN`.

Return the total number of seconds during which the service was known to be `DOWN`.

## Rules

- Events may be unsorted; process them chronologically.
- A `DOWN` event starts downtime.
- The next `UP` event ends downtime.
- Ignore `DOWN` if the service is already down.
- Ignore `UP` if the service is already up.
- Ignore an incomplete final `DOWN` interval (there is no later `UP`).
- If there are no completed downtime intervals, return `0`.
- Timestamps are non-negative integers.
- Do not modify the input.
- Use only the Python standard library.

## Examples

```python
calculate_downtime([
    (100, "DOWN"),
    (130, "UP"),
    (200, "DOWN"),
    (260, "UP"),
])
# -> 90
```

Unsorted input:

```python
calculate_downtime([
    (150, "UP"),
    (100, "DOWN"),
    (200, "DOWN"),
    (250, "UP"),
])
# -> 100
```

Duplicate state changes:

```python
calculate_downtime([
    (100, "DOWN"),
    (110, "DOWN"),
    (150, "UP"),
    (160, "UP"),
])
# -> 50
```

Incomplete final outage:

```python
calculate_downtime([
    (100, "DOWN"),
    (150, "UP"),
    (200, "DOWN"),
])
# -> 50
```

## Before coding

Think about:

1. What variable can represent whether the service is currently down?
2. What information must you remember when `DOWN` occurs?
3. What should happen when `UP` occurs?
4. Why must the events be sorted first?
5. Can you solve this with a single pass after sorting?
6. What are the time and space complexities?

## Assessment focus

This reinforces the state-tracking pattern from Exercise 06, but removes the complication of multiple services. The goal is to make event/state problems feel straightforward and automatic.
