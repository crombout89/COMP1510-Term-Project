from unittest import TestCase

from src.character import restore_points


class TestRestorePoints(TestCase):
    def test_restore_points_tummy_0_extra_energy_0_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 0, 0)
        actual = example_character["Tummy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_0_extra_energy_0_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 0, 0)
        actual = example_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_1_extra_energy_0_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 1, 0)
        actual = example_character["Tummy"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_1_extra_energy_0_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 1, 0)
        actual = example_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_0_extra_energy_1_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 0, 1)
        actual = example_character["Tummy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_0_extra_energy_1_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 0, 1)
        actual = example_character["ExtraEnergy"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_1_extra_energy_1_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 1, 1)
        actual = example_character["Tummy"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_1_extra_energy_1_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 1, 1)
        actual = example_character["ExtraEnergy"]
        expected = 1
        self.assertEqual(expected, actual)
        
    def test_restore_points_tummy_2_extra_energy_3_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 2, 3)
        actual = example_character["Tummy"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_2_extra_energy_3_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 2, 3)
        actual = example_character["ExtraEnergy"]
        expected = 3
        self.assertEqual(expected, actual)
        
    def test_restore_points_tummy_default_value_extra_energy_default_value_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character)  # Default values: tummy=0, extra_energy=0
        actual = example_character["Tummy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_default_value_extra_energy_default_value_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character)  # Default values: tummy=0, extra_energy=0
        actual = example_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)
        
    def test_restore_points_tummy_1_extra_energy_default_value_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 1)  # Default values: extra_energy=0
        actual = example_character["Tummy"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_1_extra_energy_default_value_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, 1)  # Default values: extra_energy=0
        actual = example_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_default_value_extra_energy_1_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, extra_energy=1)  # Default values: tummy=0
        actual = example_character["Tummy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_default_value_extra_energy_1_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        restore_points(example_character, extra_energy=1)  # Default values: tummy=0
        actual = example_character["ExtraEnergy"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_restore_points_tummy_less_than_1(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        with self.assertRaises(ValueError) as context:
            restore_points(example_character, -1)
        self.assertEqual("tummy must be an integer greater than or equal to 0", str(context.exception))

    def test_restore_points_extra_energy_less_than_1(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        with self.assertRaises(ValueError) as context:
            restore_points(example_character, extra_energy=-1)
        self.assertEqual("extra_energy must be an integer greater than or equal to 0", str(context.exception))

    def test_restore_points_tummy_less_than_1_extra_energy_less_than_1(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
        }
        with self.assertRaises(ValueError) as context:
            restore_points(example_character, -1, -1)
        self.assertEqual("tummy must be an integer greater than or equal to 0", str(context.exception))
