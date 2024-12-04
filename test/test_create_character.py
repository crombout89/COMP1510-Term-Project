import unittest
from unittest import TestCase

from src.character import create_character


class TestCreateCharacter(TestCase):

    def test_create_character_name(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["Name"]
        expected = "TestCharacterName"
        self.assertEqual(expected, actual)

    def test_create_character_level_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["Level"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_create_character_untilnextlevel_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["UntilNextLevel"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_create_character_intree_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["InTree"]
        expected = False
        self.assertEqual(expected, actual)

    def test_create_character_groundcoordinates_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["GroundCoordinates"]
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_create_character_treecoordinates_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["TreeCoordinates"]
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_create_character_tummy_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["Tummy"]
        expected = 100
        self.assertEqual(expected, actual)

    def test_create_character_extraenergy_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_create_character_animalshelped_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["AnimalsHelped"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_create_character_finalchallengecompleted_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["FinalChallengeCompleted"]
        expected = None
        self.assertEqual(expected, actual)

    def test_create_character_catnip_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["Inventory"]["Catnip"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_create_character_silvervine_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["Inventory"]["SilverVine"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_create_character_red_berry_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["Inventory"]["Berries"]["Red"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_create_character_green_berry_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["Inventory"]["Berries"]["Green"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_create_character_blue_berry_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["Inventory"]["Berries"]["Blue"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_create_character_yellow_berry_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["Inventory"]["Berries"]["Yellow"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_create_character_purple_berry_default_value(self):
        test_character = create_character("TestCharacterName")
        actual = test_character["Inventory"]["Berries"]["Purple"]
        expected = 1
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

