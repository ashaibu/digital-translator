import unittest

from digital_translator.data_translator import identify_data_type


class TestDataTranslator(unittest.TestCase):

    def test_identifies_integer(self):
        result = identify_data_type(30)
        self.assertEqual(result, "integer")


    def test_identifies_string(self):
        result = identify_data_type("Victor")
        self.assertEqual(result, "string")

    def test_identifies_float(self):
        result = identify_data_type(150000.50)
        self.assertEqual(result, "float")


    def test_identifies_bool(self):
        result = identify_data_type(True)
        self.assertEqual(result, "boolean")


    def test_identifies_false(self):
        result = identify_data_type(False)
        self.assertEqual(result, "boolean")


    def test_identifies_unknown_type(self):
        result = identify_data_type(None)
        self.assertEqual(result, "unknown")
