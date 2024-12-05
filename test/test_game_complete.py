import io
from unittest import TestCase
from unittest.mock import patch, Mock

from src.sfx import sfx_setup
from src.ui import game_complete


class TestPrintInstructions(TestCase):

    @patch("src.sfx.play_finale_music")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_game_complete(self, mock_output, mock_play_finale_music):
        self.maxDiff = None
        mock_play_finale_music.return_value = None
        game_complete()
        actual = mock_output.getvalue()
        expected = """
🎉 Congratulations! You've completed Whisker Woods Rescue! 🎉
Thanks to your purr-severance and kindness, the forest is thriving again.
You've become the ultimate Meowgical Healer, and all the animals are healthy and happy!
Your trusty owner, the Professor, praises you for earning the trust and love of all creatures inthe forest.
You've forged bonds with both real and imaginary friends, and now the forest is a place of joy and laughter!
"""
        self.assertEqual(expected, actual)
