from unittest import TestCase
import pygame
from src.character import update_level


class TestUpdateLevel(TestCase):
    def setUp(self):
        # Initialize Pygame mixer for sound effects
        pygame.mixer.init()

        self.base_character = {
            "Level": 1,
            "UntilNextLevel": 1,
            "FinalChallengeCompleted": None,
            "InTree": False,
            "GroundCoordinates": (5, 5)
        }

    def test_update_level_no_change(self):
        example_character = self.base_character.copy()
        update_level(example_character)
        actual = example_character["Level"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_update_level_level_up_from_1_level_change(self):
        example_character = self.base_character.copy()
        example_character["Level"] = 1
        example_character["UntilNextLevel"] = 0
        update_level(example_character)
        actual = example_character["Level"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_update_level_level_up_from_1_until_next_level(self):
        example_character = self.base_character.copy()
        example_character["Level"] = 1
        example_character["UntilNextLevel"] = 0
        update_level(example_character)
        actual = example_character["UntilNextLevel"]
        expected = 10
        self.assertEqual(expected, actual)

    def test_update_level_level_up_from_1_final_challenge_not_started(self):
        example_character = self.base_character.copy()
        update_level(example_character)
        actual = example_character["FinalChallengeCompleted"]
        expected = None
        self.assertEqual(expected, actual)

    def test_update_level_level_up_from_2_level_change(self):
        example_character = self.base_character.copy()
        example_character["Level"] = 2
        example_character["UntilNextLevel"] = 0
        update_level(example_character)
        actual = example_character["Level"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_update_level_level_up_from_2_until_next_level(self):
        example_character = self.base_character.copy()
        example_character["Level"] = 2
        example_character["UntilNextLevel"] = 0
        update_level(example_character)
        actual = example_character["UntilNextLevel"]
        expected = 15
        self.assertEqual(expected, actual)

    def test_update_level_level_up_from_2_final_challenge_started(self):
        example_character = self.base_character.copy()
        example_character["Level"] = 2
        example_character["UntilNextLevel"] = 0
        update_level(example_character)
        actual = example_character["FinalChallengeCompleted"]
        expected = False
        self.assertEqual(expected, actual)
