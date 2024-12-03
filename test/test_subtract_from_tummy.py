from unittest import TestCase

from src.character import subtract_from_tummy


class TestUpdateLevel(TestCase):
    def test_subtract_from_tummy_1_unit_no_extra_energy(self):
        example_character = {
            "Tummy": 100,
            "ExtraEnergy": 0
        }
        subtract_from_tummy(example_character, 1)
        actual = example_character["Tummy"]
        expected = 99
        self.assertEqual(expected, actual)

    def test_subtract_from_tummy_5_units_no_extra_energy(self):
        example_character = {
            "Tummy": 100,
            "ExtraEnergy": 0
        }
        subtract_from_tummy(example_character, 5)
        actual = example_character["Tummy"]
        expected = 95
        self.assertEqual(expected, actual)

    def test_subtract_from_tummy_1_unit_extra_energy_tummy_change(self):
        example_character = {
            "Tummy": 100,
            "ExtraEnergy": 1
        }
        subtract_from_tummy(example_character, 1)
        actual = example_character["Tummy"]
        expected = 100
        self.assertEqual(expected, actual)

    def test_subtract_from_tummy_5_units_extra_energy_tummy_change(self):
        example_character = {
            "Tummy": 100,
            "ExtraEnergy": 1
        }
        subtract_from_tummy(example_character, 5)
        actual = example_character["Tummy"]
        expected = 100
        self.assertEqual(expected, actual)

    def test_subtract_from_tummy_1_unit_extra_energy_extra_energy_change(self):
        example_character = {
            "Tummy": 100,
            "ExtraEnergy": 1
        }
        subtract_from_tummy(example_character, 1)
        actual = example_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_subtract_from_tummy_5_units_extra_energy_extra_energy_change(self):
        example_character = {
            "Tummy": 100,
            "ExtraEnergy": 1
        }
        subtract_from_tummy(example_character, 5)
        actual = example_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)
