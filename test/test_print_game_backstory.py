import io
from unittest import TestCase
from unittest.mock import patch

from src.ui import print_game_backstory


class TestPrintInstructions(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_game_backstory(self, mock_output):
        self.maxDiff = None
        print_game_backstory()
        actual = mock_output.getvalue()
        expected = """====================================
Welcome to Whisker Woods Rescue! 🐾🐈
====================================

Deep in the heart of Whisker Woods, a magical forest brimming with life,
animals have fallen ill from mysterious ailments. But don’t worry—there’s hope!
Meet Mittens, the Meowgical Healer, a kind-hearted kitty with a knack for
mixing berries into purrfect remedies.
Equipped with her trusty whisker sense and a satchel of enchanted berries,
she's on a mission to restore health to her forest friends, one paw at a time.

The animals are counting on you to guide Mittens through this pawsome adventure.
Every creature has a unique ailment that only the right berry can cure.
Mittens' healing magic helps animals grow stronger, level up, and paw-sibly
discover their own hidden powers!

 ✨ Your Mission: ✨
- Use your purr-oblem-solving skills to figure out which berry cures each animal’s ailment.
- Climb up trees to find berries with magical healing powers!
- Heal enough animals to help them level up and bring balance back to Whisker Woods.
- Reach Level 3, where Mittens becomes the ultimate Meowgical Healer and saves the forest for good!
- Keep an eye on your tummy while you explore! Moving and climbing is hard work,
  and if your tummy gets empty, you'll pass out from hunger!
  Eat any berry to refill your tummy by 25.
  Eat Catnip or Silvervine to refill it by even more, and get extra energy where you can move and climb for
  a while without affecting your tummy!

Are you ready to embark on this berry sweet adventure?
Paws, think, and heal! The forest is rooting for you. 🐾🍓✨
"""
        self.assertEqual(expected, actual)
