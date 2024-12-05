import io
from unittest import TestCase
from unittest.mock import patch

from src.ui import print_game_help


class TestPrintInstructions(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_game_help(self, mock_output):
        self.maxDiff = None
        print_game_help()
        actual = mock_output.getvalue()
        expected = """Type one of the following actions and press ENTER:
 - 'W' to move up
 - 'A' to move left
 - 'S' to move down
 - 'D' to move right
 - 'Check Tummy' to check your tummy and extra energy
 - 'Check Level' to check your level and how many animals you need to help before you level up
 - 'Check Inventory' to check what you have in your inventory
 - 'Check Location' to check where you are and how to get to the center of the board
 - 'Eat <item>' to eat a non-berry item like Catnip or Silvervine
 - 'Eat <colour> Berry' to eat a berry of the corresponding colour
 - 'Climb' to climb up or down a tree trunk
 - 'Nap' to take a nap on a patch of moss
 - 'Help' to the see the backstory and instructions from the start of the game

"""
        self.assertEqual(expected, actual)
