import unittest
from unittest.mock import patch
from src.entity import generate_entity

class TestGenerateEntity(unittest.TestCase):

    def setUp(self):
        self.game_board = {
            (0, 0): None,
            (1, 1): "TreeTrunk",
            (2, 2): "Moss",
        }
        self.character = {"FinalChallengeCompleted": False, "InTree": False}

if __name__ == "__main__":
    unittest.main()
