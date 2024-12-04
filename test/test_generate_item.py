import unittest
from unittest.mock import patch
from src.entity import generate_item
from src.config import BERRY_COLOR_OPTIONS

class TestGenerateItem(unittest.TestCase):

    def setUp(self):
        self.character_in_tree = {"InTree": True}
        self.character_not_in_tree = {"InTree": False}

    @patch('random.randint')
    def test_generate_silvervine(self, mock_randint):
        mock_randint.return_value = 1  # Force Silvervine to be generated
        item = generate_item(self.character_in_tree)
        self.assertEqual(item["Type"], "Item")
        self.assertEqual(item["Name"], "Silvervine")
        self.assertIsNone(item["Data"])

    @patch('random.randint')
    def test_generate_catnip(self, mock_randint):
        mock_randint.side_effect = [3, 1]  # Force Catnip to be generated
        item = generate_item(self.character_in_tree)
        self.assertEqual(item["Type"], "Item")
        self.assertEqual(item["Name"], "Catnip")
        self.assertIsNone(item["Data"])

    @patch('random.randint')
    @patch('random.choice')
    def test_generate_berry(self, mock_choice, mock_randint):
        mock_randint.side_effect = [5, 5, 1]  # Force Berry generation
        mock_choice.return_value = "Red"  # Force Berry color to Red
        item = generate_item(self.character_in_tree)
        self.assertEqual(item["Type"], "Item")
        self.assertEqual(item["Name"], "Berry")
        self.assertEqual(item["Data"], "Red")

    @patch('random.randint')
    def test_no_item_generated(self, mock_randint):
        mock_randint.side_effect = [3, 3, 5]  # Ensure no item is generated
        item = generate_item(self.character_not_in_tree)
        self.assertIsNone(item)

    @patch('random.randint')
    def test_always_generate_berry(self, mock_randint):
        mock_randint.side_effect = [5, 5]  # Force Berry generation
        item = generate_item(self.character_not_in_tree, always=True)
        self.assertEqual(item["Type"], "Item")
        self.assertEqual(item["Name"], "Berry")
        self.assertIn(item["Data"], BERRY_COLOR_OPTIONS)

if __name__ == '__main__':
    unittest.main()
