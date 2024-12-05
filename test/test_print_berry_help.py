import io
from unittest import TestCase
from unittest.mock import patch

from src.ui import print_berry_help


class TestPrintInstructions(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_berry_help(self, mock_output):
        self.maxDiff = None
        print_berry_help()
        actual = mock_output.getvalue()
        expected = """----------------------------------------
| <colour> Berry | Treats this Ailment |
----------------------------------------
| Red            | Injured             |
| Green          | Poisoned            |
| Blue           | Dehydrated          |
| Yellow         | Burned              |
| Purple         | Sad                 |
----------------------------------------
"""
        self.assertEqual(expected, actual)
