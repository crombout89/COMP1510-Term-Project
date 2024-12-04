import unittest
from src.board import generate_ground_board

class TestGenerateGroundBoard(unittest.TestCase):

    def test_tree_trunks_exist(self):
        board = generate_ground_board()
        tree_trunk_count = sum(1 for tile in board.values() if tile == "TreeTrunk")
        self.assertGreaterEqual(tree_trunk_count, 30)
        self.assertLessEqual(tree_trunk_count, 60)

if __name__ == '__main__':
    unittest.main()