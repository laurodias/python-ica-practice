# Exercise 04 — Interval Analysis

## Problem

Implement:

```python
def find_overlapping_intervals(intervals: list[tuple[int, int]]) -> bool:
```

You are given a list of time intervals. Each interval is represented as:

```text
(start, end)
```

Return `True` if **any two intervals overlap**, otherwise return `False`.

### Rules

- `start` is the beginning of the interval and `end` is the end.
- Intervals that only touch at a boundary do **not** count as overlapping.
  - `(10, 20)` and `(20, 30)` → `False`
- The input list may be unsorted.
- You may assume `start < end` for every interval.
- An empty list or a list with one interval returns `False`.
- Do not modify the input list.
- Do not use third-party libraries.

### Examples

```python
find_overlapping_intervals([
    (10, 20),
    (30, 40),
    (15, 25),
])
# -> True
```

```python
find_overlapping_intervals([
    (10, 20),
    (20, 30),
    (30, 40),
])
# -> False
```

```python
find_overlapping_intervals([
    (30, 40),
    (10, 20),
    (50, 60),
])
# -> False
```

### Before coding

Think about:

1. Does the order of the intervals matter?
2. What operation might make the problem easier to reason about?
3. What is the time complexity of your approach?
4. What is the space complexity?

## Assessment focus

This exercise introduces **sorting as a problem-solving technique** rather than simply using it to produce an ordered result.

There is a straightforward solution that should be achievable with the Python tools you already know. Don't worry about advanced interval algorithms or optimizing prematurely.
