import unittest
from unittest.mock import patch, MagicMock
from src.ui import help_animal

class TestHelpAnimal(unittest.TestCase):

    def setUp(self):
        self.character = {
            "Level": 1,
            "Inventory": {
                "Red": 2,
                "Blue": 0,
                "Green": 1
            },
            "AnimalsHelped": 0,
            "UntilNextLevel": 5
        }
        self.animal = {
            "Name": "Mouse 🐁",
            "Ailments": ["Fever", "Cough"]
        }
        self.final_challenge = {
            "Name": "FinalChallenge",
            "Ailments": ["Mystery"]
        }


if __name__ == '__main__':
    unittest.main()
