import unittest

from src.board import generate_board


class TestGenerateBoard(unittest.TestCase):

    def test_generate_board_1_by_1(self):
        actual = generate_board(0, 0, 0, 0)
        expected = {
            "meta": {
                "min_x": 0,
                "max_x": 0,
                "min_y": 0,
                "max_y": 0
            },
            (0, 0): None
        }
        self.assertEqual(expected, actual)

    def test_generate_board_3_by_1(self):
        actual = generate_board(-1, 1, 0, 0)
        expected = {
            "meta": {
                "min_x": -1,
                "max_x": 1,
                "min_y": 0,
                "max_y": 0
            },
            (-1, 0): None,
            (0, 0): None,
            (1, 0): None
        }
        self.assertEqual(expected, actual)

    def test_generate_board_1_by_3(self):
        actual = generate_board(0, 0, -1, 1)
        expected = {
            "meta": {
                "min_x": 0,
                "max_x": 0,
                "min_y": -1,
                "max_y": 1
            },
            (0, -1): None, (0, 0): None, (0, 1): None
        }
        self.assertEqual(expected, actual)

    def test_generate_board_3_by_3(self):
        actual = generate_board(-1, 1, -1, 1)
        expected = {
            "meta": {
                "min_x": -1,
                "max_x": 1,
                "min_y": -1,
                "max_y": 1
            },
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None
        }
        self.assertEqual(expected, actual)

    def test_generate_board_5_by_3(self):
        actual = generate_board(-2, 2, -1, 1)
        expected = {
            "meta": {
                "min_x": -2,
                "max_x": 2,
                "min_y": -1,
                "max_y": 1
            },
            (-2, -1): None, (-2, 0): None, (-2, 1): None,
            (-1, -1): None, (-1, 0): None, (-1, 1): None,
            (0, -1): None, (0, 0): None, (0, 1): None,
            (1, -1): None, (1, 0): None, (1, 1): None,
            (2, -1): None, (2, 0): None, (2, 1): None
        }
        self.assertEqual(expected, actual)

    def test_generate_board_3_by_5(self):
        actual = generate_board(-1, 1, -2, 2)
        expected = {
            "meta": {
                "min_x": -1,
                "max_x": 1,
                "min_y": -2,
                "max_y": 2
            },
            (-1, -2): None, (-1, -1): None, (-1, 0): None, (-1, 1): None, (-1, 2): None,
            (0, -2): None, (0, -1): None, (0, 0): None, (0, 1): None, (0, 2): None,
            (1, -2): None, (1, -1): None, (1, 0): None, (1, 1): None, (1, 2): None
        }
        self.assertEqual(expected, actual)

    def test_generate_board_5_by_5(self):
        actual = generate_board(-2, 2, -2, 2)
        expected = {
            "meta": {
                "min_x": -2,
                "max_x": 2,
                "min_y": -2,
                "max_y": 2
            },
            (-2, -2): None, (-2, -1): None, (-2, 0): None, (-2, 1): None, (-2, 2): None,
            (-1, -2): None, (-1, -1): None, (-1, 0): None, (-1, 1): None, (-1, 2): None,
            (0, -2): None, (0, -1): None, (0, 0): None, (0, 1): None, (0, 2): None,
            (1, -2): None, (1, -1): None, (1, 0): None, (1, 1): None, (1, 2): None,
            (2, -2): None, (2, -1): None, (2, 0): None, (2, 1): None, (2, 2): None
        }
        self.assertEqual(expected, actual)

    def test_generate_board_min_x_greater_than_max_x(self):
        with self.assertRaises(ValueError) as context:
            generate_board(1, -1, 0, 0)
        self.assertEqual("min_x must be less than or equal to max_x", str(context.exception))

    def test_generate_board_min_y_greater_than_max_y(self):
        with self.assertRaises(ValueError) as context:
            generate_board(0, 0, 1, -1)
        self.assertEqual("min_y must be less than or equal to max_y", str(context.exception))

    def test_generate_board_min_x_greater_than_max_x_and_min_y_greater_than_max_y(self):
        with self.assertRaises(ValueError) as context:
            generate_board(1, -1, 1, -1)
        self.assertEqual("min_x must be less than or equal to max_x", str(context.exception))

if __name__ == '__main__':
    unittest.main()