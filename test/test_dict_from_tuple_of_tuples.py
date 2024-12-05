from unittest import TestCase

from src.util import dict_from_tuple_of_tuples


class TestCurrentLocation(TestCase):
    def test_dict_from_tuple_of_tuples_single_key_value_pair(self):
        example_structure = (
            ("key", "value"),
        )
        actual = dict_from_tuple_of_tuples(example_structure)
        expected = {
            "key": "value"
        }
        self.assertEqual(expected, actual)

    def test_dict_from_tuple_of_tuples_two_key_value_pairs(self):
        example_structure = (
            ("key1", "value1"),
            ("key2", "value2"),
        )
        actual = dict_from_tuple_of_tuples(example_structure)
        expected = {
            "key1": "value1",
            "key2": "value2"
        }
        self.assertEqual(expected, actual)

    def test_dict_from_tuple_of_tuples_multiple_key_value_pairs(self):
        example_structure = (
            ("key1", "value1"),
            ("key2", "value2"),
            ("key3", "value3"),
            ("key4", "value4")
        )
        actual = dict_from_tuple_of_tuples(example_structure)
        expected = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
            "key4": "value4"
        }
        self.assertEqual(expected, actual)

    def test_dict_from_tuple_of_tuples_int_as_key(self):
        example_structure = (
            (1, "value"),
        )
        actual = dict_from_tuple_of_tuples(example_structure)
        expected = {
            1: "value"
        }
        self.assertEqual(expected, actual)

    def test_dict_from_tuple_of_tuples_int_as_value(self):
        example_structure = (
            ("key", 1),
        )
        actual = dict_from_tuple_of_tuples(example_structure)
        expected = {
            "key": 1
        }
        self.assertEqual(expected, actual)

    def test_dict_from_tuple_of_tuples_bool_as_key(self):
        example_structure = (
            (False, "value"),
        )
        actual = dict_from_tuple_of_tuples(example_structure)
        expected = {
            False: "value"
        }
        self.assertEqual(expected, actual)

    def test_dict_from_tuple_of_tuples_bool_as_value(self):
        example_structure = (
            ("key", False),
        )
        actual = dict_from_tuple_of_tuples(example_structure)
        expected = {
            "key": False
        }
        self.assertEqual(expected, actual)

    def test_dict_from_tuple_of_tuples_tuple_as_key(self):
        example_structure = (
            ((1, 2), "value"),
        )
        actual = dict_from_tuple_of_tuples(example_structure)
        expected = {
            (1, 2): "value"
        }
        self.assertEqual(expected, actual)

    def test_dict_from_tuple_of_tuples_tuple_as_value(self):
        example_structure = (
            ("key", (1, 2)),
        )
        actual = dict_from_tuple_of_tuples(example_structure)
        expected = {
            "key": (1, 2)
        }
        self.assertEqual(expected, actual)

    def test_dict_from_tuple_of_tuples_none_as_key(self):
        example_structure = (
            (None, "value"),
        )
        actual = dict_from_tuple_of_tuples(example_structure)
        expected = {
            None: "value"
        }
        self.assertEqual(expected, actual)

    def test_dict_from_tuple_of_tuples_none_as_value(self):
        example_structure = (
            ("key", None),
        )
        actual = dict_from_tuple_of_tuples(example_structure)
        expected = {
            "key": None
        }
        self.assertEqual(expected, actual)
