# Exercise 05 — JSON-Style Data Validation

## Problem

Implement:

```python
def find_invalid_services(services: list[dict]) -> list[str]:
```

You are given a list of service configuration records. Each record should contain:

- `name`: a non-empty string
- `port`: an integer between `1` and `65535`
- `enabled`: a boolean

Return a list containing the `name` of every **invalid** service record.

### Validation rules

A record is invalid if **any** of the following is true:

- `name` is missing, is not a string, or is an empty string
- `port` is missing, is not an integer, or is outside `1..65535`
- `enabled` is missing or is not a boolean

### Important details

- If a record is invalid, use its `name` only if the `name` is a non-empty string. Otherwise use the string `"<unknown>"`.
- Preserve the order in which invalid records appear in the input.
- If the same service name appears more than once and multiple records are invalid, include the name each time.
- Do not modify the input list or dictionaries.
- Do not use third-party libraries.
- Return an empty list when all records are valid or when the input is empty.

### Examples

```python
services = [
    {"name": "api", "port": 8080, "enabled": True},
    {"name": "web", "port": 443, "enabled": True},
    {"name": "worker", "port": 70000, "enabled": True},
]

# find_invalid_services(services)
# -> ["worker"]
```

```python
services = [
    {"name": "api", "port": 8080, "enabled": True},
    {"name": "", "port": 8080, "enabled": True},
    {"port": 8080, "enabled": False},
    {"name": "worker", "port": "9000", "enabled": True},
    {"name": "cache", "port": 6379},
]

# find_invalid_services(services)
# -> ["<unknown>", "<unknown>", "worker", "cache"]
```

## Before coding

Think about:

1. How will you validate multiple fields without making the code difficult to follow?
2. What happens when a key is missing?
3. What is the difference between checking a value's type and checking whether it is merely truthy/falsy?
4. What is the time complexity?
5. What is the space complexity?

## Assessment focus

This exercise moves from lists of simple values to **structured data**, similar to configuration or API data you might encounter in SRE/DevOps work.

Focus on defensive handling of missing or malformed data and on writing clear validation logic. There is no need for classes, third-party validation frameworks, or advanced techniques.
