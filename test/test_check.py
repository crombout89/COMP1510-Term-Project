import unittest
from unittest.mock import patch
from io import StringIO
from src.action import check

class TestCheckFunction(unittest.TestCase):

    def setUp(self):
        self.character = {
            "Tummy": 50,
            "Level": 2,
            "Inventory": ["Catnip", "Silvervine"]
        }

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_tummy(self, mock_stdout):
        check(self.character, "Tummy")
        self.assertEqual(mock_stdout.getvalue().strip(), 'Your tummy level is: 50')

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_level(self, mock_stdout):
        check(self.character, "Level")
        self.assertEqual(mock_stdout.getvalue().strip(), 'Your current level is: 2')

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_inventory(self, mock_stdout):
        check(self.character, "Inventory")
        expected_output = "Your inventory contains:\n - Catnip\n - Silvervine"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_empty_inventory(self, mock_stdout):
        self.character["Inventory"] = []
        check(self.character, "Inventory")
        self.assertEqual(mock_stdout.getvalue().strip(), "Your inventory is empty.")

    def test_check_invalid_attribute(self):
        with self.assertRaises(ValueError) as context:
            check(self.character, "Health")
        self.assertEqual(str(context.exception), "'Health' is not a supported attribute to check.")

    def test_check_nonexistent_attribute(self):
        with self.assertRaises(ValueError) as context:
            check(self.character, "Strength")
        self.assertEqual(str(context.exception), "'Strength' is not a supported attribute to check.")

if __name__ == '__main__':
    unittest.main()
