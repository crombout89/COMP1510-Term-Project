import random
import logging

from .character import current_location
from .config import GROUND_X_SCALE, GROUND_Y_SCALE, TREE_SCALE_OPTIONS
from .description import forest_patch_description, tree_patch_description, moss_description


def generate_board(min_x: int, max_x: int, min_y: int, max_y: int) -> dict:
    """
    Generate an empty board of the specified coordinate range.

    :param min_x: the minimum x coordinate of the board
    :precondition: min_x must be an integer less than or equal to max_x
    :param max_x: the maximum x coordinate of the board
    :precondition: max_x must be an integer greater than or equal to min_x
    :param min_y: the minimum y coordinate of the board
    :precondition: min_y must be an integer less than or equal to max_y
    :param max_y: the maximum y coordinate of the board
    :precondition: max_y must be an integer greater than or equal to min_y
    :postcondition: generates a grid of coordinates with x coordinates from min_x to max_x,
                    and y coordinates from min_y max_y
    :return: a dictionary with a "meta" key containing a nested dictionary with the maximum and minimum x and y
             coordinates; and a set of tuple keys representing an x and y coordinate, and whose values are None
    :raises ValueError: if min_x is greater than max_x
    :raises ValueError: if min_y is greater than max_y

    >>> generate_board(-1, 1, -1, 1)
    {"meta": {"min_x": -1, "max_x": 1, "min_y": -1, "max_y": 1},
     (-1, -1): None, (-1, 0): None, (-1, 1): None, (0, -1): None, (0, 0): None, (0, 1): None,
     (1, -1): None, (1, 0): None, (1, 1): None}
    >>> generate_board(-2, 2, -1, 1)
    {"meta": {"min_x": -2, "max_x": 2, "min_y": -1, "max_y": 1},
     (-2, -1): None, (-2, 0): None, (-2, 1): None, (-1, -1): None, (-1, 0): None, (-1, 1): None,
     (0, -1): None, (0, 0): None, (0, 1): None, (1, -1): None, (1, 0): None, (1, 1): None,
     (2, -1): None, (2, 0): None, (2, 1): None}
    >>> generate_board(-1, 1, -2, 2)
    {"meta": {"min_x": -1, "max_x": 1, "min_y": -2, "max_y": 2},
     (-1, -2): None, (-1, -1): None, (-1, 0): None, (-1, 1): None, (-1, 2): None, (0, -2): None,
     (0, -1): None, (0, 0): None, (0, 1): None, (0, 2): None, (1, -2): None, (1, -1): None,
     (1, 0): None, (1, 1): None, (1, 2): None}
    """
    if min_x > max_x:
        raise ValueError("min_x must be less than or equal to max_x")
    if min_y > max_y:
        raise ValueError("min_y must be less than or equal to max_y")

    board = {
        "meta": {
            "min_x": min_x,
            "max_x": max_x,
            "min_y": min_y,
            "max_y": max_y
        }
    }

    # Initialize all tiles as None
    for current_x in range(min_x, max_x + 1):
        for current_y in range(min_y, max_y + 1):
            board[(current_x, current_y)] = None

    return board


def populate_board(board: dict, name: str, times: int, animal_data=None):
    """
    Populate the game board with a specified entity at random coordinates.

    :param board: A dictionary representing the game board, including metadata and tile states.
    :param name: A string representing the name of the entity to place on the board.
    :param times: An integer representing the number of times the entity will be placed on the board.
    :param animal_data: Optional data specific to the type of entity being placed (e.g., for animals).
    :precondition: board must have a "meta" key with "min_x", "max_x", "min_y", and "max_y" values.
    :precondition: times must be a positive, non-zero integer.
    :postcondition: Places the entity on the board at random coordinates, ensuring no overlap with
                    existing entities or the reserved tile (0, 0).

    >>> game_board = {
    ...     "meta": {"min_x": 1, "max_x": 5, "min_y": 1, "max_y": 5},
    ...     (1, 1): None,
    ...     (2, 2): None,
    ...     (0, 0): None  # Reserved tile
    ... }
    >>> populate_board(game_board, "TreeTrunk", 3)
    >>> reserved_tile_check = (0, 0) in game_board and game_board[(0, 0)] is None
    True  # Reserved tile remains unchanged
    """
    if times <= 0:
        raise ValueError("Times must be a positive, non-zero integer.")

    # Calculate available spaces
    valid_tiles = [
        (x, y) for x in range(board["meta"]["min_x"], board["meta"]["max_x"] + 1)
        for y in range(board["meta"]["min_y"], board["meta"]["max_y"] + 1)
        if (x, y) != (0, 0) and board.get((x, y)) is None
    ]

    if len(valid_tiles) < times:
        raise ValueError(f"Not enough valid spaces to place {times} {name}(s). Available: {len(valid_tiles)}")

    counter = 0
    max_attempts = 100  # Limit attempts to avoid infinite loops
    attempts = 0

    while counter < times and attempts < max_attempts:
        coordinate = random.choice(valid_tiles)

        if coordinate != (0, 0) and board.get(coordinate) is None:
            if animal_data:
                board[coordinate] = {"name": name, "data": animal_data}  # Use a dict to store both name and data
            else:
                board[coordinate] = name  # Just place the name if no data
            counter += 1
        attempts += 1

    if attempts == max_attempts:
        logging.warning("Warning: Maximum attempts reached. Some entities may not have been placed.")


def generate_ground_board() -> dict:
    """
    Generate a ground board with tree trunks and randomized forest patch descriptions for empty tiles.

    :postcondition: The board includes a random number of "TreeTrunk" entities and randomized forest patch descriptions
                    for empty tiles.
    :return: A dictionary representing the generated ground board with entities and descriptions.

    >>> ground_board_result = generate_ground_board()  # Generate the ground board
    >>> "TreeTrunk" in ground_board_result.values()  # Check that TreeTrunks exist
    True
    >>> test_tree_trunk_count = sum(1 for tile in ground_board_result.values() if tile == "TreeTrunk")  # Count TreeTrunks
    30 <= tree_trunk_count <= 60  # Randomized, skip the exact count check
    """
    ground_board = generate_board(-GROUND_X_SCALE, GROUND_X_SCALE, -GROUND_Y_SCALE, GROUND_Y_SCALE)
    tree_trunk_count = random.randint(30, 60)

    # Populate board with tree trunks
    populate_board(ground_board, "TreeTrunk", tree_trunk_count)

    return ground_board


def generate_tree_board() -> dict:
    """
    Generate a tree board with a central tree trunk and moss.

    :postcondition: The board includes one "TreeTrunk" at the center and a random number of "Moss" entities.
    :return: A dictionary representing the generated tree board with entities.

    >>> tree_board_result = generate_tree_board()
    >>> tree_board_result[(0, 0)] == "TreeTrunk"
    True  # The center should contain a TreeTrunk
    >>> test_moss_count = sum(1 for tile in tree_board_result.values() if tile == "Moss")
    0 <= test_moss_count <= tree_scale  # Number of Moss entities should be within the expected range
    """
    tree_scale = random.choice(TREE_SCALE_OPTIONS)
    # Ensure at least one moss tile is placed
    moss_count = random.randint(1, tree_scale)  # Ensure moss_count is at least 1

    tree_board = generate_board(-tree_scale, tree_scale, -tree_scale, tree_scale)

    # Place the central TreeTrunk
    tree_board[(0, 0)] = "TreeTrunk"

    # Populate Moss tiles randomly
    populate_board(tree_board, "Moss", moss_count)

    return tree_board


def valid_location(board: dict, coordinates: tuple[int, int]) -> bool:
    """
    Check if the specified coordinates are valid locations on the board.

    :param board: A dictionary representing the game board.
    :param coordinates: A tuple of integers representing the coordinates to check.
    :return: True if the coordinates are valid, False otherwise.

    >>> game_board = {
    ...     (1, 1): None,
    ...     (0, 0): "Reserved",
    ...     (2, 2): "TreeTrunk"
    ... }
    >>> valid_location(board, (1, 1))
    True  # (1, 1) is a valid location
    >>> valid_location(board, (3, 3))
    False  # (3, 3) does not exist on the board
    >>> valid_location(board, (0, 0))
    True  # (0, 0) is valid but reserved
    """
    return coordinates in board


def describe_current_location(character: dict, board: dict) -> str:
    """
    Describe the current location of the character based on their state.

    :param character: A dictionary representing the character's state, including whether they are in a tree.
    :return: A string description of the current location.

    >>> my_character = {"InTree": False}
    >>> describe_current_location(my_character)
    'You are in a forest: A patch of soft green grass sways gently in the breeze.🌱'
    >>> my_character["InTree"] = True
    >>> describe_current_location(my_character)
    'You are in a treetop: The treetop sways gently in the breeze, a serene spot high above the ground.🍃🌬️'
    """
    board_description = board[current_location(character)]
    logging.info(f"Current location: {current_location(character)}, Description: {board_description}")
    if board_description == "TreeTrunk":
        print("🌲 You're at a tree trunk, you can climb up or down the tree.")
    elif board_description == "Moss":
        print("🌿 You're in a patch of moss. You can take a nap to get extra energy.")
    elif character["InTree"]:
        print(tree_patch_description())
    else:
        print(forest_patch_description())

