import unittest
from src.action import climb

class TestClimbFunction(unittest.TestCase):

    def setUp(self):
        self.character = {
            "InTree": False,
            "TreeCoordinates": (0, 0),
            "GroundCoordinates": (5, 5),  # Add the expected key for current location
            "ExtraEnergy": 10,
            "Tummy": 100
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
        # Climb for the first time
        self.character["GroundCoordinates"] = (5, 5)  # Ensure at tree trunk
        climb(self.character, self.board)
        result = climb(self.character, self.board)  # Try to climb again
        self.assertFalse(result)  # Should return False
        self.assertTrue(self.character["InTree"])  # Still in tree

    def test_climb_without_tree(self):
        self.character["GroundCoordinates"] = (6, 5)  # Not at tree trunk
        result = climb(self.character, self.board)
        self.assertFalse(result)  # Should return False
        self.assertFalse(self.character["InTree"])  # Should still not be in tree

if __name__ == '__main__':
    unittest.main()
