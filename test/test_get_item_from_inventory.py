from unittest import TestCase

from src.character import get_item_from_inventory


class TestUpdateLevel(TestCase):
    def test_get_item_from_inventory_get_catnip_when_character_has_catnip_return_value(self):
        example_character = {
            "Inventory": {
                "Catnip": 1
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        actual = get_item_from_inventory(example_character, example_item)
        expected = True
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_get_catnip_when_character_has_catnip_inventory_change(self):
        example_character = {
            "Inventory": {
                "Catnip": 1
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        get_item_from_inventory(example_character, example_item)
        actual = example_character["Inventory"]["Catnip"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_get_catnip_when_character_has_no_catnip_return_value(self):
        example_character = {
            "Inventory": {
                "Catnip": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        actual = get_item_from_inventory(example_character, example_item)
        expected = False
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_get_catnip_when_character_has_no_catnip_inventory_change(self):
        example_character = {
            "Inventory": {
                "Catnip": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        get_item_from_inventory(example_character, example_item)
        actual = example_character["Inventory"]["Catnip"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_get_silvervine_when_character_has_silvervine_return_value(self):
        example_character = {
            "Inventory": {
                "Silvervine": 1
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        actual = get_item_from_inventory(example_character, example_item)
        expected = True
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_get_silvervine_when_character_has_silvervine_inventory_change(self):
        example_character = {
            "Inventory": {
                "Silvervine": 1
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        get_item_from_inventory(example_character, example_item)
        actual = example_character["Inventory"]["Silvervine"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_get_silvervine_when_character_has_no_silvervine_return_value(self):
        example_character = {
            "Inventory": {
                "Silvervine": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        actual = get_item_from_inventory(example_character, example_item)
        expected = False
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_get_silvervine_when_character_has_no_silvervine_inventory_change(self):
        example_character = {
            "Inventory": {
                "Silvervine": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        get_item_from_inventory(example_character, example_item)
        actual = example_character["Inventory"]["Silvervine"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_get_berry_when_character_has_berry_return_value(self):
        example_character = {
            "Inventory": {
                "Berries": {
                    "Red": 1
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        actual = get_item_from_inventory(example_character, example_item)
        expected = True
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_get_berry_when_character_has_berry_inventory_change(self):
        example_character = {
            "Inventory": {
                "Berries": {
                    "Red": 1
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        get_item_from_inventory(example_character, example_item)
        actual = example_character["Inventory"]["Berries"]["Red"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_get_berry_when_character_has_no_berry_return_value(self):
        example_character = {
            "Inventory": {
                "Berries": {
                    "Red": 0
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        actual = get_item_from_inventory(example_character, example_item)
        expected = False
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_get_berry_when_character_has_no_berry_inventory_change(self):
        example_character = {
            "Inventory": {
                "Berries": {
                    "Red": 0
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        get_item_from_inventory(example_character, example_item)
        actual = example_character["Inventory"]["Berries"]["Red"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_item_from_inventory_entity_type_not_item(self):
        example_character = {
            "Inventory": {
                "Berries": {
                    "Red": 1
                }
            }
        }
        example_item = {
            "Type": "Animal",
            "Name": "Mouse",
            "Data": ["Starving"]
        }
        with self.assertRaises(TypeError) as context:
            get_item_from_inventory(example_character, example_item)
        self.assertEqual("Expected entity type 'Item', got 'Animal'", str(context.exception))
