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

    def create_character(self, extra_energy=0, in_tree=False):
        return {
            "ExtraEnergy": extra_energy,
            "InTree": in_tree,
            "GroundCoordinates": (5, 5),
            "Tummy": 100,
            "TreeCoordinates": (5, 5) if in_tree else None  # Include TreeCoordinates
        }

    @patch('src.character.current_location')
    def test_nap_on_moss_when_in_tree(self, mock_current_location):
        self.character = self.create_character(in_tree=True)  # Character is in a tree
        mock_current_location.return_value = (5, 5)  # Mock location to moss

        result = nap(self.character, self.board)
        print(f"Nap result on moss when in tree: {result}")
        print(f"Extra energy after nap on moss: {self.character['ExtraEnergy']}")

        self.assertTrue(result)
        self.assertEqual(self.character['ExtraEnergy'], NAP_EXTRA_ENERGY)

    @patch('src.character.current_location')
    def test_nap_on_empty(self, mock_current_location):
        self.character = self.create_character(extra_energy=0, in_tree=False)  # Not in tree
        mock_current_location.return_value = (6, 5)  # Mock location to empty

        result = nap(self.character, self.board)
        print(f"Nap result on empty: {result}")
        print(f"Extra energy after nap on empty: {self.character['ExtraEnergy']}")

        self.assertFalse(result)  # Expecting False since it's empty
        self.assertEqual(self.character['ExtraEnergy'], 0)  # Ensure energy remains unchanged

    @patch('src.character.current_location')
    def test_nap_on_moss_when_not_in_tree(self, mock_current_location):
        self.character = self.create_character(in_tree=False)  # Character is not in a tree
        mock_current_location.return_value = (5, 5)  # Mock location to moss

        result = nap(self.character, self.board)
        print(f"Nap result on moss when not in tree: {result}")
        print(f"Extra energy after nap on moss: {self.character['ExtraEnergy']}")

        self.assertFalse(result)  # Expecting False since not in tree
        self.assertEqual(self.character['ExtraEnergy'], 0)  # Ensure energy remains unchanged

if __name__ == '__main__':
    unittest.main()
