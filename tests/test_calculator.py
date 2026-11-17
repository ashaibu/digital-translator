import unittest

from digital_translator.calculator import calculate


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        result = calculate(10, "add", 5)
        self.assertEqual(result, 15)

    def test_subtraction(self):
        result = calculate(20, "subtract", 5)
        self.assertEqual(result, 15)

    def test_multiplication(self):
        result = calculate(8, "multiply", 5)
        self.assertEqual(result, 40)

    def test_division(self):
        result = calculate(20, "divide", 5)
        self.assertEqual(result, 4)

    def test_division_by_zero(self):
        result = calculate(20, "divide", 0)
        self.assertEqual(result, "cannot divide by zero")

    def test_invalid_operator(self):
        result = calculate(10, "power", 2)
        self.assertEqual(result, "Invalid operator.")