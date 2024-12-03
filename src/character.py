import copy

from .config import CHARACTER_DEFAULT_ATTRIBUTES, UNTIL_NEXT_LEVEL_MULTIPLIER
from .ui import start_final_challenge


def create_character(name: str) -> dict:
    new_character = copy.deepcopy(CHARACTER_DEFAULT_ATTRIBUTES)
    new_character["Name"] = name
    return new_character


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
            print("⚠️ You're getting hungry! You should eat an item soon to restore your tummy!")
            return True
        elif character["Tummy"] == 1:
            print("⚠️ You're about to pass out from hunger! Eat an item now to restore your tummy!")
            return True
        else:
            return character["Tummy"] > 0


def update_level(character: dict) -> bool:
    if character["UntilNextLevel"] <= 0:
        character["Level"] += 1
        character["UntilNextLevel"] = UNTIL_NEXT_LEVEL_MULTIPLIER * character["Level"]
    if character["Level"] == 3 and character["FinalChallengeCompleted"] is None:
        start_final_challenge(character)
    else:
        return character["Level"] == 3 and character["FinalChallengeCompleted"]


def subtract_from_tummy(character: dict, units: int):
    if character["ExtraEnergy"] > 0:
        character["ExtraEnergy"] -= 1
    else:
        character["Tummy"] -= units


def get_item_from_inventory(character: dict, item: dict) -> bool:
    """
    :raises TypeError: if value of key "Type" of item is not "Item"
    """
    if item["Type"] != "Item":
        raise TypeError(f"Expected entity type 'Item', got '{item['Type']}'")
    if item["Name"] == "Catnip" or item["Name"] == "Silvervine":
        if character["Inventory"][item["Name"]] > 0:
            character["Inventory"][item["Name"]] -= 1
            return True
        else:
            return False
    elif item["Name"] == "Berry":
        try:
            berry_in_inventory = character["Inventory"]["Berries"][item["Data"]]
        except KeyError:
            return False
        else:
            if berry_in_inventory > 0:
                character["Inventory"]["Berries"][item["Data"]] -= 1
                return True
            else:
                return False
    else:
        return False
