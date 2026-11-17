
import unittest

from digital_translator.atm import (
    validate_card,
    verify_pin,
    check_balance,
    check_atm_cash,
    withdraw_cash,
    handle_dispensing_result,
    process_withdrawal,
)


class TestATM(unittest.TestCase):

    def test_accepts_readable_card(self):
        self.assertTrue(validate_card(True))

    def test_rejects_unreadable_card(self):
        self.assertFalse(validate_card(False))

    def test_accepts_correct_pin(self):
        result = verify_pin("1234", "1234")
        self.assertEqual(result, (True, False, 0))

    def test_allows_retry_after_wrong_pin(self):
        result = verify_pin("5678", "1234", attempts=0)
        self.assertEqual(result, (False, False, 1))

    def test_blocks_card_after_third_wrong_pin(self):
        result = verify_pin("5678", "1234", attempts=2)
        self.assertEqual(result, (False, True, 3))

    def test_accepts_sufficient_balance(self):
        self.assertTrue(check_balance(50000, 20000))

    def test_rejects_insufficient_balance(self):
        self.assertFalse(check_balance(10000, 25000))

    def test_accepts_sufficient_atm_cash(self):
        self.assertTrue(check_atm_cash(50000, 20000))

    def test_rejects_insufficient_atm_cash(self):
        self.assertFalse(check_atm_cash(10000, 25000))

    def test_successful_withdrawal(self):
        result = withdraw_cash(100000, 50000, 20000)
        self.assertEqual(result, (True, 80000, 30000))

    def test_rejects_insufficient_account_balance(self):
        result = withdraw_cash(10000, 50000, 20000)
        self.assertEqual(result, (False, 10000, 50000))

    def test_rejects_withdrawal_when_atm_cash_is_insufficient(self):
        result = withdraw_cash(100000, 10000, 20000)
        self.assertEqual(result, (False, 100000, 10000))

    def test_restores_both_balances_when_cash_is_not_dispensed(self):
        result = handle_dispensing_result(80000, 30000, 20000, False)
        self.assertEqual(result, (False, 100000, 50000))

    def test_keeps_both_deductions_when_cash_is_dispensed(self):
        result = handle_dispensing_result(80000, 30000, 20000, True)
        self.assertEqual(result, (True, 80000, 30000))


    def test_complete_successful_withdrawal(self):
        result = process_withdrawal(
            True,
            ["1234"],
            "1234",
            100000,
            50000,
            20000,
            True
        )

        self.assertEqual(result, "Withdrawal successful.")

if __name__ == "__main__":
    unittest.main()


