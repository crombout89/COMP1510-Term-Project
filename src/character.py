import logging

from .animal import help_animal
from .config import (CHARACTER_DEFAULT_ATTRIBUTES, CHARACTER_DEFAULT_INVENTORY_TOP_LEVEL,
                     CHARACTER_DEFAULT_INVENTORY_BERRIES, UNTIL_NEXT_LEVEL_MULTIPLIER)
from .entity import generate_entity
from .util import dict_from_tuple_of_tuples


def create_character(name: str) -> dict:
    """
    Create a new character with default attributes and a specified name.

    :param name: A string representing the name of the new character.
    :precondition: name must be a non-empty string.
    :postcondition: Returns a dictionary representing the new character with default attributes.
    :return: A dictionary containing the new character's attributes, including the provided name.

    >>> TEST_CHARACTER_DEFAULT_ATTRIBUTES = {
    ...     "Tummy": 10,
    ...     "ExtraEnergy": 0,
    ...     "Inventory": [],
    ...     "GroundCoordinates": [0, 0]
    ... }
    >>> test_new_character = create_character("Whiskers")
    >>> test_new_character["Name"]
    'Whiskers'
    >>> test_new_character["Tummy"]
    10  # Default value
    >>> test_new_character["Inventory"]
    []  # Default empty inventory
    """
    new_character = dict_from_tuple_of_tuples(CHARACTER_DEFAULT_ATTRIBUTES)
    new_character["Inventory"] = dict_from_tuple_of_tuples(CHARACTER_DEFAULT_INVENTORY_TOP_LEVEL)
    new_character["Inventory"]["Berries"] = dict_from_tuple_of_tuples(CHARACTER_DEFAULT_INVENTORY_BERRIES)
    new_character["Name"] = name
    return new_character


def current_location(character: dict) -> tuple[int, int]:
    """
    Retrieve the current coordinates of the character based on their position.

    :param character: A dictionary representing the character's state, including location attributes.
    :precondition: character must have keys "InTree", "TreeCoordinates", and "GroundCoordinates".
    :postcondition: Returns a tuple representing the current coordinates of the character.
    :return: A tuple of two integers representing the character's current location (x, y).

    >>> test_character = {
    ...     "InTree": False,
    ...     "GroundCoordinates": (5, 5),
    ...     "TreeCoordinates": (0, 0)
    ... }
    >>> current_location(test_character)
    (5, 5)

    >>> test_character["InTree"] = True
    >>> test_character["TreeCoordinates"] = (3, 4)
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

    >>> test_character = {
    ...     "Tummy": 10,
    ...     "ExtraEnergy": 0
    ... }
    >>> check_tummy(test_character)
    ⚠️ You're getting hungry! You should eat an item soon to restore your tummy!
    True

    >>> test_character["Tummy"] = 1
    >>> check_tummy(test_character)
    ⚠️ You're about to pass out from hunger! Eat an item now to restore your tummy!
    True

    >>> test_character["Tummy"] = 0
    >>> check_tummy(test_character)
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

    >>> test_character = {
    ...     "Level": 2,
    ...     "UntilNextLevel": 0,
    ...     "FinalChallengeCompleted": None
    ... }
    >>> TEST_UNTIL_NEXT_LEVEL_MULTIPLIER = 10
    >>> update_level(test_character)
    >>> test_character["Level"]
    3
    >>> test_character["UntilNextLevel"]
    30  # Assuming UNTIL_NEXT_LEVEL_MULTIPLIER is set to 10

    >>> test_character["FinalChallengeCompleted"] = None  # Not completed yet
    >>> update_level(test_character)  # Should start the final challenge
    >>> test_character["FinalChallengeCompleted"] is None
    True  # Indicates the final challenge has started
    """
    def print_level_up_message():
        print("\n✨ You Leveled Up! ✨\n")
        if character["Level"] == 2:
            print("You've mastered the art of healing with single berries, and the animals are so grateful!\n"
                  "As you continue your journey, you discover that some ailments require a bit more.\n"
                  "Now, you can use up to 2 berries to create more powerful remedies for your furry friends.\n"
                  "Gather different berries and experiment with combinations to cure even the toughest ailments!\n"
                  "The forest is becoming more vibrant, and your skills are truly blossoming!")
        elif character["Level"] == 3:
            print("\n🌟 Congratulations on reaching Level 3! 🌟")
            print("Your healing abilities have grown immensely!\n"
                  "You've learned how to combine berries and other ingredients from"
                  "your inventory to create unique recipes.")
            # print("Now, you can mix and match items to craft powerful remedies that "
            #       "can help any creature in Whisker Woods.")
            print("The animals are counting on your creativity and wisdom!")
        else:
            print(f"🌟 You are now at level {character['Level']}! 🌟")
        input("Press Enter to continue...")

    if character["UntilNextLevel"] <= 0:
        character["Level"] += 1
        character["UntilNextLevel"] = UNTIL_NEXT_LEVEL_MULTIPLIER * character["Level"]
        print_level_up_message()
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

    >>> test_character = {
    ...     "Tummy": 10,
    ...     "ExtraEnergy": 2
    ... }
    >>> subtract_from_tummy(test_character, 3)
    >>> test_character["Tummy"]
    10  # Tummy remains unchanged because extra energy is available
    >>> test_character["ExtraEnergy"]
    1  # Extra energy is reduced by 1

    >>> test_character["ExtraEnergy"] = 0  # Deplete extra energy
    >>> subtract_from_tummy(test_character, 3)
    >>> test_character["Tummy"]
    7  # Tummy reduced by 3
    """
    logging.info(f"Character: '{character}', Units: {units}")
    if character["ExtraEnergy"] > 0:
        character["ExtraEnergy"] -= 1
    else:
        character["Tummy"] -= units
        if character["Tummy"] < 0:
            character["Tummy"] = 0  # Prevent tummy from going negative


def get_item_from_inventory(character: dict, item: dict) -> bool:
    """
    Retrieve an item from the character's inventory if available.

    :param character: A dictionary representing the character's state, including their inventory.
    :param item: A dictionary representing the item to be retrieved, including its type and name.
    :precondition: character must have an "Inventory" key with appropriate item counts.
    :raises TypeError: if value of key "Type" of item is not "Item".
    :postcondition: Decreases the count of the specified item in the character's inventory if available.
    :return: True if the item was successfully retrieved, False if the item is not available.

    >>> test_character = {
    ...     "Inventory": {
    ...         "Catnip": 2,
    ...         "Silvervine": 1,
    ...         "Berries": {"Red": 3, "Blue": 5}
    ...     }
    ... }
    >>> item_catnip = {"Type": "Item", "Name": "Catnip"}
    >>> get_item_from_inventory(test_character, item_catnip)
    True
    >>> test_character["Inventory"]["Catnip"]
    1  # One less Catnip

    >>> item_silvervine = {"Type": "Item", "Name": "Silvervine"}
    >>> get_item_from_inventory(test_character, item_silvervine)
    True
    >>> character["Inventory"]["Silvervine"]
    0  # Silvervine is now depleted

    >>> item_berry = {"Type": "Item", "Name": "Berry", "Data": "Red"}
    >>> get_item_from_inventory(test_character, item_berry)
    True
    >>> test_character["Inventory"]["Berries"]["Red"]
    2  # One less Red Berry

    >>> item_invalid = {"Type": "Item", "Name": "InvalidItem"}
    >>> get_item_from_inventory(test_character, item_invalid)
    False  # Item is not in the inventory
    """
    logging.info(f"Character: {character}, Item: {item}")
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


def restore_points(character: dict, tummy: int = 0, extra_energy: int = 0):
    """
    Add points to the Tummy and ExtraEnergy of a character.

    :param character: the character to add points to
    :precondition: character must be a well-formed dictionary representing a character
    :param tummy: how many points to add to the Tummy of the character
    :precondition: tummy must be an integer greater than or equal to 0
    :param extra_energy: how many points to add to the ExtraEnergy of the character
    :precondition: extra_energy must be an integer greater than or equal to 0
    :postcondition: adds the specified points to the Tummy and ExtraEnergy of the character
    :raises ValueError: if tummy is less than 0
    :raises ValueError: if extra_energy is less than 0

    >>> example_character = {
    ...     "Tummy": 0,
    ...     "ExtraEnergy": 0,
    ... }
    >>> restore_points(example_character, 1)
    >>> example_character["Tummy"]
    1
    >>> example_character["ExtraEnergy"]
    0
    >>> example_character = {
    ...     "Tummy": 0,
    ...     "ExtraEnergy": 0,
    ... }
    >>> restore_points(example_character, 1, 1)
    >>> example_character["Tummy"]
    1
    >>> example_character["ExtraEnergy"]
    1
    >>> example_character = {
    ...     "Tummy": 0,
    ...     "ExtraEnergy": 0,
    ... }
    >>> restore_points(example_character, extra_energy=1)
    >>> example_character["Tummy"]
    0
    >>> example_character["ExtraEnergy"]
    1
    """
    logging.info(f"Character: '{character}', Tummy: {tummy}, ExtraEnergy: {extra_energy}")
    if tummy < 0:
        raise ValueError("tummy must be an integer greater than or equal to 0")
    if extra_energy < 0:
        raise ValueError("extra_energy must be an integer greater than or equal to 0")
    character["Tummy"] += tummy
    character["ExtraEnergy"] += extra_energy


def start_final_challenge(character: dict) -> None:
    """
    Initialize the final challenge for the character.

    :param character: A dictionary containing information about the player character.
    :precondition: character must be a dictionary with keys for "InTree", "GroundCoordinates",
                   and "FinalChallengeCompleted".
    :raises KeyError: If required keys are missing from the character dictionary.
    :postcondition: Sets up the character for the final challenge by updating relevant keys and printing instructions.

    This function:
    - Sets the "InTree" key to False.
    - Sets the "GroundCoordinates" key to (0, 0).
    - Sets the "FinalChallengeCompleted" key to False.
    - Prints a message to the user explaining the final challenge and how to complete it.

    >>> game_character = {
    ...     "InTree": True,
    ...     "GroundCoordinates": (5, 5),
    ...     "FinalChallengeCompleted": True
    ... }
    >>> start_final_challenge(game_character)
    The final challenge is to find the hidden treasure on the ground.
    Search carefully and use all your skills to complete the task!
    Beware of obstacles and enemies that may block your path.
    >>> game_character["InTree"]
    False
    >>> game_character["GroundCoordinates"]
    (0, 0)
    >>> game_character["FinalChallengeCompleted"]
    False
    """
    def print_final_challenge_instructions():
        print("\n🗣️ You suddenly hear the professor calling you from the center of the forest.")
        print("You drop what you're doing and run to him.")
        print("The Professor is tending to a legendary creature, the Moonlit Lynx, the great protector of the forest.")
        print("The Professor tells you that the Moonlit Lynx is gravely ill.\n"
              "Without the forest's guardian to watch over it, everything will soon wither away.\n"
              "The only way to cure the Lynx is a special recipe of all the different berries in the forest.\n"
              "The recipe needs need two of each coloured berry. No more, no less.\n"
              "The Professor can use his technology to stabilize the Lynx, for now. \n"
              "It's up to you to get the berries!\n"
              "The fate of the forest rests in your paws!\n")
        input("Press Enter to continue...")
    # Ensure required keys are in the character dictionary
    required_keys = ["InTree", "GroundCoordinates", "FinalChallengeCompleted"]
    for key in required_keys:
        if key not in character:
            raise KeyError(f"Missing required key '{key}' in character dictionary.")

    # Update character attributes for the final challenge
    character["InTree"] = False
    character["GroundCoordinates"] = (0, 0)
    character["FinalChallengeCompleted"] = False

    print_final_challenge_instructions()

    help_animal(character, generate_entity({(0, 0): None}, character))
