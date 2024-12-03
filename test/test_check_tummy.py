import io
from unittest import TestCase
from unittest.mock import patch

from src.character import check_tummy


class TestCurrentLocation(TestCase):
    def test_current_location_tummy_greater_than_10_extra_energy_not_0_return_value(self):
        example_character = {
            "ExtraEnergy": 1,
            "Tummy": 11,
        }
        actual = check_tummy(example_character)
        expected = True
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_current_location_tummy_greater_than_10_extra_energy_not_0_console_output(self, mock_output):
        example_character = {
            "ExtraEnergy": 1,
            "Tummy": 11,
        }
        check_tummy(example_character)
        actual = mock_output.getvalue()
        expected = ""
        self.assertEqual(expected, actual)

    def test_current_location_tummy_greater_than_10_extra_energy_0_return_value(self):
        example_character = {
            "ExtraEnergy": 0,
            "Tummy": 11,
        }
        actual = check_tummy(example_character)
        expected = True
        self.assertEqual(expected, actual)

    def test_current_location_tummy_greater_than_10_extra_energy_less_than_0_return_value(self):
        example_character = {
            "ExtraEnergy": -1,
            "Tummy": 11,
        }
        actual = check_tummy(example_character)
        expected = True
        self.assertEqual(expected, actual)
        
    def test_current_location_tummy_10_extra_energy_not_0_return_value(self):
        example_character = {
            "ExtraEnergy": 1,
            "Tummy": 10,
        }
        actual = check_tummy(example_character)
        expected = True
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_current_location_tummy_10_extra_energy_not_0_console_output(self, mock_output):
        example_character = {
            "ExtraEnergy": 1,
            "Tummy": 10,
        }
        check_tummy(example_character)
        actual = mock_output.getvalue()
        expected = ""
        self.assertEqual(expected, actual)

    def test_current_location_tummy_10_extra_energy_0_return_value(self):
        example_character = {
            "ExtraEnergy": 0,
            "Tummy": 10,
        }
        actual = check_tummy(example_character)
        expected = True
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_current_location_tummy_10_extra_energy_0_console_output(self, mock_output):
        example_character = {
            "ExtraEnergy": 0,
            "Tummy": 10,
        }
        check_tummy(example_character)
        actual = mock_output.getvalue()
        expected = "⚠️ You're getting hungry! You should eat an item soon to restore your tummy!\n"
        self.assertEqual(expected, actual)

    def test_current_location_tummy_less_than_10_extra_energy_not_0_return_value(self):
        example_character = {
            "ExtraEnergy": 1,
            "Tummy": 9,
        }
        actual = check_tummy(example_character)
        expected = True
        self.assertEqual(expected, actual)

    def test_current_location_tummy_less_than_10_extra_energy_0_return_value(self):
        example_character = {
            "ExtraEnergy": 0,
            "Tummy": 9,
        }
        actual = check_tummy(example_character)
        expected = True
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_current_location_tummy_less_than_10_extra_energy_0_console_output(self, mock_output):
        example_character = {
            "ExtraEnergy": 0,
            "Tummy": 9,
        }
        check_tummy(example_character)
        actual = mock_output.getvalue()
        expected = ""
        self.assertEqual(expected, actual)

    def test_current_location_tummy_1_extra_energy_not_0_return_value(self):
        example_character = {
            "ExtraEnergy": 1,
            "Tummy": 1,
        }
        actual = check_tummy(example_character)
        expected = True
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_current_location_tummy_1_extra_energy_not_0_console_output(self, mock_output):
        example_character = {
            "ExtraEnergy": 1,
            "Tummy": 1,
        }
        check_tummy(example_character)
        actual = mock_output.getvalue()
        expected = ""
        self.assertEqual(expected, actual)

    def test_current_location_tummy_1_extra_energy_0_return_value(self):
        example_character = {
            "ExtraEnergy": 0,
            "Tummy": 1,
        }
        actual = check_tummy(example_character)
        expected = True
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_current_location_tummy_1_extra_energy_0_console_output(self, mock_output):
        example_character = {
            "ExtraEnergy": 0,
            "Tummy": 1,
        }
        check_tummy(example_character)
        actual = mock_output.getvalue()
        expected = "⚠️ You're about to pass out from hunger! Eat an item now to restore your tummy!\n"
        self.assertEqual(expected, actual)

    def test_current_location_tummy_0_extra_energy_not_0_return_value(self):
        example_character = {
            "ExtraEnergy": 1,
            "Tummy": 0,
        }
        actual = check_tummy(example_character)
        expected = True
        self.assertEqual(expected, actual)

    def test_current_location_tummy_0_extra_energy_0_return_value(self):
        example_character = {
            "ExtraEnergy": 0,
            "Tummy": 0,
        }
        actual = check_tummy(example_character)
        expected = False
        self.assertEqual(expected, actual)

    def test_current_location_tummy_less_than_0_extra_energy_not_0_return_value(self):
        example_character = {
            "ExtraEnergy": 1,
            "Tummy": -1,
        }
        actual = check_tummy(example_character)
        expected = True
        self.assertEqual(expected, actual)

    def test_current_location_tummy_less_than_0_extra_energy_0_return_value(self):
        example_character = {
            "ExtraEnergy": 0,
            "Tummy": -1,
        }
        actual = check_tummy(example_character)
        expected = False
        self.assertEqual(expected, actual)
