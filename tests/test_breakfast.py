import unittest

from digital_translator.breakfast import create_breakfast_plan


class TestBreakfastPlan(unittest.TestCase):

    def test_returns_a_dictionary(self):
        result = create_breakfast_plan(
            ["frying pan", "toaster", "kettle"]
        )
        self.assertIsInstance(result, dict)

    def test_assumptions_are_not_empty(self):
        result = create_breakfast_plan(
            ["frying pan", "toaster", "kettle"]
        )
        self.assertTrue(result["assumptions"])

    def test_contains_assumptions_and_steps(self):
        result = create_breakfast_plan(
            ["frying pan", "toaster", "kettle"]
        )
        self.assertIn("assumptions", result)
        self.assertIn("steps", result)

    def test_instructions_are_in_order(self):
        result = create_breakfast_plan(
            ["frying pan", "toaster", "kettle"]
        )
        steps = result["steps"]

        self.assertLess(
            steps.index("Boil water in the kettle."),
            steps.index("Prepare the tea in a clean cup.")
        )
        self.assertLess(
            steps.index("Toast two slices of bread using the toaster."),
            steps.index("Fry two eggs until properly cooked.")
        )

    def test_missing_equipment_is_reported(self):
        result = create_breakfast_plan(["toaster"])

        self.assertIn("error", result)
        self.assertEqual(
            result["missing_equipment"],
            ["frying pan", "kettle"]
        )


if __name__ == "__main__":
    unittest.main()
