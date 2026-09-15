# Python ICA Practice

A focused practice environment for Python coding assessments, with an emphasis on ICA/CodeSignal-style problems.

## Goal

Build speed, correctness, edge-case awareness, and clean Python implementation under assessment-style constraints.

## Structure

- `exercises/` — problems to solve
- `tests/` — automated tests
- `solutions/` — reference solutions (added later; do not look here during timed practice)
- `run_ica.py` — local ICA-style test runner

## Local validation

The test runner loads the `solution.py` from your local working tree, so you can test code before committing it.

```bash
python run_ica.py 10
python run_ica.py 10 11 12
python run_ica.py --all
```

Exercise 07 is intentionally excluded because it is currently parked.

## Practice rules

1. Read the problem carefully before coding.
2. Start with a simple correct approach.
3. Consider edge cases before submitting.
4. Be prepared to explain time and space complexity.
5. During simulation exercises, avoid looking at solutions or searching for the exact problem.

Exercises will progress from Python/data-structure fundamentals toward realistic data-processing and SRE/DevOps-oriented problems.
