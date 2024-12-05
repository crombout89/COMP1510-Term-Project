import unittest
from unittest.mock import patch, MagicMock
from src.ui import get_action_input
from src.action import eat, nap


class TestActionInput(unittest.TestCase):

    def setUp(self):
        self.character = {
            "Position": (0, 0),
            "Tummy": 50,
            "ExtraEnergy": 0,
            "Inventory": ["Catnip", "Silvervine"],
            "Level": 2
        }
        self.board = {
            "Tiles": [["Grass", "Moss"], ["Tree", "Rock"]]
        }

    @patch('builtins.input', side_effect=["W"])
    def test_move_action_up(self, mock_input):
        action = get_action_input(self.character, self.board)
        self.assertEqual(action, {'Data': (0, -1), 'Type': 'Move'})

    @patch('builtins.input', side_effect=["A"])
    def test_move_action_left(self, mock_input):
        action = get_action_input(self.character, self.board)
        self.assertEqual(action, {'Data': (-1, 0), 'Type': 'Move'})

    @patch('builtins.input', side_effect=["S"])
    def test_move_action_down(self, mock_input):
        action = get_action_input(self.character, self.board)
        self.assertEqual(action, {'Data': (0, 1), 'Type': 'Move'})

    @patch('builtins.input', side_effect=["D"])
    def test_move_action_right(self, mock_input):
        action = get_action_input(self.character, self.board)
        self.assertEqual(action, {'Data': (1, 0), 'Type': 'Move'})

    @patch('src.action.eat')  # Mock the eat function
    def test_eat_action(self, mock_eat):
        with patch('builtins.input', side_effect=['Eat Catnip']):
            action = get_action_input(self.character, self.board)

        self.assertEqual(action["Type"], "Eat")
        self.assertEqual(action["Data"], ["Catnip"])
        mock_eat.assert_called_once()  # Check if eat was called with the correct item


if __name__ == '__main__':
    unittest.main()