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


if __name__ == '__main__':
    unittest.main()
