import copy

from .config import CHARACTER_DEFAULT_ATTRIBUTES, UNTIL_NEXT_LEVEL_MULTIPLIER
from .ui import start_final_challenge


def create_character(name: str) -> dict:
    """
    Create a new character with default attributes and a specified name.

    :param name: A string representing the name of the new character.
    :precondition: name must be a non-empty string.
    :postcondition: Returns a dictionary representing the new character with default attributes.
    :return: A dictionary containing the new character's attributes, including the provided name.

    >>> CHARACTER_DEFAULT_ATTRIBUTES = {
    ...     "Tummy": 10,
    ...     "ExtraEnergy": 0,
    ...     "Inventory": [],
    ...     "GroundCoordinates": [0, 0]
    ... }
    >>> new_character = create_character("Whiskers")
    >>> new_character["Name"]
    'Whiskers'
    >>> new_character["Tummy"]
    10  # Default value
    >>> new_character["Inventory"]
    []  # Default empty inventory
    """
    new_character = copy.deepcopy(CHARACTER_DEFAULT_ATTRIBUTES)
    new_character["Name"] = name
    return new_character


def current_location(character: dict) -> tuple[int, int]:
    """
    Retrieve the current coordinates of the character based on their position.

    :param character: A dictionary representing the character's state, including location attributes.
    :precondition: character must have keys "InTree", "TreeCoordinates", and "GroundCoordinates".
    :postcondition: Returns a tuple representing the current coordinates of the character.
    :return: A tuple of two integers representing the character's current location (x, y).

    >>> character = {
    ...     "InTree": False,
    ...     "GroundCoordinates": (5, 5),
    ...     "TreeCoordinates": (0, 0)
    ... }
    >>> current_location(character)
    (5, 5)

    >>> character["InTree"] = True
    >>> character["TreeCoordinates"] = (3, 4)
    >>> current_location(character)
    (3, 4)
    """
    if character["InTree"]:
        return character["TreeCoordinates"]
    else:
        return character["GroundCoordinates"]


def check_tummy(character: dict) -> bool:
    """
    Check the character's tummy level and determine if they are in a hungry state.

    :param character: A dictionary representing the character's state, including tummy and energy levels.
    :precondition: character must have the keys "Tummy" and "ExtraEnergy".
    :postcondition: Displays warnings based on the character's tummy level.
    :return: True if the character is safe (not starving) or has extra energy; False if the character's
             tummy is empty.

    >>> character = {
    ...     "Tummy": 10,
    ...     "ExtraEnergy": 0
    ... }
    >>> check_tummy(character)
    ⚠️ You're getting hungry! You should eat an item soon to restore your tummy!
    True

    >>> character["Tummy"] = 1
    >>> check_tummy(character)
    ⚠️ You're about to pass out from hunger! Eat an item now to restore your tummy!
    True

    >>> character["Tummy"] = 0
    >>> check_tummy(character)
    False
    """
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
    """
    Update the character's current level based on experience points and check for the final challenge.

    :param character: A dictionary representing the character's state, including level and challenge status.
    :precondition: character must have keys "Level", "UntilNextLevel", and "FinalChallengeCompleted".
    :postcondition: Increments the character's level if the threshold is met and checks if the final challenge
                    should start.
    :return: True if the character has completed the final challenge, False otherwise.

    >>> character = {
    ...     "Level": 2,
    ...     "UntilNextLevel": 0,
    ...     "FinalChallengeCompleted": None
    ... }
    >>> UNTIL_NEXT_LEVEL_MULTIPLIER = 10
    >>> update_level(character)
    >>> character["Level"]
    3
    >>> character["UntilNextLevel"]
    30  # Assuming UNTIL_NEXT_LEVEL_MULTIPLIER is set to 10

    >>> character["FinalChallengeCompleted"] = None  # Not completed yet
    >>> update_level(character)  # Should start the final challenge
    >>> character["FinalChallengeCompleted"] is None
    True  # Indicates the final challenge has started

    >>> character["FinalChallengeCompleted"] = True
    >>> update_level(character)  # Should return True now
    True
    """
    if character["UntilNextLevel"] <= 0:
        character["Level"] += 1
        character["UntilNextLevel"] = UNTIL_NEXT_LEVEL_MULTIPLIER * character["Level"]
    if character["Level"] == 3 and character["FinalChallengeCompleted"] is None:
        start_final_challenge(character)
    else:
        return character["Level"] == 3 and character["FinalChallengeCompleted"]


def subtract_from_tummy(character: dict, units: int):
    """
    Decrease the character's tummy level by a specified number of units, prioritizing extra energy
    if available.

    :param character: A dictionary representing the character's state, including tummy and energy levels.
    :param units: An integer representing the number of units to subtract from the tummy level when extra
                  energy is depleted.
    :precondition: character must have keys "Tummy" and "ExtraEnergy".
    :precondition: units must be a non-negative integer.
    :postcondition: Reduces the character's tummy or extra energy based on availability.

    >>> character = {
    ...     "Tummy": 10,
    ...     "ExtraEnergy": 2
    ... }
    >>> subtract_from_tummy(character, 3)
    >>> character["Tummy"]
    10  # Tummy remains unchanged because extra energy is available
    >>> character["ExtraEnergy"]
    1  # Extra energy is reduced by 1

    >>> character["ExtraEnergy"] = 0  # Deplete extra energy
    >>> subtract_from_tummy(character, 3)
    >>> character["Tummy"]
    7  # Tummy reduced by 3
    """
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
