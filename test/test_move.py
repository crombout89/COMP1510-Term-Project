import unittest
from unittest.mock import patch
from src.action import move
import src.config
from src.character import subtract_from_tummy

class TestMoveFunction(unittest.TestCase):

    def setUp(self):
        self.character = {
            "InTree": False,
            "GroundCoordinates": (5, 5),
            "Tummy": 50,
            "ExtraEnergy": 2
        }
        self.board = {
            (5, 5): "Empty",         # Current position
            (6, 5): "Empty",         # Valid move right
            (5, 6): "TreeTrunk",     # Invalid move down
            (4, 5): "Empty",         # Valid move left
            (5, 4): "Empty"          # Valid move up
        }

    def test_move_valid_right_return__value(self):
        result = move(self.character, self.board, (1, 0))
        self.assertTrue(result)

    def test_move_valid_right_coordinate_change(self):
        move(self.character, self.board, (1, 0))
        actual = self.character["GroundCoordinates"]
        expected = (6, 5)
        self.assertEqual(actual, expected)

    @patch('src.character.subtract_from_tummy')
    def test_move_valid_right_subtract_from_tummy_called(self, mock_subtract):
        move(self.character, self.board, (1, 0))
        mock_subtract.assert_called_once_with(self.character, src.config.SUBTRACT_FROM_TUMMY_IF_MOVE)

    @patch('src.character.subtract_from_tummy')
    def test_move_invalid_tree(self, mock_subtract):
        result = move(self.character, self.board, (0, 1))
        self.assertFalse(result)
        actual = self.character["GroundCoordinates"]
        expected = (5, 5)
        self.assertEqual(expected, actual)
        mock_subtract.assert_not_called()

    @patch('src.character.subtract_from_tummy')
    def test_move_valid_left(self, mock_subtract):
        result = move(self.character, self.board, (-1, 0))
        self.assertTrue(result)
        actual = self.character["GroundCoordinates"]
        expected = (4, 5)
        self.assertEqual(expected, actual)
        mock_subtract.assert_called_once_with(self.character, src.config.SUBTRACT_FROM_TUMMY_IF_MOVE)

    @patch('src.character.subtract_from_tummy')
    def test_move_valid_up(self, mock_subtract):
        result = move(self.character, self.board, (0, -1))
        self.assertTrue(result)
        actual = self.character["GroundCoordinates"]
        expected = (5, 4)
        self.assertEqual(expected, actual)
        mock_subtract.assert_called_once_with(self.character, src.config.SUBTRACT_FROM_TUMMY_IF_MOVE)

    @patch('src.character.subtract_from_tummy')
    def test_move_valid_down(self, mock_subtract):
        result = move(self.character, self.board, (0, 1))
        self.assertTrue(result)
        actual = self.character["GroundCoordinates"]
        expected = (5, 6)
        self.assertEqual(expected, actual)
        mock_subtract.assert_called_once_with(self.character, src.config.SUBTRACT_FROM_TUMMY_IF_MOVE)

    @patch('src.character.subtract_from_tummy')
    def test_move_out_of_bounds(self, mock_subtract):
        self.board[(16, 15)] = None  # Assume that (16, 15) is out of bounds
        result = move(self.character, self.board, (1, 0))
        self.assertFalse(result)
        actual = self.character["GroundCoordinates"]
        expected = (5, 5)
        self.assertEqual(expected, actual)
        mock_subtract.assert_not_called()

    @patch('src.character.subtract_from_tummy')
    def test_move_in_tree(self, mock_subtract):
        self.character["InTree"] = True
        self.character["TreeCoordinates"] = [0, 0]
        result = move(self.character, self.board, (1, 0))
        self.assertTrue(result)
        actual = self.character["GroundCoordinates"]
        expected = (1, 0)
        self.assertEqual(expected, actual)
        mock_subtract.assert_called_once_with(self.character, src.config.SUBTRACT_FROM_TUMMY_IF_MOVE)


if __name__ == '__main__':
    unittest.main()
