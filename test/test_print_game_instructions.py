import io
from unittest import TestCase
from unittest.mock import patch

from src.ui import print_game_instructions


class TestPrintInstructions(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_game_instructions(self, mock_output):
        self.maxDiff = None
        print_game_instructions()
        actual = mock_output.getvalue()
        expected = """ ✨ Your Mission: ✨
- Use your purr-oblem-solving skills to figure out which berry cures each animal’s ailment.
- Climb up trees to find berries with magical healing powers!
- Heal enough animals to help them level up and bring balance back to Whisker Woods.
- Reach Level 3, where Mittens becomes the ultimate Meowgical Healer and saves the forest for good!
- Keep an eye on your tummy while you explore! Moving and climbing is hard work,
  and if your tummy gets empty, you'll pass out from hunger!
  Eat any berry to refill your tummy by 25.
  Eat Catnip or Silvervine to refill it by even more, and get extra energy where you can move and climb for
  a while without affecting your tummy!
"""
        self.assertEqual(expected, actual)
