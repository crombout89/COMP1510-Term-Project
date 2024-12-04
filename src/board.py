import random

from .config import GROUND_X_SCALE, GROUND_Y_SCALE, TREE_SCALE_OPTIONS
from .descriptions import forest_patch_description, tree_patch_description, moss_description


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

    for current_x in range(min_x, max_x + 1):
        for current_y in range(min_y, max_y + 1):
            board[(current_x, current_y)] = "An empty patch of grass sways gently in the breeze."

    return board


def populate_board(board: dict, name: str, times: int):
    """
    Populate the game board with a specified entity at random coordinates.

    :param board: A dictionary representing the game board, including metadata and tile states.
    :param name: A string representing the name of the entity to place on the board.
    :param times: An integer representing the number of times the entity will be placed on the board.
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
    >>> populate_board(game_board, "Tree", 3)
    >>> tree_count = sum(1 for tile in game_board.values() if tile == "Tree")
    3  # Should place 3 Trees on the board
    >>> reserved_tile_check = (0, 0) in game_board and game_board[(0, 0)] is None
    True  # Reserved tile remains unchanged
    """
    counter = 1
    while counter <= times:
        x_coordinate = random.randint(board["meta"]["min_x"], board["meta"]["max_x"])
        y_coordinate = random.randint(board["meta"]["min_y"], board["meta"]["max_y"])
        coordinate = (x_coordinate, y_coordinate)

        # Don't generate anything for (0, 0) because it's a reserved tile
        # Don't generate anything if the selected coordinate is not a blank tile
        if coordinate != (0, 0) and board[coordinate] is None:
            # Add a detailed description for the entity
            if name == "TreeTrunk":
                board[coordinate] = "A sturdy tree trunk rises above you, its smooth bark perfect for climbing."
            else:
                board[coordinate] = f"A mysterious entity: {name}."
            counter += 1


def generate_ground_board() -> dict:
    """
    Generate a ground board with tree trunks and randomized forest patch descriptions for empty tiles.

    :postcondition: The board includes a random number of "TreeTrunk" entities and randomized forest patch descriptions
                    for empty tiles.
    :return: A dictionary representing the generated ground board with entities and descriptions.

    >>> ground_board_result = generate_ground_board()  # Generate the ground board
    >>> "TreeTrunk" in ground_board_result.values()  # Check that TreeTrunks exist
    True
    >>> tree_trunk_count = sum(1 for tile in ground_board_result.values() if tile == "TreeTrunk")  # Count TreeTrunks
    30 <= tree_trunk_count <= 60  # Randomized, skip the exact count check
    """
    ground_board = generate_board(-GROUND_X_SCALE, GROUND_X_SCALE, -GROUND_Y_SCALE, GROUND_Y_SCALE)
    populate_board(ground_board, "TreeTrunk", random.randint(30, 60))

    # Collect empty tiles
    empty_tiles = [tile for tile, content in ground_board.items() if content is None]

    # Fill empty tiles with forest patch descriptions
    for tile in empty_tiles:
        ground_board[tile] = forest_patch_description()

    return ground_board


def generate_tree_board() -> dict:
    """
    Generate a tree board with a central tree trunk and moss.

    :postcondition: The board includes one "TreeTrunk" at the center and a random number of "Moss" entities.
    :return: A dictionary representing the generated tree board with entities.

    >>> tree_board_result = generate_tree_board()
    >>> tree_board_result[(0, 0)] == "TreeTrunk"
    True  # The center should contain a TreeTrunk
    >>> total_moss_count = sum(1 for moss_entity in tree_board_result.values() if moss_entity == "Moss")
    0 <= total_moss_count <= tree_scale  # Number of Moss entities should be within the expected range
    """
    tree_scale = random.choice(TREE_SCALE_OPTIONS)
    tree_board = generate_board(-tree_scale, tree_scale, -tree_scale, tree_scale)

    # Place the central TreeTrunk
    tree_board[(0, 0)] = "TreeTrunk"

    # Populate Moss tiles randomly
    moss_count = random.randint(0, tree_scale)
    populate_board(tree_board, "Moss", moss_count)

    # Add descriptions for Moss and empty tiles
    for position in tree_board.keys():
        if tree_board[position] == "Moss":
            tree_board[position] = moss_description()  # Replace with a random moss description
        elif tree_board[position] is None:
            tree_board[position] = tree_patch_description()  # Random description for empty tiles

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
