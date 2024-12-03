from unittest import TestCase

from src.entity import stringify_item


class TestStringifyItem(TestCase):
    def test_stringify_item_berry(self):
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        actual = stringify_item(example_item)
        expected = "Red Berry"
        self.assertEqual(expected, actual)

    def test_stringify_item_not_berry(self):
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        actual = stringify_item(example_item)
        expected = "Silvervine"
        self.assertEqual(expected, actual)

    def test_stringify_item_incorrect_entity_type(self):
        example_item = {
            "Type": "Animal",
            "Name": "Mouse",
            "Data": ["Injured"]
        }
        with self.assertRaises(TypeError) as context:
            stringify_item(example_item)
        self.assertEqual("Expected entity type 'Item', got 'Animal'", str(context.exception))
