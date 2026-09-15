#!/usr/bin/env python3
"""Run ICA-style tests against local exercise solutions.

Usage:
    python run_ica.py 10
    python run_ica.py 1 2 3
    python run_ica.py --all

Exercise 07 is intentionally excluded because it is currently parked.
The runner imports the solution.py that exists in your local working tree,
so uncommitted changes are tested too.
"""

from __future__ import annotations

import argparse
import copy
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_solution(exercise: int):
    path = ROOT / "exercises" / f"{exercise:02d}_*"
    matches = list(ROOT.glob(str(path.relative_to(ROOT))))
    if not matches:
        raise FileNotFoundError(f"Exercise {exercise:02d} not found")

    solution_path = matches[0] / "solution.py"
    if not solution_path.exists():
        raise FileNotFoundError(f"Missing solution.py for exercise {exercise:02d}")

    module_name = f"exercise_{exercise:02d}_solution"
    spec = importlib.util.spec_from_file_location(module_name, solution_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {solution_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ExerciseTest(unittest.TestCase):
    exercise = 0

    @classmethod
    def setUpClass(cls):
        cls.solution = load_solution(cls.exercise)


class Test01(ExerciseTest):
    exercise = 1

    def test_examples_and_edges(self):
        fn = self.solution.count_unique_words
        cases = [
            ("Hello hello world", 2),
            ("hello-world", 2),
            ("Python, python! PYTHON", 1),
            ("123 !!!", 0),
            ("", 0),
        ]
        for text, expected in cases:
            self.assertEqual(fn(text), expected)


class Test02(ExerciseTest):
    exercise = 2

    def test_examples_and_tie(self):
        fn = self.solution.most_common_error
        logs = [
            "INFO started",
            "ERROR connection failed",
            "WARN retrying",
            "ERROR timeout",
            "ERROR connection failed",
        ]
        self.assertEqual(fn(logs), "connection failed")
        self.assertIsNone(fn(["INFO ok", "WARN retry"]))
        self.assertEqual(
            fn(["ERROR first", "ERROR second"]),
            "first",
        )


class Test03(ExerciseTest):
    exercise = 3

    def test_frequency_and_ties(self):
        fn = self.solution.top_n_services
        services = ["api", "web", "api", "worker", "web", "api", "worker"]
        original = services.copy()
        self.assertEqual(fn(services, 2), ["api", "web"])
        self.assertEqual(services, original)
        self.assertEqual(fn(["api", "web", "worker", "web", "worker", "api"], 2), ["api", "web"])
        self.assertEqual(fn(["api", "web"], 0), [])


class Test04(ExerciseTest):
    exercise = 4

    def test_overlap_cases(self):
        fn = self.solution.find_overlapping_intervals
        self.assertTrue(fn([(1, 5), (3, 7)]))
        self.assertTrue(fn([(10, 30), (10, 20)]))
        self.assertFalse(fn([(1, 5), (5, 10)]))
        self.assertFalse(fn([(1, 2), (3, 4)]))
        self.assertFalse(fn([]))


class Test05(ExerciseTest):
    exercise = 5

    def test_validation_cases(self):
        fn = self.solution.find_invalid_services
        services = [
            {"name": "api", "port": 8080, "enabled": True},
            {"name": "", "port": 8080, "enabled": True},
            {"port": 8080, "enabled": False},
            {"name": "worker", "port": 65535, "enabled": True},
            {"name": "cache", "port": 0, "enabled": True},
        ]
        original = copy.deepcopy(services)
        self.assertEqual(fn(services), ["<unknown>", "<unknown>", "cache"])
        self.assertEqual(services, original)


class Test06(ExerciseTest):
    exercise = 6

    def test_outages(self):
        fn = self.solution.find_longest_outage
        self.assertEqual(
            fn([
                "100 api DOWN", "130 api UP",
                "200 web DOWN", "260 web UP",
                "300 api DOWN", "350 api UP",
            ]),
            60,
        )
        self.assertEqual(fn(["200 api UP", "100 api DOWN", "150 api UP"]), 50)
        self.assertEqual(fn(["100 api DOWN", "100 api DOWN", "150 api UP"]), 50)
        self.assertEqual(fn(["100 api DOWN"]), 0)


class Test08(ExerciseTest):
    exercise = 8

    def test_metrics(self):
        fn = self.solution.summarize_service_requests
        requests = [
            {"service": "api", "status": 200, "duration_ms": 120},
            {"service": "api", "status": 500, "duration_ms": 300},
            {"service": "web", "status": 200, "duration_ms": 80},
            {"service": "api", "status": 200, "duration_ms": 150},
            {"service": "web", "status": 503, "duration_ms": 250},
        ]
        original = copy.deepcopy(requests)
        self.assertEqual(fn(requests), {
            "api": {"requests": 3, "errors": 1, "slowest_ms": 300},
            "web": {"requests": 2, "errors": 1, "slowest_ms": 250},
        })
        self.assertEqual(requests, original)


class Test09(ExerciseTest):
    exercise = 9

    def test_downtime(self):
        fn = self.solution.calculate_downtime
        self.assertEqual(fn([(100, "DOWN"), (130, "UP"), (200, "DOWN"), (260, "UP")]), 90)
        self.assertEqual(fn([(150, "UP"), (100, "DOWN"), (200, "DOWN"), (250, "UP")]), 100)
        self.assertEqual(fn([(100, "DOWN"), (110, "DOWN"), (150, "UP"), (160, "UP")]), 50)
        self.assertEqual(fn([(100, "DOWN"), (150, "UP"), (200, "DOWN")]), 50)


class Test10(ExerciseTest):
    exercise = 10

    def test_error_counts(self):
        fn = self.solution.summarize_logs
        logs = [
            "100 INFO api", "110 ERROR api", "120 ERROR web",
            "130 WARN api", "140 ERROR api", "150 ERROR web",
        ]
        self.assertEqual(fn(logs), {"api": 2, "web": 2})
        self.assertEqual(fn(["100 INFO api", "110 WARN web"]), {})


class Test11(ExerciseTest):
    exercise = 11

    def test_window_counts(self):
        fn = self.solution.count_requests_in_window
        requests = [(100, "api"), (110, "web"), (120, "api"), (130, "worker"), (140, "api")]
        self.assertEqual(fn(requests, 110, 130), {"web": 1, "api": 1, "worker": 1})
        self.assertEqual(fn([(100, "api"), (200, "api"), (201, "api")], 100, 200), {"api": 2})
        self.assertEqual(fn(requests, 500, 600), {})


TEST_CLASSES = {
    1: Test01, 2: Test02, 3: Test03, 4: Test04, 5: Test05,
    6: Test06, 8: Test08, 9: Test09, 10: Test10, 11: Test11,
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Run ICA-style tests against local solutions.")
    parser.add_argument("exercises", nargs="*", type=int, help="Exercise numbers to test")
    parser.add_argument("--all", action="store_true", help="Run all available tests")
    args = parser.parse_args()

    if args.all:
        selected = sorted(TEST_CLASSES)
    elif args.exercises:
        selected = args.exercises
    else:
        parser.error("Provide exercise numbers or use --all")

    unknown = [n for n in selected if n not in TEST_CLASSES]
    if unknown:
        parser.error(f"No runner tests configured for: {unknown}. Exercise 07 is parked.")

    suite = unittest.TestSuite()
    for number in selected:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TEST_CLASSES[number]))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
