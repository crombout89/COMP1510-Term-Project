import unittest
from src.board import describe_current_location


class TestDescribeCurrentLocation(unittest.TestCase):

    def setUp(self):
        self.character = {
            "InTree": False  # Initially set to False
        }

    def test_describe_current_location_ground(self):
        description = describe_current_location(self.character)
        self.assertIn("You are on the forest floor:", description)  # Update expected text

    def test_describe_current_location_treetop(self):
        self.character["InTree"] = True
        description = describe_current_location(self.character)
        self.assertIn("You are in a treetop:", description)

    def test_default_state(self):
        character = {}  # No InTree key
        description = describe_current_location(character)
        self.assertIn("You are on the forest floor:", description)  # Update expected text

    def test_invalid_in_tree_value(self):
        self.character["InTree"] = "Yes"  # Non-boolean value
        description = describe_current_location(self.character)
        self.assertIn("You are on the forest floor:", description)  # Update expected text

    def test_character_state_change(self):
        description_ground = describe_current_location(self.character)
        self.assertIn("You are on the forest floor:", description_ground)  # Update expected text

        self.character["InTree"] = True
        description_treetop = describe_current_location(self.character)
        self.assertIn("You are in a treetop:", description_treetop)

if __name__ == '__main__':
    unittest.main()
