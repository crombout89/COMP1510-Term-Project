import random
from config import GROUND_X_SCALE, GROUND_Y_SCALE, TREE_SCALE_OPTIONS


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
            board[(current_x, current_y)] = None

    return board


def populate_board(board: dict, name: str, times: int):
    counter = 1
    while counter <= times:
        x_coordinate = random.randint(board["meta"]["min_x"], board["meta"]["max_x"])
        y_coordinate = random.randint(board["meta"]["min_y"], board["meta"]["max_y"])
        coordinate = (x_coordinate, y_coordinate)

        # Don't generate anything for (0, 0) because it's a reserved tile
        # Don't generate anything if the selected coordinate is not a blank tile
        if coordinate != (0, 0) and board[coordinate] is None:
            board[coordinate] = name
            counter += 1


def generate_ground_board() -> dict:
    ground_board = generate_board(-GROUND_X_SCALE, GROUND_X_SCALE, -GROUND_Y_SCALE, GROUND_Y_SCALE)
    populate_board(ground_board, "TreeTrunk", random.randint(30, 60))
    return ground_board


def generate_tree_board() -> dict:
    tree_scale = random.choice(TREE_SCALE_OPTIONS)
    tree_board = generate_board(-tree_scale, tree_scale, -tree_scale, tree_scale)
    tree_board[(0, 0)] = "TreeTrunk"
    populate_board(tree_board, "Moss", random.randint(0, tree_scale))
    return tree_board
