import unittest
from unittest import TestCase

from src.action import direction_input_to_action


class TestDirectionInputToAction(TestCase):

    def test_direction_input_to_action_w_upper_case(self):
        actual = direction_input_to_action("W")
        expected = {
            "Type": "Move",
            "Data": (0, -1)
        }
        self.assertEqual(expected, actual)

    def test_direction_input_to_action_w_lower_case(self):
        actual = direction_input_to_action("w")
        expected = {
            "Type": "Move",
            "Data": (0, -1)
        }
        self.assertEqual(expected, actual)

    def test_direction_input_to_action_a_upper_case(self):
        actual = direction_input_to_action("A")
        expected = {
            "Type": "Move",
            "Data": (-1, 0)
        }
        self.assertEqual(expected, actual)

    def test_direction_input_to_action_a_lower_case(self):
        actual = direction_input_to_action("a")
        expected = {
            "Type": "Move",
            "Data": (-1, 0)
        }
        self.assertEqual(expected, actual)

    def test_direction_input_to_action_s_upper_case(self):
        actual = direction_input_to_action("S")
        expected = {
            "Type": "Move",
            "Data": (0, 1)
        }
        self.assertEqual(expected, actual)

    def test_direction_input_to_action_s_lower_case(self):
        actual = direction_input_to_action("s")
        expected = {
            "Type": "Move",
            "Data": (0, 1)
        }
        self.assertEqual(expected, actual)

    def test_direction_input_to_action_d_upper_case(self):
        actual = direction_input_to_action("D")
        expected = {
            "Type": "Move",
            "Data": (1, 0)
        }
        self.assertEqual(expected, actual)

    def test_direction_input_to_action_d_lower_case(self):
        actual = direction_input_to_action("d")
        expected = {
            "Type": "Move",
            "Data": (1, 0)
        }
        self.assertEqual(expected, actual)

    def test_direction_input_to_action_invalid_direction_input(self):
        with self.assertRaises(ValueError) as context:
            direction_input_to_action("X")
        self.assertEqual("Invalid direction input", str(context.exception))

if __name__ == '__main__':
    unittest.main()
