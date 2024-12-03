from .board import valid_location
from .character import current_location, get_item_from_inventory, subtract_from_tummy
from .config import (SUBTRACT_FROM_TUMMY_IF_CLIMB, SUBTRACT_FROM_TUMMY_IF_MOVE,
                     ADD_TO_TUMMY_IF_EAT_ITEM, CATNIP_EXTRA_ENERGY, SILVERVINE_EXTRA_ENERGY,
                     CATNIP_TUMMY_MULTIPLIER, SILVERVINE_TUMMY_MULTIPLIER)


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

    >>> character = {
    ...     "InTree": False,
    ...     "GroundCoordinates": [5, 5]
    ... }
    >>> board = {
    ...     (5, 5): "Empty",
    ...     (6, 5): "Empty",
    ...     (6, 5): "TreeTrunk"  # Assuming (6, 5) has a tree trunk
    ... }
    >>> move(character, board, (1, 0))  # Move right
    True
    >>> character["GroundCoordinates"]
    [6, 5]
    >>> move(character, board, (1, 0))  # Attempt to move right into a tree trunk
    False
    >>> character["GroundCoordinates"]
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
        return False


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

    >>> character = {
    ...     "InTree": False,
    ...     "TreeCoordinates": (0, 0)
    ... }
    >>> board = {
    ...     (5, 5): "TreeTrunk",
    ...     (6, 5): "Empty"
    ... }
    >>> climb(character, board)  # At tree trunk
    True
    >>> character["InTree"]
    True
    >>> climb(character, board)  # Climbing again
    True
    >>> character["InTree"]
    False
    >>> climb(character, board)  # Attempt to climb again without being at a tree trunk
    False
    🚫 You can't climb because you're not at a tree trunk!
    """
    location = current_location(character)
    if board[location] == "TreeTrunk":
        if character["InTree"]:
            character["InTree"] = False
        else:
            character["TreeCoordinates"] = (0, 0)
            character["InTree"] = True
        subtract_from_tummy(character, SUBTRACT_FROM_TUMMY_IF_CLIMB)
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

        >>> character = {
    ...     "Tummy": 5,
    ...     "ExtraEnergy": 10,
    ...     "Inventory": []
    ... }
    >>> item = {
    ...     "Type": "Item",
    ...     "Name": "SilverVine"
    ... }
    >>> character["Inventory"].append(item)
    >>> eat(character, item)
    True
    >>> character["Tummy"]
    15  # Assuming SILVERVINE_TUMMY_MULTIPLIER is set accordingly
    >>> character["ExtraEnergy"]
    15  # Assuming SILVERVINE_EXTRA_ENERGY is set accordingly

    >>> item_invalid = {
    ...     "Type": "Food",
    ...     "Name": "Apple"
    ... }
    >>> eat(character, item_invalid)  # Raises TypeError
    Traceback (most recent call last):
        ...
    TypeError: Expected entity type 'Item', got 'Food'

    >>> item2 = {
    ...     "Type": "Item",
    ...     "Name": "Catnip"
    ... }
    >>> character["Inventory"].append(item2)  # Add item to inventory
    >>> eat(character, item2)
    True
    >>> character["Tummy"]
    10  # Assuming CATNIP_TUMMY_MULTIPLIER is set accordingly
    """
    if item["Type"] != "Item":
        raise TypeError(f"Expected entity type 'Item', got '{item['Type']}'")
    if get_item_from_inventory(character, item):
        if item["Name"] == "SilverVine":
            character["ExtraEnergy"] += SILVERVINE_EXTRA_ENERGY
            character["Tummy"] += ADD_TO_TUMMY_IF_EAT_ITEM * SILVERVINE_TUMMY_MULTIPLIER
        elif item["Name"] == "Catnip":
            character["ExtraEnergy"] += CATNIP_EXTRA_ENERGY
            character["Tummy"] += ADD_TO_TUMMY_IF_EAT_ITEM * CATNIP_TUMMY_MULTIPLIER
        else:
            character["Tummy"] += ADD_TO_TUMMY_IF_EAT_ITEM
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

    >>> character = {
    ...     "ExtraEnergy": 0
    ... }
    >>> board = {
    ...     (5, 5): "Moss",
    ...     (6, 5): "Empty"
    ... }
    >>> current_location = lambda character: (5, 5)  # Mocking the current_location function
    >>> nap(character, board)
    😴 You took a nap on the moss.
    ⚡ You now have extra energy for 5 moves!
    True
    >>> character["ExtraEnergy"]
    5

    >>> character["ExtraEnergy"] = 0  # Reset energy for next test
    >>> current_location = lambda character: (6, 5)  # Move to a different location
    >>> nap(character, board)  # Attempt to nap on "Empty"
    🚫 You can't nap here because you're not on moss!
    False
    """
    location = current_location(character)
    if board[location] == "Moss":
        character["ExtraEnergy"] += 5
        print("😴 You took a nap on the moss.")
        print("⚡ You now have extra energy for 5 moves!")
        return True
    else:
        print("🚫 You can't nap here because you're not on moss!")
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
        >>> character = {
    ...     "Tummy": 5,
    ...     "ExtraEnergy": 10,
    ...     "GroundCoordinates": [5, 5],
    ...     "Inventory": []
    ... }
    >>> board = {
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

    >>> action_eat = {"Type": "Eat", "data": {"Type": "Item", "Name": "SilverVine"}}
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
    """
    if action["Type"] == "Move":
        return move(character, board, action["data"])
    elif action["Type"] == "Climb":
        return climb(character, board)
    elif action["Type"] == "Eat":
        return eat(character, action["data"])
    elif action["Type"] == "Nap":
        return nap(character, board)
    else:
        print("🚫 You can't perform this action!")
        return False
