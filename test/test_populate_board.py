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

    def test_populate_tree_trunk(self):
        populate_board(self.board, "TreeTrunk", 3)
        tree_count = sum(1 for tile in self.board.values() if tile == "TreeTrunk")
        self.assertEqual(tree_count, 3)

    def test_populate_sick_animal(self):
        animal_data = {
            "Type": "Animal",
            "Name": "Rabbit",
            "Data": ["Injury", "Exhaustion"]
        }
        populate_board(self.board, "SickAnimal", 2, animal_data)
        sick_animal_count = sum(1 for tile in self.board.values() if "Rabbit" in tile)
        self.assertEqual(sick_animal_count, 2)

    def test_reserve_tile_not_occupied(self):
        populate_board(self.board, "TreeTrunk", 1)
        self.assertIsNone(self.board[(0, 0)])  # Reserved tile should remain unchanged

    def test_no_population_with_zero_times(self):
        with self.assertRaises(ValueError):
            populate_board(self.board, "TreeTrunk", 0)

    def test_population_with_no_space(self):
        # Fill the board completely except for the reserved tile
        for x in range(1, 6):
            for y in range(1, 6):
                if (x, y) != (0, 0):
                    self.board[(x, y)] = "Occupied"

        populate_board(self.board, "TreeTrunk", 1)  # Should not throw an error, but not place anything
        self.assertEqual(sum(1 for tile in self.board.values() if tile == "TreeTrunk"), 0)


if __name__ == '__main__':
    unittest.main()