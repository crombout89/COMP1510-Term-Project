import unittest
from unittest.mock import patch, MagicMock
from src.character import get_item_from_inventory
from src.entity import stringify_item, generate_item
from src.animal import validate_berry, help_animal


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

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["Red"])  # Simulate giving a Red berry
    def test_help_animal_success(self, mock_print):
        with patch('src.character.get_item_from_inventory', return_value=True), \
                patch('src.animal.validate_berry', return_value=True), \
                patch('src.entity.stringify_item', return_value="Red Berry"), \
                patch('src.entity.generate_item', return_value={"Type": "Item", "Name": "Silvervine"}):
            help_animal(self.character, self.animal)

            # Assertions to verify the expected outcomes
            self.assertEqual(self.character["AnimalsHelped"], 1)
            self.assertEqual(self.character["UntilNextLevel"], 4)
            mock_print.assert_any_call("The Mouse has been completely cured of their ailments!")
            mock_print.assert_any_call("You received: Red Berry!")

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["Blue"])  # Simulate giving a Blue berry
    def test_help_animal_invalid_berry(self, mock_print):
        with patch('src.character.get_item_from_inventory', return_value=False):
            help_animal(self.character, self.animal)

            mock_print.assert_called_once_with("Oh no! You don't have any 'Blue' berries in your inventory.")

    @patch('builtins.print')
    @patch('builtins.input', side_effect=[""])  # Simulate skipping the berry
    def test_skip_treatment(self, mock_input, mock_print):
        help_animal(self.character, self.animal)

        mock_print.assert_called_once_with("You skipped giving the animal a berry.")

    @patch('builtins.print')
    def test_no_ailments(self, mock_print):
        animal_without_ailments = {
            "Name": "Snake 🐍",
            "Ailments": []
        }
        help_animal(self.character, animal_without_ailments)

        mock_print.assert_called_once_with("The Snake 🐍 has been completely cured of their ailments!")

    @patch('builtins.print')
    @patch('builtins.input', side_effect=["Red"])  # Simulate giving a Red berry for the final challenge
    def test_final_challenge(self, mock_input, mock_print):
        final_challenge = {
            "Name": "FinalChallenge",
            "Ailments": ["Mystery"]
        }
        with patch('src.character.get_item_from_inventory', return_value=True), \
             patch('src.animal.validate_berry', return_value=True), \
             patch('src.entity.stringify_item', return_value="Red Berry"), \
             patch('src.entity.generate_item', return_value={"Type": "Item", "Name": "Special Token"}):

             help_animal(self.character, final_challenge)

             self.assertTrue(self.character.get("FinalChallengeCompleted", False))
             mock_print.assert_any_call("Congratulations! You have completed the Final Challenge! 🎉")

if __name__ == '__main__':
    unittest.main()
