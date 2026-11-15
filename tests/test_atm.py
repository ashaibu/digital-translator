import unittest

from digital_translator.atm import validate_card
from digital_translator.atm import validate_card, verify_pin


class TestATM(unittest.TestCase):

    def test_accepts_readable_card(self):
        self.assertTrue(validate_card(True))

    def test_rejects_unreadable_card(self):
        self.assertFalse(validate_card(False))

    def test_accepts_correct_pin(self):
        self.assertTrue(verify_pin("1234", "1234"))

    def test_rejects_incorrect_pin(self):
        self.assertFalse(verify_pin("5678", "1234"))


if __name__ == "__main__":
    unittest.main()
