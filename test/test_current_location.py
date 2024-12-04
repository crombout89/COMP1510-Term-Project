import unittest
from unittest import TestCase

from src.character import current_location


class TestCurrentLocation(TestCase):
    def test_current_location_ground(self):
        example_character = {
            "GroundCoordinates": (1, 2),
            "TreeCoordinates": (3, 4),
            "InTree": False
        }
        actual = current_location(example_character)
        expected = (1, 2)
        self.assertEqual(expected, actual)

    def test_current_location_tree(self):
        example_character = {
            "GroundCoordinates": (1, 2),
            "TreeCoordinates": (3, 4),
            "InTree": True
        }
        actual = current_location(example_character)
        expected = (3, 4)
        self.assertEqual(expected, actual)

    def test_no_coordinates(self):
        example_character = {
            "GroundCoordinates": None,
            "TreeCoordinates": None,
            "InTree": False
        }
        actual = current_location(example_character)
        expected = None
        self.assertEqual(expected, actual)

    def test_only_ground_coordinates(self):
        example_character = {
            "GroundCoordinates": (1, 2),
            "TreeCoordinates": None,
            "InTree": False
        }
        actual = current_location(example_character)
        expected = (1, 2)
        self.assertEqual(expected, actual)

    def test_only_tree_coordinates(self):
        example_character = {
            "GroundCoordinates": None,
            "TreeCoordinates": (3, 4),
            "InTree": True
        }
        actual = current_location(example_character)
        expected = (3, 4)
        self.assertEqual(expected, actual)

    def test_in_tree_with_none_coordinates(self):
        example_character = {
            "GroundCoordinates": None,
            "TreeCoordinates": None,
            "InTree": True
        }
        actual = current_location(example_character)
        expected = None
        self.assertEqual(expected, actual)

    def test_in_tree_with_invalid_coordinates(self):
        example_character = {
            "GroundCoordinates": (1, 2),
            "TreeCoordinates": None,
            "InTree": True
        }
        actual = current_location(example_character)
        expected = None
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()

