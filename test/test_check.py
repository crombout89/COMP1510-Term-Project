import unittest
from unittest.mock import patch
from io import StringIO
from src.ui import check


class TestCheckFunction(unittest.TestCase):

    def setUp(self):
        self.character = {
            "Tummy": 50,
            "ExtraEnergy": 10,
            "Level": 2,
            "UntilNextLevel": 10,
            "GroundCoordinates": (5, 5),
            "InTree": False,
            "FinalChallengeCompleted": False,
            "Inventory": {
                "Catnip": 0,
                "Silvervine": 1,
                "Berries": {
                    "Red": 0,
                    "Green": 1,
                    "Blue": 2,
                    "Yellow": 3,
                    "Purple": 4
                }
            }
        }

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_tummy(self, mock_stdout):
        check(self.character, "Tummy")
        self.assertEqual(mock_stdout.getvalue().strip(),
                         'Your tummy level is: 50\nYou have extra energy for the next 10 move(s).')

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_level(self, mock_stdout):
        check(self.character, "Level")
        self.assertEqual(mock_stdout.getvalue().strip(), 'Your current level is: 2.'
                                                         '\nYou have to help 10 more animals to level up.')

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_inventory(self, mock_stdout):
        check(self.character, "Inventory")
        expected_output = ("Your inventory contains:\n "
                           "- 0 Catnip\n "
                           "- 1 Silvervine\n"
                           " - 0 Red Berries\n"
                           " - 1 Green Berry\n"
                           " - 2 Blue Berries\n"
                           " - 3 Yellow Berries\n"
                           " - 4 Purple Berries")
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('src.ui.check')
    def test_check_invalid_attribute(self, mock_check):
        # Set the mock to raise a ValueError when called
        mock_check.side_effect = ValueError("🚫 'Health' is not a supported attribute to check!")

        with self.assertRaises(ValueError) as context:
            mock_check(self.character, "Health")

        self.assertEqual(str(context.exception), "🚫 'Health' is not a supported attribute to check!")

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_location(self, mock_stdout):
        check(self.character, "Location")
        output = mock_stdout.getvalue().strip()
        self.assertIn("You're on the ground.", output)


if __name__ == '__main__':
    unittest.main()
