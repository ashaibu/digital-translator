import unittest

from digital_translator.atm import validate_card


class TestATM(unittest.TestCase):

    def test_accepts_readable_card(self):
        self.assertTrue(validate_card(True))

    def test_rejects_unreadable_card(self):
        self.assertFalse(validate_card(False))


if __name__ == "__main__":
    unittest.main()
