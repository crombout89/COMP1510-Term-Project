def main():
    berry_treatments = {
        # "Berry colour": "Treats this ailment"
        "Red": "Injured",
        "Green": "Poisoned",
        "Blue": "Dehydrated",
        "Yellow": "Burned",
        "Purple": "Sad",
    }

    for berry_treatment in berry_treatments.items():
        print(f"""
    def test_validate_berry_{berry_treatment[1].lower()}_correct_berry_return_value(self):
        example_ailments = ["{berry_treatment[1]}"]
        berry_color = "{berry_treatment[0]}"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)
        
    def test_validate_berry_{berry_treatment[1].lower()}_correct_berry_ailment_list_change(self):
        example_ailments = ["{berry_treatment[1]}"]
        berry_color = "{berry_treatment[0]}"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)""")

    for berry in berry_treatments.keys():
        print(f"""
    def test_validate_berry_starving_{berry.lower()}_berry_ailment_return_value(self):
        example_ailments = ["Starving"]
        berry_color = "{berry}"
        actual = validate_berry(berry_color, example_ailments)
        expected = True
        self.assertEqual(expected, actual)
        
    def test_validate_berry_starving_{berry.lower()}_berry_ailment_list_change(self):
        example_ailments = ["Starving"]
        berry_color = "{berry}"
        validate_berry(berry_color, example_ailments)
        actual = example_ailments
        expected = []
        self.assertEqual(expected, actual)""")


if __name__ == "__main__":
    main()
