import unittest
from unittest.mock import patch
from src.action import nap
from src.config import NAP_EXTRA_ENERGY


class TestNapFunctions(unittest.TestCase):

    def setUp(self):
        self.board = {
            (5, 5): "Moss",
            (6, 5): "Empty"
        }

    def create_character(self, extra_energy=0):
        return {
            "ExtraEnergy": extra_energy,
            "InTree": False,
            "GroundCoordinates": (5, 5),
            "Tummy": 100
        }

    @patch('src.character.current_location')
    def test_nap_on_moss(self, mock_current_location):
        self.character = self.create_character()
        mock_current_location.return_value = (5, 5)

        result = nap(self.character, self.board)
        self.assertTrue(result)
        self.assertEqual(self.character['ExtraEnergy'], NAP_EXTRA_ENERGY)

    @patch('src.character.current_location')
    def test_nap_on_empty(self, mock_current_location):
        self.character = self.create_character(extra_energy=0)  # Reset ExtraEnergy
        mock_current_location.return_value = (6, 5)

        result = nap(self.character, self.board)
        self.assertFalse(result)
        self.assertEqual(self.character['ExtraEnergy'], 0)  # Energy should remain unchanged

if __name__ == '__main__':
    unittest.main()
