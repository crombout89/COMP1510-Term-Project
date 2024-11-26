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
        "FinalChallengeCompleted": None,
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


def current_location(character) -> tuple[int, int]:
    if character["InTree"]:
        return character["TreeCoordinates"]
    else:
        return character["GroundCoordinates"]


def check_tummy(character: dict) -> bool:
    if character["ExtraEnergy"] > 0:
        # If the character has extra energy, their tummy cannot run out by definition,
        # even if the actual level of the tummy is zero or negative. This buys the character time
        # to refill their tummy.
        return True
    else:
        if character["Tummy"] == 10:
            # TODO: print a message warning the user that they are getting hungry, and they should eat an item to
            #  restore their tummy
            return True
        elif character["Tummy"] == 1:
            # TODO: print a message warning the user that they are about to pass out from hunger, and they should eat
            #  an item to restore their tummy
            return True
        else:
            return character["Tummy"] > 0
