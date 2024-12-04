import unittest
from src.board import describe_current_location


class TestDescribeCurrentLocation(unittest.TestCase):

    def setUp(self):
        self.character = {
            "InTree": False  # Initially set to False
        }

    def test_describe_current_location_ground(self):
        description = describe_current_location(self.character)
        self.assertIn("You are on the forest floor:", description)

    def test_describe_current_location_treetop(self):
        self.character["InTree"] = True
        description = describe_current_location(self.character)
        self.assertIn("You are in a treetop:", description)

if __name__ == '__main__':
    unittest.main()
