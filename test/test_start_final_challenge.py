import unittest
from src.character import start_final_challenge

class TestStartFinalChallenge(unittest.TestCase):

    def setUp(self):
        self.valid_character = {
            "InTree": True,
            "GroundCoordinates": (5, 5),
            "FinalChallengeCompleted": True
        }

    def test_successful_initialization(self):
        start_final_challenge(self.valid_character)

        # Check the character's state after the function call
        self.assertFalse(self.valid_character["InTree"])
        self.assertEqual(self.valid_character["GroundCoordinates"], (0, 0))
        self.assertFalse(self.valid_character["FinalChallengeCompleted"])

    def test_missing_in_tree_key(self):
        character_missing_key = {
            "GroundCoordinates": (5, 5),
            "FinalChallengeCompleted": True
        }
        with self.assertRaises(KeyError) as context:
            start_final_challenge(character_missing_key)
        self.assertEqual(context.exception.args[0], "Missing required key 'InTree' in character dictionary.")

    def test_missing_ground_coordinates_key(self):
        character_missing_key = {
            "InTree": True,
            "FinalChallengeCompleted": True
        }
        with self.assertRaises(KeyError) as context:
            start_final_challenge(character_missing_key)
        self.assertEqual(context.exception.args[0], "Missing required key 'GroundCoordinates' in character dictionary.")

    def test_missing_final_challenge_completed_key(self):
        character_missing_key = {
            "InTree": True,
            "GroundCoordinates": (5, 5),
        }
        with self.assertRaises(KeyError) as context:
            start_final_challenge(character_missing_key)
        self.assertEqual(context.exception.args[0],
                         "Missing required key 'FinalChallengeCompleted' in character dictionary.")


if __name__ == '__main__':
    unittest.main()