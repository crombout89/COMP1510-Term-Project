import io
from unittest import TestCase
from unittest.mock import patch

from src.ui import game_over


class TestPrintInstructions(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_berry_help(self, mock_output):
        self.maxDiff = None
        game_over()
        actual = mock_output.getvalue()
        expected = """
💔 Oh no! You've passed out from hunger!
Without the energy to continue, your adventure comes to an end.
But don’t worry —- every hero gets another chance!
"""
        self.assertEqual(expected, actual)
