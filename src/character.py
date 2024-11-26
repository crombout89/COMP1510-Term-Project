from config import UNTIL_NEXT_LEVEL_MULTIPLIER


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


def update_level(character: dict) -> bool:
    if character["UntilNextLevel"] <= 0:
        character["Level"] += 1
        character["UntilNextLevel"] = UNTIL_NEXT_LEVEL_MULTIPLIER * character["Level"]
    if character["Level"] == 3 and character["FinalChallengeCompleted"] is None:
        character["FinalChallengeCompleted"] = False
    else:
        return character["Level"] == 3 and character["FinalChallengeCompleted"]


def subtract_from_tummy(character: dict, units: int):
    if character["ExtraEnergy"] > 0:
        character["ExtraEnergy"] -= 1
    else:
        character["Tummy"] -= units


def get_item_from_inventory(character: dict, item: dict) -> bool:
    if item["Name"] == "Catnip" or item["Name"] == "Silvervine":
        if character["Inventory"][item["Name"]] > 0:
            character["Inventory"][item["Name"]] -= 0
            return True
        else:
            return False
    elif item["Name"] == "Berry":
        if character["Inventory"]["Berries"][item["Data"]] > 0:
            character["Inventory"]["Berries"][item["Data"]] -= 1
            return True
        else:
            return False
    else:
        return False
