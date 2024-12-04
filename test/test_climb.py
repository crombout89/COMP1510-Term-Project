import unittest
from src.action import climb

class TestClimbFunction(unittest.TestCase):

    def setUp(self):
        self.character = {
            "InTree": False,
            "TreeCoordinates": (0, 0)
        }
        self.board = {
            (5, 5): "TreeTrunk",
            (6, 5): None
        }

if __name__ == '__main__':
    unittest.main()
