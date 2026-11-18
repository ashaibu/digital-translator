
import unittest
import json
import os
import tempfile
from pathlib import Path
from unittest.mock import patch

from digital_translator.store import (
    validate_customer,
    validate_product,
    validate_quantity,
    calculate_total,
    process_order,
    save_order,
    display_confirmation,
    place_order,
)


class TestStore(unittest.TestCase):

    def setUp(self):
        self.products = {
            "laptop": 450000,
            "phone": 250000,
            "tablet": 180000,
        }

    # Customer validation
    def test_accepts_valid_customer(self):
        self.assertTrue(validate_customer("Victor", "08012345678"))

    def test_rejects_missing_customer_name(self):
        self.assertFalse(validate_customer("", "08012345678"))

    def test_rejects_missing_phone(self):
        self.assertFalse(validate_customer("Victor", ""))

    # Product validation
    def test_accepts_available_product(self):
        self.assertTrue(validate_product("laptop", self.products))

    def test_rejects_unavailable_product(self):
        self.assertFalse(validate_product("camera", self.products))

    # Quantity validation
    def test_accepts_valid_quantity(self):
        self.assertTrue(validate_quantity(3))

    def test_rejects_zero_quantity(self):
        self.assertFalse(validate_quantity(0))

    def test_rejects_negative_quantity(self):
        self.assertFalse(validate_quantity(-2))

    def test_rejects_text_quantity(self):
        self.assertFalse(validate_quantity("three"))

    def test_rejects_boolean_quantity(self):
        self.assertFalse(validate_quantity(True))

    # Total calculation
    def test_calculates_total(self):
        self.assertEqual(calculate_total(450000, 3), 1350000)

    # Order processing
    def test_processes_valid_order(self):
        result = process_order(
            "Victor", "08012345678", "laptop", 3, self.products
        )

        self.assertIsInstance(result, dict)
        self.assertEqual(result["total"], 1350000)

    def test_rejects_invalid_customer_order(self):
        result = process_order(
            "", "08012345678", "laptop", 3, self.products
        )
        self.assertEqual(result, "Invalid customer information.")

    def test_rejects_unavailable_product_order(self):
        result = process_order(
            "Victor", "08012345678", "camera", 3, self.products
        )
        self.assertEqual(result, "Product not available")

    def test_rejects_invalid_quantity_order(self):
        result = process_order(
            "Victor", "08012345678", "laptop", 0, self.products
        )
        self.assertEqual(result, "Invalid quantity")

    # Order storage
    def test_saves_order_to_json(self):
        order = {
            "customer_name": "Victor",
            "phone": "08012345678",
            "product": "laptop",
            "quantity": 3,
            "unit_price": 450000,
            "total": 1350000,
        }

        original_directory = os.getcwd()

        try:
            with tempfile.TemporaryDirectory() as temporary_directory:
                os.chdir(temporary_directory)
                Path("data").mkdir()

                result = save_order(order)

                self.assertTrue(result)

                saved_orders = json.loads(
                    Path("data/orders.json").read_text()
                )

                self.assertEqual(saved_orders, [order])
        finally:
            os.chdir(original_directory)

    # Confirmation
    def test_displays_order_confirmation(self):
        order = {
            "customer_name": "Victor",
            "phone": "08012345678",
            "product": "laptop",
            "quantity": 3,
            "unit_price": 450000,
            "total": 1350000,
        }

        from io import StringIO
        from contextlib import redirect_stdout

        output = StringIO()

        with redirect_stdout(output):
            display_confirmation(order)

        self.assertIn("Victor", output.getvalue())
        self.assertIn("₦1,350,000", output.getvalue())

    # Complete order workflow
    @patch("digital_translator.store.display_confirmation")
    @patch("digital_translator.store.save_order")
    def test_completes_valid_order(self, mock_save, mock_display):
        mock_save.return_value = True

        result = place_order(
            "Victor", "08012345678", "laptop", 3, self.products
        )

        self.assertEqual(result, "Order completed successfully.")
        mock_save.assert_called_once()
        mock_display.assert_called_once()

    @patch("digital_translator.store.save_order")
    def test_does_not_save_invalid_order(self, mock_save):
        result = place_order(
            "Victor", "08012345678", "laptop", 0, self.products
        )

        self.assertEqual(result, "Invalid quantity")
        mock_save.assert_not_called()

    @patch("digital_translator.store.display_confirmation")
    @patch("digital_translator.store.save_order")
    def test_does_not_confirm_failed_save(self, mock_save, mock_display):
        mock_save.return_value = False

        result = place_order(
            "Victor", "08012345678", "laptop", 3, self.products
        )

        self.assertEqual(result, "Order could not be saved.")
        mock_display.assert_not_called()


if __name__ == "__main__":
    unittest.main()
