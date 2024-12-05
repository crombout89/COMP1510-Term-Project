import itertools
import logging

from .board import valid_location, current_location
from .character import subtract_from_tummy, restore_points
from .config import (SUBTRACT_FROM_TUMMY_IF_MOVE, ADD_TO_TUMMY_IF_EAT_ITEM, CATNIP_EXTRA_ENERGY,
                     SILVERVINE_EXTRA_ENERGY, NAP_EXTRA_ENERGY, CATNIP_TUMMY_MULTIPLIER, SILVERVINE_TUMMY_MULTIPLIER,
                     DIRECTION_MAPPING)
from .entity import stringify_item, get_item_from_inventory
from .util import plural, dict_from_tuple_of_tuples


def move(character: dict, board: dict, direction: tuple[int, int]) -> bool:
    """
    Move the character in the specified direction if the new location is valid.

    :param character: A dictionary representing the character's state, including its current coordinates.
    :param board: A dictionary representing the game board with valid location.
    :param direction: A tuple indicating the direction to move (x, y).
    :precondition: character must have keys for "InTree" and appropriate coordinate keys ("GroundCoordinates
                    or "TreeCoordinates")
    :precondition: board must be a valid representation of the game area.
    :postcondition: Updates the character's coordinates if the move is valid, and subtracts from the character's
                    Tummy Meter.
    :return: True if the move was successful, False otherwise.

    >>> game_character = {
    ...     "InTree": False,
    ...     "GroundCoordinates": [5, 5]
    ... }
    >>> game_board = {
    ...     (5, 5): "Empty",
    ...     (6, 5): "Empty",
    ...     (6, 5): "TreeTrunk"  # Assuming (6, 5) has a tree trunk
    ... }
    >>> move(character, board, (1, 0))  # Move right
    True
    >>> game_character["GroundCoordinates"]
    [6, 5]
    >>> move(character, board, (1, 0))  # Attempt to move right into a tree trunk
    False
    >>> game_character["GroundCoordinates"]
    [6, 5]
    """
    coordinate_type = ("Tree" if character["InTree"] else "Ground") + "Coordinates"
    new_coordinates = (character[coordinate_type][0] + direction[0],
                       character[coordinate_type][1] + direction[1])
    if valid_location(board, new_coordinates):
        character[coordinate_type] = new_coordinates
        subtract_from_tummy(character, SUBTRACT_FROM_TUMMY_IF_MOVE)
        return True
    else:
        print("🚫 You're at the edge of the map and can't move in that direction!")
        return False


def how_to_get_to_center(location: tuple[int, int]) -> str:
    """
    Tells the user how to get to the center of the board.

    Assumes that the center of the board is at coordinates (0, 0).

    Returns an empty string if location is already at the center

    :param location: a tuple representing a coordinate
    :precondition: location must be a tuple of two integers where
    :postcondition: determines how to get to the center of the board
    :return: a string telling the user how many tiles to move and in what direction to get to the center of the board

    >>> how_to_get_to_center((-2, -1))
    "2 tiles right and 1 tile down"
    >>> how_to_get_to_center((3, 0))
    "3 tiles left"
    >>> how_to_get_to_center((0, 4))
    "4 tiles up"
    """
    instruction_tokens = []
    if location[0] < 0:
        # If x coordinate is negative, they are in the left half of the map and need to go right
        instruction_tokens.append(f"{abs(location[0])} tile{plural(abs(location[0]))} right")
    elif location[0] > 0:
        # If x coordinate is positive, they are in the right half of the map and need to go left
        instruction_tokens.append(f"{abs(location[0])} tile{plural(abs(location[0]))} left")

    if location[1] < 0:
        # If x coordinate is negative, they are in the top half of the map and need to go down
        instruction_tokens.append(f"{abs(location[1])} tile{plural(abs(location[1]))} down")
    elif location[1] > 0:
        # If x coordinate is positive, they are in the bottom half of the map and need to go up
        instruction_tokens.append(f"{abs(location[1])} tile{plural(abs(location[1]))} up")

    if len(instruction_tokens) == 2:
        return f"{instruction_tokens[0]} and {instruction_tokens[1]}"
    elif len(instruction_tokens) == 1:
        return instruction_tokens[0]
    else:
        return ""


def check(character: dict, attribute: str) -> None:
    """
    Check a specific attribute of the character and display its value.

    :param character: A dictionary containing information about the player character.
    :param attribute: The attribute to check (e.g., 'Tummy', 'Level', 'Inventory').
    :precondition: character must be a dictionary containing the relevant attributes.
    :precondition: attribute must be a string representing a valid character attribute.
    :postcondition: Displays the value of the specified attribute.
    :raises ValueError: If the specified attribute does not exist in the character dictionary.
    :raises ValueError: If the attribute name is invalid or unsupported.

    >>> game_character = {
    ...     "Tummy": 50,
    ...     "Level": 2,
    ...     "Inventory": ["Catnip", "Silvervine"]
    ... }
    >>> check(character, "Tummy")
    Your tummy level is: 50
    >>> check(character, "Level")
    Your current level is: 2
    >>> check(character, "Inventory")
    Your inventory contains:
     - Catnip
     - Silvervine
    """
    def check_tummy_and_extra_energy():
        print(f"Your tummy level is: {character['Tummy']}")
        if character['ExtraEnergy'] > 0:
            print(f"You have extra energy for the next {character['ExtraEnergy']} move(s).")

    def check_level():
        print(f"Your current level is: {character['Level']}.\n"
              f"You have to help {character['UntilNextLevel']} more animals to level up.")

    def check_inventory():
        print("Your inventory contains:")
        top_level_items = [item for item in character["Inventory"].items() if type(item[1]) is int]
        berries = map(lambda b: (f"{b[0]} Berry" if b[1] == 1 else f"{b[0]} Berries", b[1]),
                      character["Inventory"]["Berries"].items())
        for inventory_item in itertools.chain(top_level_items, berries):
            print(f" - {inventory_item[1]} {inventory_item[0]}")

    def check_location():
        location = current_location(character)
        if character["InTree"]:
            print("You're in a tree.")
            print(f"Your current coordinates are {location}")
            if location == (0, 0):
                print("You're at the center of the tree and can climb down.")
            else:
                print("If you want to climb down, you have to go to the center of the tree at (0, 0)\n"
                      f"  Hint: Go {how_to_get_to_center(location)}.")
        else:
            print("You're on the ground.")
            print(f"Your current coordinates are {location}")
            if location == (0, 0):
                print("You're at the center of the forest.")
            elif character["FinalChallengeCompleted"] is False:
                print("If you want to attempt the final challenge,"
                      "you need to go to the center of the forest at (0, 0).\n"
                      f"  Hint: Go {how_to_get_to_center(location)}.")

    valid_attributes = {
        # "Attribute name": the_closure_to_call
        "Tummy": check_tummy_and_extra_energy,
        "Level": check_level,
        "Inventory": check_inventory,
        "Location": check_location,
    }

    # Ensure the attribute is valid
    if attribute in valid_attributes:
        valid_attributes[attribute]()
    else:
        print(f"🚫 '{attribute}' is not a supported attribute to check!")


def climb(character: dict, board) -> bool:
    """
    Allow the character to climb a tree trunk if they are currently at one.

    :param character: A dictionary representing the character's state, including if they are in a tree.
    :param board: A dictionary representing the game board with location.
    :precondition: character must have keys for "InTree" and "TreeCoordinates".
    :precondition: board must represent a valid location, including "TreeTrunk".
    :postcondition: Updates the character's state as being in a tree, and subtracts from the character's
                    Tummy Meter.
    :return: True if the climb was successful, False if the character is not at a tree trunk.

    >>> game_character = {
    ...     "InTree": False,
    ...     "TreeCoordinates": (5, 5)
    ... }
    >>> game_board = {
    ...     (5, 5): "TreeTrunk",
    ...     (6, 5): None
    ... }
    >>> climb(character, board)  # At tree trunk
    True
    >>> game_character["InTree"]
    True
    >>> climb(character, board)  # Climbing again
    True
    >>> game_character["InTree"]
    False
    >>> game_character = {
    ...     "InTree": False,
    ...     "TreeCoordinates": (6, 5)
    ... }
    >>> game_board = {
    ...     (5, 5): "TreeTrunk",
    ...     (6, 5): None
    ... }
    >>> climb(character, board)  # Attempt to climb again without being at a tree trunk
    False
    🚫 You can't climb because you're not at a tree trunk!
    """
    if board[current_location(character)] == "TreeTrunk":
        if character["InTree"]:
            character["InTree"] = False
            print("You climbed down the tree.")
            logging.info(f"Climbing down, Character: {character}")
        else:
            character["TreeCoordinates"] = (0, 0)
            character["InTree"] = True
            print("You climbed up the tree.")
            logging.info(f"Climbing up, Character: {character}")
        return True
    else:
        print("🚫 You can't climb because you're not at a tree trunk!")
        return False


def eat(character: dict, item: dict) -> bool:
    """
    Allow the character to eat an item, updating their energy and tummy levels.

    :param character: A dictionary representing the character's state, including energy and tummy levels.
    :param item: A dictionary representing the item to be eaten, which must have a "Type" and "Name".
    :precondition: item must have a "Type" key with value "Item" for successful consumption.
    :raises TypeError: if value of key "Type" of item is not "Item".
    :postcondition: Updates the character's energy and tummy levels based on the item consumed.
    :return: True if item was successfully eaten, False if the item is not in the inventory.

    >>> game_character = {
    ...     "Tummy": 5,
    ...     "ExtraEnergy": 10,
    ...     "Inventory": {
    ...         "Silvervine": 1,
    ...         "Catnip": 0
    ...     }
    ... }
    >>> game_item = {
    ...     "Type": "Item",
    ...     "Name": "Silvervine"
    ... }
    >>> eat(game_character, game_item)
    True
    >>> game_character["Tummy"]
    105
    >>> game_character["ExtraEnergy"]
    60
    >>> game_character["Inventory"]["Silvervine"]
    0

    >>> game_item_2 = {
    ...     "Type": "Item",
    ...     "Name": "Catnip"
    ... }
    >>> eat(game_character, game_item_2)  # Attempt to eat an item not in inventory
    False
    >>> game_character["Tummy"]
    105
    >>> game_character["ExtraEnergy"]
    60
    """
    if item["Type"] != "Item":
        raise TypeError(f"Expected entity type 'Item', got '{item['Type']}'")
    if get_item_from_inventory(character, item):
        if item["Name"] == "Silvervine":
            restore_points(character, ADD_TO_TUMMY_IF_EAT_ITEM * SILVERVINE_TUMMY_MULTIPLIER, SILVERVINE_EXTRA_ENERGY)
        elif item["Name"] == "Catnip":
            restore_points(character, ADD_TO_TUMMY_IF_EAT_ITEM * CATNIP_TUMMY_MULTIPLIER, CATNIP_EXTRA_ENERGY)
        else:
            restore_points(character, ADD_TO_TUMMY_IF_EAT_ITEM)
        print(f"🍽️ You ate a {stringify_item(item)}.\n",
              f"⚡ Your Tummy is now at {character['Tummy']} and you have {character['ExtraEnergy']} extra energy.")
        return True
    else:
        print("🚫 You can't eat this item because it's not in your inventory!")
        return False


def nap(character: dict, board: dict) -> bool:
    """
    Allow the character to take a nap on moss, restoring extra energy.

    :param character: A dictionary representing the character's state, including energy levels.
    :param board: A dictionary representing the game board with locations, including mossy squares.
    :precondition: character must have a key "ExtraEnergy" to track energy levels.
    :precondition: board must be a dictionary representing the game board with locations.
    :postcondition: Increases the character's extra energy if napping on moss.
    :return: True if the nap was successful, False if the character is not on moss.

    >>> game_character = {
    ...     "ExtraEnergy": 0
    ... }
    >>> game_board = {
    ...     (5, 5): "Moss",
    ...     (6, 5): "Empty"
    ... }
    >>> game_current_location = lambda game_character: (5, 5)  # Mocking the current_location function
    >>> nap(character, board)
    😴 You took a nap on the moss.
    ⚡ You now have extra energy for 5 moves!
    True
    >>> game_character["ExtraEnergy"]
    5

    >>> character["ExtraEnergy"] = 0  # Reset energy for next test
    >>> game_current_location = lambda game_character: (6, 5)  # Move to a different location
    >>> nap(character, board)  # Attempt to nap on "Empty"
    🚫 You can't nap here because you're not on moss!
    False
    """
    location = current_location(character)

    # Check if the character is in a tree and the current location is moss
    if character["InTree"] and board.get(location) == "Moss":
        restore_points(character, extra_energy=NAP_EXTRA_ENERGY)  # Only restore extra energy
        print("😴 You took a nap on the moss.")
        print(f"⚡ You now have extra energy for {NAP_EXTRA_ENERGY} moves!")
        return True
    else:
        print("🚫 You can't nap here because you're not in a tree or not on moss!")
        return False


def perform_action(character: dict, board: dict, action: dict) -> bool:
    """
    Execute a specified action for the character based on the action type.

    :param character: A dictionary representing the character's state, including position and attributes.
    :param board: A dictionary representing the game board with locations.
    :param action: A dictionary representing the action to be performed, including its type and associated
                   data.
    :precondition: character must have the necessary keys related to its actions (e.g. "Inventory",
                   "GroundCoordinates").
    :precondition: board must be a valid dictionary where the keys are coordinates and values are the types
                   of terrain or obstacles.
    :precondition: action dictionary must have a "Type" key that indicates the action type (e.g. "Move", "Climb"
                   "Eat", "Nap").
    :postcondition: Executes the corresponding function for the specified action type.
    :return: True if the action was successfully performed, False if the action type is invalid or unsuccessful.
    >>> game_character = {
    ...     "Tummy": 5,
    ...     "ExtraEnergy": 10,
    ...     "GroundCoordinates": [5, 5],
    ...     "Inventory": []
    ... }
    >>> game_board = {
    ...     (5, 5): "Moss",
    ...     (6, 5): "Empty"
    ... }
    >>> action_move = {"Type": "Move", "data": (1, 0)}
    >>> perform_action(character, board, action_move)  # Move right
    True
    >>> character["GroundCoordinates"]
    [6, 5]

    >>> action_climb = {"Type": "Climb"}
    >>> perform_action(character, board, action_climb)  # Climb a tree
    True

    >>> action_eat = {"Type": "Eat", "data": {"Type": "Item", "Name": "Silvervine"}}
    >>> character["Inventory"].append(action_eat["data"])  # Add item to inventory
    >>> perform_action(character, board, action_eat)
    True

    >>> action_nap = {"Type": "Nap"}
    >>> perform_action(character, board, action_nap)  # Take a nap
    😴 You took a nap on the moss.
    ⚡ You now have extra energy for 5 moves!
    True

    >>> action_invalid = {"Type": "Dance"}
    >>> perform_action(character, board, action_invalid)  # Invalid action
    🚫 You can't perform this action!
    False
    """
    if action["Type"] == "Move":
        return move(character, board, action["Data"])
    elif action["Type"] == "Climb":
        return climb(character, board)
    elif action["Type"] == "Eat":
        return eat(character, action["Data"])
    elif action["Type"] == "Nap":
        return nap(character, board)
    else:
        print("🚫 You can't perform this action!")
        return False


def direction_input_to_action(direction_input: str) -> dict:
    """
    Determines the correct action dictionary for a selected movement direction.

    Uses WASD mapping, where W is up, A is left, S is down, and D is right.

    :param direction_input: a string representing the selected direction
    :precondition: direction_input must be one of "W", "A", "S" or "D" (non-case-sensitive)
    :postcondition: determines the correct action for the chosen direction
    :raises ValueError: if direction_input is not one of "W", "A", "S" or "D"
    :return: an action dictionary with "Move" as the key "Type" and the correct direction vector as the key "Data"

    >>> direction_input_to_action("W")
    {'Type': 'Move', 'Data': (0, -1)}
    >>> direction_input_to_action("A")
    {'Type': 'Move', 'Data': (-1, 0)}
    >>> direction_input_to_action("S")
    {'Type': 'Move', 'Data': (0, 1)}
    """
    action = {
        "Type": "Move"
    }
    try:
        action["Data"] = dict_from_tuple_of_tuples(DIRECTION_MAPPING)[direction_input.upper()]
    except KeyError:
        raise ValueError("Invalid direction input")
    else:
        return action
