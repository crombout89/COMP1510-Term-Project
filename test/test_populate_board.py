import unittest
from unittest.mock import patch
from src.board import populate_board
from src.descriptions import sick_animal_description

class TestPopulateBoard(unittest.TestCase):

    def setUp(self):
        self.board = {
            "meta": {"min_x": 1, "max_x": 5, "min_y": 1, "max_y": 5},
            (1, 1): None,
            (2, 2): None,
            (0, 0): None  # Reserved tile
        }


if __name__ == '__main__':
    unittest.main()