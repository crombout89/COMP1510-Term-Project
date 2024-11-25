def create_character(name: str) -> dict:
    return {
        "Name": name,
        "Level": 1,
        "UntilNextLevel": 5,
        "InTree": False,
        "GroundCoordinates": (0, 0),
        "TreeCoordinates": (0, 0),
        "Tummy": 100,
        "ExtraEnergy": 0,
        "AnimalsHelped": 0,
        "FinalChallengeCompleted": 0,
        "Inventory": {
            "Berries": {
                "Red": 1,
                "Green": 1,
                "Blue": 1,
                "Yellow": 1,
                "Purple": 1
            },
            "Catnip": 0,
            "SilverVine": 0
        }
    }
