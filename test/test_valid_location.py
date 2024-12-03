from unittest import TestCase

from src.board import valid_location


class TestValidLocation(TestCase):
    def test_valid_location_center_of_board(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (0, 0))
        expected = True
        self.assertEqual(expected, actual)

    def test_valid_location_top_edge(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (-1, 0))
        expected = True
        self.assertEqual(expected, actual)

    def test_valid_location_off_top_edge(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (-2, 0))
        expected = False
        self.assertEqual(expected, actual)

    def test_valid_location_bottom_edge(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (1, 0))
        expected = True
        self.assertEqual(expected, actual)

    def test_valid_location_off_bottom_edge(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (2, 0))
        expected = False
        self.assertEqual(expected, actual)

    def test_valid_location_left_edge(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (0, -1))
        expected = True
        self.assertEqual(expected, actual)

    def test_valid_location_off_left_edge(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (0, -2))
        expected = False
        self.assertEqual(expected, actual)

    def test_valid_location_right_edge(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (0, 1))
        expected = True
        self.assertEqual(expected, actual)

    def test_valid_location_off_right_edge(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (0, 2))
        expected = False
        self.assertEqual(expected, actual)

    def test_valid_location_top_left_corner(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (-1, -1))
        expected = True
        self.assertEqual(expected, actual)

    def test_valid_location_off_top_left_corner(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (-2, -2))
        expected = False
        self.assertEqual(expected, actual)

    def test_valid_location_top_right_corner(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (-1, 1))
        expected = True
        self.assertEqual(expected, actual)

    def test_valid_location_off_top_right_corner(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (-2, 2))
        expected = False
        self.assertEqual(expected, actual)

    def test_valid_location_bottom_left_corner(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (1, -1))
        expected = True
        self.assertEqual(expected, actual)

    def test_valid_location_off_bottom_left_corner(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (2, -2))
        expected = False
        self.assertEqual(expected, actual)

    def test_valid_location_bottom_right_corner(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (1, 1))
        expected = True
        self.assertEqual(expected, actual)

    def test_valid_location_off_bottom_right_corner(self):
        example_board = {
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        actual = valid_location(example_board, (2, 2))
        expected = False
        self.assertEqual(expected, actual)
