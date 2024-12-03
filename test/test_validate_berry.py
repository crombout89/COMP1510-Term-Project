from unittest import TestCase

from src.animal import validate_berry


class TestValidateBerry(TestCase):
    def test_validate_berry_injured_correct_berry_return_value(self):
        example_ailments = ["Injured"]
        berry_color = "Red"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_injured_correct_berry_ailment_list_change(self):
        example_ailments = ["Injured"]
        berry_color = "Red"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)

    def test_validate_berry_poisoned_correct_berry_return_value(self):
        example_ailments = ["Poisoned"]
        berry_color = "Green"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_poisoned_correct_berry_ailment_list_change(self):
        example_ailments = ["Poisoned"]
        berry_color = "Green"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)

    def test_validate_berry_dehydrated_correct_berry_return_value(self):
        example_ailments = ["Dehydrated"]
        berry_color = "Blue"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_dehydrated_correct_berry_ailment_list_change(self):
        example_ailments = ["Dehydrated"]
        berry_color = "Blue"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)

    def test_validate_berry_burned_correct_berry_return_value(self):
        example_ailments = ["Burned"]
        berry_color = "Yellow"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_burned_correct_berry_ailment_list_change(self):
        example_ailments = ["Burned"]
        berry_color = "Yellow"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)

    def test_validate_berry_sad_correct_berry_return_value(self):
        example_ailments = ["Sad"]
        berry_color = "Purple"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_sad_correct_berry_ailment_list_change(self):
        example_ailments = ["Sad"]
        berry_color = "Purple"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)

    def test_validate_berry_starving_red_berry_ailment_return_value(self):
        example_ailments = ["Starving"]
        berry_color = "Red"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_starving_red_berry_ailment_list_change(self):
        example_ailments = ["Starving"]
        berry_color = "Red"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)

    def test_validate_berry_starving_green_berry_ailment_return_value(self):
        example_ailments = ["Starving"]
        berry_color = "Green"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_starving_green_berry_ailment_list_change(self):
        example_ailments = ["Starving"]
        berry_color = "Green"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)

    def test_validate_berry_starving_blue_berry_ailment_return_value(self):
        example_ailments = ["Starving"]
        berry_color = "Blue"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_starving_blue_berry_ailment_list_change(self):
        example_ailments = ["Starving"]
        berry_color = "Blue"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)

    def test_validate_berry_starving_yellow_berry_ailment_return_value(self):
        example_ailments = ["Starving"]
        berry_color = "Yellow"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_starving_yellow_berry_ailment_list_change(self):
        example_ailments = ["Starving"]
        berry_color = "Yellow"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)

    def test_validate_berry_starving_purple_berry_ailment_return_value(self):
        example_ailments = ["Starving"]
        berry_color = "Purple"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_starving_purple_berry_ailment_list_change(self):
        example_ailments = ["Starving"]
        berry_color = "Purple"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)

    def test_validate_berry_more_than_one_ailment_correct_berry_return_value(self):
        example_ailments = ["Injured", "Dehydrated", "Sad"]
        berry_color = "Blue"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_more_than_one_ailment_correct_berry_ailment_list_change(self):
        example_ailments = ["Injured", "Dehydrated", "Sad"]
        berry_color = "Blue"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = ["Injured", "Sad"]
        self.assertEqual(expected, actual)

    def test_validate_berry_duplicate_ailment_correct_berry_return_value(self):
        example_ailments = ["Injured", "Injured"]
        berry_color = "Red"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_duplicate_ailment_correct_berry_ailment_list_change(self):
        example_ailments = ["Injured", "Injured"]
        berry_color = "Red"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = ["Injured"]
        self.assertEqual(expected, actual)

    def test_validate_berry_incorrect_berry_for_ailment_treats_starving_return_value(self):
        example_ailments = ["Injured", "Starving"]
        berry_color = "Blue"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_berry_incorrect_berry_for_ailment_treats_starving_ailment_list_change(self):
        example_ailments = ["Injured", "Starving"]
        berry_color = "Blue"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = ["Injured"]
        self.assertEqual(expected, actual)

    def test_validate_berry_incorrect_berry_return_value(self):
        example_ailments = ["Injured"]
        berry_color = "Blue"
        actual = validate_berry(berry_color, example_ailments)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_berry_incorrect_berry_ailment_list_change(self):
        example_ailments = ["Injured"]
        berry_color = "Blue"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = ["Injured"]
        self.assertEqual(expected, actual)
