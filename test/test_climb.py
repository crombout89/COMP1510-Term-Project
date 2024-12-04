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

    def test_climb_success(self):
        self.character["TreeCoordinates"] = (5, 5)
        result = climb(self.character, self.board)
        self.assertTrue(result)
        self.assertTrue(self.character["InTree"])
        self.assertEqual(self.character["TreeCoordinates"], (5, 5))

    def test_climb_again(self):
        self.character["InTree"] = True
        self.character["TreeCoordinates"] = (5, 5)
        result = climb(self.character, self.board)
        self.assertFalse(result)
        self.assertFalse(self.character["InTree"])

    def test_climb_without_tree(self):
        self.character["TreeCoordinates"] = (6, 5)
        result = climb(self.character, self.board)
        self.assertFalse(result)
        self.assertFalse(self.character["InTree"])

if __name__ == '__main__':
    unittest.main()
