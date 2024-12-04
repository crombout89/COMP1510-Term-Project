import unittest
from src.board import populate_board


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

        # Check if the sick animal was placed correctly
        sick_animal_count = sum(1 for tile in self.board.values() if tile and tile.get("name") == "SickAnimal")
        self.assertEqual(sick_animal_count, 2)

    def test_reserve_tile_not_occupied(self):
        populate_board(self.board, "TreeTrunk", 1)
        self.assertIsNone(self.board[(0, 0)])  # Reserved tile should remain unchanged

    def test_no_population_with_zero_times(self):
        with self.assertRaises(ValueError):
            populate_board(self.board, "TreeTrunk", 0)

    def test_population_with_no_space(self):
        # Fill the board completely, but leave the reserved tile unoccupied
        for x in range(1, 6):
            for y in range(1, 6):
                if (x, y) != (0, 0):  # Leave the reserved tile empty
                    self.board[(x, y)] = "Occupied"

        # Ensure the reserved tile remains unoccupied
        self.board[(0, 0)] = None  # Reserved tile

        # Now test for a case with no valid spaces
        with self.assertRaises(ValueError):
            populate_board(self.board, "TreeTrunk", 1)  # Should throw an error

        # Check that no TreeTrunks were placed
        self.assertEqual(sum(1 for tile in self.board.values() if tile == "TreeTrunk"), 0)


if __name__ == '__main__':
    unittest.main()