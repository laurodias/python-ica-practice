# Exercise 06 — Log Event State

## Problem

Implement:

```python
def find_longest_outage(events: list[str]) -> int:
```

You are given a list of service events. Each event has the format:

```text
<TIMESTAMP> <SERVICE> <EVENT>
```

where `TIMESTAMP` is an integer representing seconds, and `EVENT` is either `UP` or `DOWN`.

For each service, a `DOWN` event starts an outage and the next `UP` event for that same service ends it.

Return the duration in seconds of the **longest completed outage** across all services.

### Rules

- Events may be provided in any order. You must process them chronologically.
- A service has at most one active outage at a time.
- Ignore an `UP` event if that service is not currently down.
- Ignore a `DOWN` event if that service is already down.
- Ignore outages that never receive a matching `UP` event.
- If there are no completed outages, return `0`.
- Timestamps are non-negative integers.
- Do not modify the input list.
- Do not use third-party libraries.

### Example

```python
events = [
    "100 api DOWN",
    "130 api UP",
    "200 web DOWN",
    "260 web UP",
    "300 api DOWN",
    "350 api UP",
]

# find_longest_outage(events)
# -> 60
```

The completed outages are:

- `api`: 130 - 100 = 30 seconds
- `web`: 260 - 200 = 60 seconds
- `api`: 350 - 300 = 50 seconds

So the longest is `60` seconds.

### Unordered example

```python
events = [
    "200 api UP",
    "100 api DOWN",
    "150 api UP",
]

# find_longest_outage(events)
# -> 50
```

The input is not chronological, so the events must be ordered by timestamp before evaluating the outage.

### Multiple services

```python
events = [
    "10 api DOWN",
    "20 web DOWN",
    "50 api UP",
    "80 web UP",
]

# find_longest_outage(events)
# -> 60
```

## Before coding

Think about:

1. What data structure can track whether each service is currently down?
2. Why do the events need to be sorted?
3. What information needs to be stored when a service goes `DOWN`?
4. What happens when it later goes `UP`?
5. What is the time complexity?
6. What is the space complexity?

## Assessment focus

This exercise introduces **state tracking**: maintaining information about something while processing a sequence of events.

It also combines parsing, dictionaries, sorting, and careful handling of event order. This is deliberately closer to practical SRE/DevOps scripting than the previous exercises.

A straightforward solution is expected. Do not use datetime libraries or build a class for this problem.
