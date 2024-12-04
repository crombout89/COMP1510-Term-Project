import unittest
from unittest.mock import patch
from src.entity import generate_item

class TestGenerateItem(unittest.TestCase):

    def setUp(self):
        self.character_in_tree = {"InTree": True}
        self.character_not_in_tree = {"InTree": False}


if __name__ == '__main__':
    unittest.main()
