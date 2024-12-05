import io
import unittest
from unittest import TestCase
from unittest.mock import patch

from src.action import perform_action


class TestPerformAction(TestCase):

    @patch("src.action.move")
    def test_perform_action_move(self, mock_function):
        mock_function.return_value = "move() called"
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        example_character = {
            "TreeCoordinates": (0, 1),
            "GroundCoordinates": (1, 0),
            "InTree": False,
            "Tummy": 100,
            "ExtraEnergy": 0
        }
        example_action = {
            "Type": "Move",
            "Data": (0, -1)
        }
        actual = perform_action(example_character, example_board, example_action)
        expected = "move() called"
        self.assertEqual(expected, actual)

    @patch("src.action.climb")
    def test_perform_action_climb(self, mock_function):
        mock_function.return_value = "climb() called"
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        example_character = {
            "TreeCoordinates": (0, 1),
            "GroundCoordinates": (1, 0),
            "InTree": False,
            "Tummy": 100,
            "ExtraEnergy": 0
        }
        example_action = {
            "Type": "Climb",
            "Data": None
        }
        actual = perform_action(example_character, example_board, example_action)
        expected = "climb() called"
        self.assertEqual(expected, actual)

    @patch("src.action.eat")
    def test_perform_action_eat(self, mock_function):
        mock_function.return_value = "eat() called"
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        example_character = {
            "TreeCoordinates": (0, 1),
            "GroundCoordinates": (1, 0),
            "InTree": False,
            "Tummy": 100,
            "ExtraEnergy": 0
        }
        example_action = {
            "Type": "Eat",
            "Data": {
                "Type": "Item",
                "Name": "Catnip",
                "Data": None
            }
        }
        actual = perform_action(example_character, example_board, example_action)
        expected = "eat() called"
        self.assertEqual(expected, actual)

    @patch("src.action.nap")
    def test_perform_action_nap(self, mock_function):
        mock_function.return_value = "nap() called"
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        example_character = {
            "TreeCoordinates": (0, 1),
            "GroundCoordinates": (1, 0),
            "InTree": False,
            "Tummy": 100,
            "ExtraEnergy": 0
        }
        example_action = {
            "Type": "Nap",
            "Data": None
        }
        actual = perform_action(example_character, example_board, example_action)
        expected = "nap() called"
        self.assertEqual(expected, actual)

    def test_perform_action_nonexistant_action_return_value(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        example_character = {
            "TreeCoordinates": (0, 1),
            "GroundCoordinates": (1, 0),
            "InTree": False,
            "Tummy": 100,
            "ExtraEnergy": 0
        }
        example_action = {
            "Type": "DabOnTheHaters",
            "Data": None
        }
        actual = perform_action(example_character, example_board, example_action)
        expected = False
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_perform_action_nonexistant_action_console_output(self, mock_output):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        example_character = {
            "TreeCoordinates": (0, 1),
            "GroundCoordinates": (1, 0),
            "InTree": False,
            "Tummy": 100,
            "ExtraEnergy": 0
        }
        example_action = {
            "Type": "DabOnTheHaters",
            "Data": None
        }
        perform_action(example_character, example_board, example_action)
        actual = mock_output.getvalue()
        expected = "🚫 You can't perform this action!\n"
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
