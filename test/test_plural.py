from unittest import TestCase

from src.util import plural


class TestPlural(TestCase):
    def test_plural_1(self):
        actual = plural(1)
        expected = ""
        self.assertEqual(expected, actual)

    def test_plural_2(self):
        actual = plural(2)
        expected = "s"
        self.assertEqual(expected, actual)

    def test_plural_5(self):
        actual = plural(5)
        expected = "s"
        self.assertEqual(expected, actual)

    def test_plural_0(self):
        actual = plural(0)
        expected = "s"
        self.assertEqual(expected, actual)

    def test_plural_negative(self):
        actual = plural(-1)
        expected = "s"
        self.assertEqual(expected, actual)

    def test_plural_floating_point_less_than_1(self):
        actual = plural(0.5)
        expected = "s"
        self.assertEqual(expected, actual)

    def test_plural_floating_point_greater_than_1(self):
        actual = plural(1.5)
        expected = "s"
        self.assertEqual(expected, actual)
