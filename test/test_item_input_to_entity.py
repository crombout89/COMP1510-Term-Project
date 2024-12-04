from unittest import TestCase

from src.ui import item_input_to_entity


class TestItemInputToEntity(TestCase):
    def test_item_input_to_entity_single_element_item(self):
        actual = item_input_to_entity(["Catnip"])
        expected = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        self.assertEqual(expected, actual)
        
    def test_item_input_to_entity_double_element_item(self):
        actual = item_input_to_entity(["Red", "Berry"])
        expected = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        self.assertEqual(expected, actual)

    def test_item_input_to_entity_triple_element_item(self):
        actual = item_input_to_entity(["Red", "Berry", "ThisWillBeIgnored"])
        expected = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        self.assertEqual(expected, actual)

    def test_item_input_to_entity_nonsensical_item(self):
        actual = item_input_to_entity(["British", "Columbia"])
        expected = {
            "Type": "Item",
            "Name": "Columbia",
            "Data": "British"
        }
        self.assertEqual(expected, actual)
