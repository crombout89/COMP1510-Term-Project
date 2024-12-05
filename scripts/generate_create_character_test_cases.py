def main():
    top_level_attributes = {
        "Level": 1,
        "UntilNextLevel": 5,
        "InTree": False,
        "GroundCoordinates": (0, 0),
        "TreeCoordinates": (0, 0),
        "Tummy": 100,
        "ExtraEnergy": 0,
        "AnimalsHelped": 0,
        "FinalChallengeCompleted": None,
    }

    top_level_inventory = {
        "Catnip": 0,
        "Silvervine": 0
    }

    berries = {
        "Red": 1,
        "Green": 1,
        "Blue": 1,
        "Yellow": 1,
        "Purple": 1
    }

    for attribute in top_level_attributes.items():
        print(f"""
        def test_create_character_{attribute[0].lower()}_default_value(self):
            test_character = create_character("TestCharacterName")
            actual = test_character["{attribute[0]}"]
            expected = {attribute[1]}
            self.assertEqual(expected, actual)""")

    for attribute in top_level_inventory.items():
        print(f"""
        def test_create_character_{attribute[0].lower()}_default_value(self):
            test_character = create_character("TestCharacterName")
            actual = test_character["Inventory"]["{attribute[0]}"]
            expected = {attribute[1]}
            self.assertEqual(expected, actual)""")

    for attribute in berries.items():
        print(f"""
        def test_create_character_{attribute[0].lower()}_berry_default_value(self):
            test_character = create_character("TestCharacterName")
            actual = test_character["Inventory"]["Berries"]["{attribute[0]}"]
            expected = {attribute[1]}
            self.assertEqual(expected, actual)""")

if __name__ == "__main__":
    main()
