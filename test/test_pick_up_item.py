import unittest
from unittest.mock import patch
from src.entity import pick_up_item


class TestPickUpItem(unittest.TestCase):

    def setUp(self):
        # Set up a character and entities for testing
        self.character = {
            "Inventory": {
                "Catnip": 0,
                "Silvervine": 0,
                "Berries": {
                    "Red": 0,
                    "Green": 0,
                    "Blue": 0,
                    "Yellow": 0,
                    "Purple": 0
                }
            }
        }
        self.valid_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        self.valid_item_silvervine = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        self.valid_item_berry = {
            'Type': 'Item',
            'Name': 'Berries',  # Correct name for the inventory
            'Data': 'Red'  # Data indicating the color
        }
        self.invalid_item_type = {
            "Type": "NotItem",
            "Name": "Stone",
            "Data": None
        }

    @patch('builtins.print')
    def test_pick_up_valid_item(self, mock_print):
        pick_up_item(self.character, self.valid_item)
        self.assertEqual(self.character["Inventory"]["Catnip"], 1)
        mock_print.assert_called_once_with("💼 You picked up a Catnip.")

    @patch('builtins.print')
    def test_pick_up_valid_silvervine(self, mock_print):
        pick_up_item(self.character, self.valid_item_silvervine)
        self.assertEqual(self.character["Inventory"]["Silvervine"], 1)
        mock_print.assert_called_once_with("💼 You picked up a Silvervine.")

    @patch('builtins.print')
    def test_pick_up_berry(self, mock_print):
        pick_up_item(self.character, self.valid_item_berry)
        self.assertEqual(self.character["Inventory"]["Berries"]["Red"], 1)
        mock_print.assert_called_once_with("💼 You picked up a Red berry.")

    def test_invalid_item_type(self):
        with self.assertRaises(TypeError):
            pick_up_item(self.character, self.invalid_item_type)


if __name__ == '__main__':
    unittest.main()
