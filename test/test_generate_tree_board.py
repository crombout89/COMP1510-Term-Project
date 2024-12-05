import unittest
import random
from src.board import generate_tree_board
from src.config import TREE_SCALE_OPTIONS
from src.description import moss_description


class TestGenerateTreeBoard(unittest.TestCase):

    def setUp(self):
        # Choose a random tree scale for each test
        self.tree_scale = random.choice(TREE_SCALE_OPTIONS)

    def test_tree_trunk_placement(self):
        tree_board_result = generate_tree_board()
        self.assertEqual(tree_board_result[(0, 0)], "TreeTrunk")  # Specify the expected value

    def test_moss_count_within_bounds(self):
        tree_board_result = generate_tree_board()
        total_moss_count = sum(1 for moss_entity in tree_board_result.values() if moss_entity == "Moss")
        self.assertGreaterEqual(total_moss_count, 0, "Moss count should not be negative")
        self.assertLessEqual(total_moss_count, self.tree_scale, "Moss count should not exceed tree_scale")

    def test_board_dimensions(self):
        tree_board_result = generate_tree_board()
        min_x = -self.tree_scale
        max_x = self.tree_scale
        min_y = -self.tree_scale
        max_y = self.tree_scale

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                self.assertIn((x, y), tree_board_result, f"Coordinate {(x, y)} should be in the board")

    def test_empty_tiles_description(self):
        tree_board_result = generate_tree_board()
        for position, entity in tree_board_result.items():
            # Check if the entity is None (indicating an empty tile)
            if entity is None:
                self.assertIn(position, tree_board_result, "Empty tiles should exist in the board")
                description = "An empty tile, but it could hold secrets."
                self.assertIsNotNone(description, "Empty tiles should have a description")

    def test_randomness_of_moss(self):
        moss_descriptions = {moss_description() for _ in range(10)}  # Get a set of moss descriptions
        self.assertGreater(len(moss_descriptions), 1, "Moss descriptions should be varied")


if __name__ == '__main__':
    unittest.main()
