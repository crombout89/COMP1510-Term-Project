import unittest
from unittest.mock import patch, MagicMock
from src.ui import get_action_input

class TestActionInput(unittest.TestCase):

    def setUp(self):
        self.character = {
            "Position": (0, 0),
            "Tummy": 50,
            "ExtraEnergy": 0,
            "Inventory": ["Catnip", "Fish"],
            "Level": 2
        }
        self.board = {
            "Tiles": [["Grass", "Moss"], ["Tree", "Rock"]]
        }

    @patch('builtins.input', side_effect=["W"])
    def test_move_action_up(self, mock_input):
        action = get_action_input(self.character, self.board)
        self.assertEqual(action, {'Type': 'Move', 'Data': (0, -1)})

    @patch('builtins.input', side_effect=["A"])
    def test_move_action_left(self, mock_input):
        action = get_action_input(self.character, self.board)
        self.assertEqual(action, {'Type': 'Move', 'Data': (-1, 0)})

    @patch('builtins.input', side_effect=["S"])
    def test_move_action_down(self, mock_input):
        action = get_action_input(self.character, self.board)
        self.assertEqual(action, {'Type': 'Move', 'Data': (0, 1)})

    @patch('builtins.input', side_effect=["D"])
    def test_move_action_right(self, mock_input):
        action = get_action_input(self.character, self.board)
        self.assertEqual(action, {'Type': 'Move', 'Data': (1, 0)})


if __name__ == '__main__':
    unittest.main()