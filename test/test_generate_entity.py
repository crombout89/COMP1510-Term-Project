import unittest
from unittest.mock import patch
from src.entity import generate_entity
from src.config import AILMENT_OPTIONS


class TestGenerateEntity(unittest.TestCase):

    def setUp(self):
        self.game_board = {
            (0, 0): None,
            (1, 1): "TreeTrunk",
            (2, 2): "Moss",
        }
        self.character = {
            "FinalChallengeCompleted": False,
            "InTree": False,
            "GroundCoordinates": (0, 0)  # Add this key to match expected structure
        }

    @patch('random.randint')
    @patch('src.entity.generate_animal')
    @patch('src.entity.generate_item')
    def test_generate_final_challenge_entity(self, mock_generate_item, mock_generate_animal, mock_randint):
        """Test that the final challenge entity is generated correctly."""
        mock_randint.return_value = 1  # Not used here, but just for safety
        entity = generate_entity(self.game_board, self.character)
        self.assertEqual(entity["Type"], "Animal")
        self.assertEqual(entity["Name"], "FinalChallenge")
        self.assertEqual(len(entity["Data"]), (len(AILMENT_OPTIONS) - 1) * 2)  # Two of each ailment except "Starving"

    @patch('random.randint')
    @patch('src.entity.generate_animal')
    @patch('src.entity.generate_item')
    def test_no_entity_generated_on_tree_trunk(self, mock_generate_item, mock_generate_animal, mock_randint):
        """Test that no entity is generated on TreeTrunk."""
        self.character["FinalChallengeCompleted"] = False
        self.character["GroundCoordinates"] = (1, 1)  # Set location to TreeTrunk
        mock_randint.return_value = 2  # Ensure not generating an animal
        entity = generate_entity(self.game_board, self.character)
        self.assertIsNone(entity)

    @patch('random.randint')
    @patch('src.entity.generate_animal')
    @patch('src.entity.generate_item')
    def test_no_entity_generated_on_moss(self, mock_generate_item, mock_generate_animal, mock_randint):
        """Test that no entity is generated on Moss."""
        self.character["FinalChallengeCompleted"] = False
        self.character["GroundCoordinates"] = (2, 2)  # Set location to Moss
        mock_randint.return_value = 2  # Ensure not generating an animal
        entity = generate_entity(self.game_board, self.character)
        self.assertIsNone(entity)

    @patch('random.randint')
    @patch('src.entity.generate_animal')
    @patch('src.entity.generate_item')
    def test_generate_animal(self, mock_generate_item, mock_generate_animal, mock_randint):
        """Test that an animal is generated correctly."""
        self.character["FinalChallengeCompleted"] = False
        self.character["GroundCoordinates"] = (0, 1)  # Set location to a valid position
        mock_randint.return_value = 1  # Force animal generation
        mock_generate_animal.return_value = {"Type": "Animal", "Name": "Raccoon", "Data": []}

        entity = generate_entity(self.game_board, self.character)
        self.assertEqual(entity["Type"], "Animal")
        self.assertEqual(entity["Name"], "Raccoon")

    @patch('random.randint')
    @patch('src.entity.generate_animal')
    @patch('src.entity.generate_item')
    def test_generate_item(self, mock_generate_item, mock_generate_animal, mock_randint):
        """Test that an item is generated correctly."""
        self.character["FinalChallengeCompleted"] = False
        self.character["GroundCoordinates"] = (0, 1)  # Set location to a valid position
        mock_randint.return_value = 2  # Force item generation
        mock_generate_item.return_value = {"Type": "Item", "Name": "Berry", "Data": "Red"}

        entity = generate_entity(self.game_board, self.character)
        self.assertEqual(entity["Type"], "Item")
        self.assertEqual(entity["Name"], "Berry")

    @patch('random.randint')
    def test_no_entity_generated_if_final_challenge_completed(self, mock_randint):
        """Test that no entity is generated if the final challenge has been completed."""
        self.character["FinalChallengeCompleted"] = True
        entity = generate_entity(self.game_board, self.character)
        self.assertIsNone(entity)


if __name__ == '__main__':
    unittest.main()
