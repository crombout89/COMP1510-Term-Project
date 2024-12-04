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


if __name__ == '__main__':
    unittest.main()