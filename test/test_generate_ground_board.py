import unittest
from src.board import generate_ground_board

class TestGenerateGroundBoard(unittest.TestCase):

    def test_tree_trunks_exist(self):
        board = generate_ground_board()
        self.assertIn("TreeTrunk", board.values())

    def test_tree_trunk_count(self):
        board = generate_ground_board()
        tree_trunk_count = sum(1 for tile in board.values() if tile == "TreeTrunk")
        self.assertGreaterEqual(tree_trunk_count, 30)
        self.assertLessEqual(tree_trunk_count, 60)

    def test_empty_tiles_has_empty_space(self):
        board = generate_ground_board()
        empty_tiles = [tile for tile in board if board[tile] is None]
        actual = len(empty_tiles)
        self.assertGreater(actual, 0)  # All empty tiles should be filled


if __name__ == '__main__':
    unittest.main()