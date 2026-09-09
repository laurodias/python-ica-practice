# Exercise 01 — Normalize and Count Words

## Objective

Implement a function that normalizes a text string and returns the number of distinct words.

## Requirements

Create `count_unique_words(text)` in `solution.py`.

A word is a sequence of alphabetic characters. Matching is case-insensitive.

For example:

```text
"Hello, hello world!" -> 2
```

Ignore punctuation and numbers. Consecutive whitespace has no special meaning.

### Edge cases

- An empty string contains zero words.
- A string containing no alphabetic characters contains zero words.
- Words differing only by case count as the same word.

## Constraints

- Do not use third-party libraries.
- Aim for a single pass over the input where practical.
- Return an `int`.

## Assessment mindset

Before coding, identify the exact definition of a word and consider punctuation, casing, whitespace, and empty input.
