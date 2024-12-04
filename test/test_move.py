import unittest
from unittest.mock import patch
from src.action import move
from src.config import SUBTRACT_FROM_TUMMY_IF_MOVE
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
            (5, 5): "Empty",  # Current position
            (6, 5): "Empty",  # Valid move right
            (5, 6): "TreeTrunk",  # Invalid move down
            (4, 5): "Empty",  # Valid move left
            (5, 4): "Empty"  # Valid move up
        }

    @patch('src.character.subtract_from_tummy')
    def test_move_valid_right(self, mock_subtract):
        mock_subtract.side_effect = lambda *args, **kwargs: print(f"Mock called with args: {args}, kwargs: {kwargs}")
        result = move(self.character, self.board, (1, 0))  # Move right

    @patch('src.character.subtract_from_tummy')
    def test_move_valid_left(self, mock_subtract):
        result = move(self.character, self.board, (-1, 0))  # Move left
        self.assertTrue(result)
        self.assertEqual(self.character["GroundCoordinates"], (4, 5))  # Check position after move
        mock_subtract.assert_called_once_with(self.character, SUBTRACT_FROM_TUMMY_IF_MOVE)

    @patch('src.character.subtract_from_tummy')
    def test_move_valid_up(self, mock_subtract):
        result = move(self.character, self.board, (0, -1))  # Move up
        self.assertTrue(result)
        self.assertEqual(self.character["GroundCoordinates"], (5, 4))  # Check position after move
        mock_subtract.assert_called_once_with(self.character, SUBTRACT_FROM_TUMMY_IF_MOVE)

    @patch('src.character.subtract_from_tummy')
    def test_move_invalid_tree(self, mock_subtract):
        result = move(self.character, self.board, (0, 1))  # Attempt to move down into a tree
        self.assertFalse(result)  # Should return False
        self.assertEqual(self.character["GroundCoordinates"], (5, 5))  # Should stay in the same position
        mock_subtract.assert_not_called()  # Should not call subtract_from_tummy

    @patch('src.character.subtract_from_tummy')
    def test_move_out_of_bounds(self, mock_subtract):
        result = move(self.character, self.board, (11, 10))  # Out of bounds move
        self.assertFalse(result)  # Should return False
        self.assertEqual(self.character["GroundCoordinates"], (5, 5))  # Should stay in the same position
        mock_subtract.assert_not_called()  # Should not call subtract_from_tummy


if __name__ == '__main__':
    unittest.main()
