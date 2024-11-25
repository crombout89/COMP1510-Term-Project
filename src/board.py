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
    :postcondition: generates a grid of coordinates with x coordinates from min_x to one less than max_x,
                    and y coordinates from min_y to one greater than max_y
    :return: a dictionary with a "meta" key containing a nested dictionary with the maximum and minimum x and y
             coordinates; and a set of tuple keys representing an x and y coordinate, and whose values are None
    :raises ValueError: if min_x is greater than max_x
    :raises ValueError: if min_y is greater than max_y

    >>> generate_board(-1, 1, -1, 1)
    {"meta": {"min_x": -1, "max_x": 1, "min_y": -1, "max_y": 1},
     (-1, -1): None, (-1, 0): None, (0, -1): None, (0, 0): None}
    >>> generate_board(-2, 2, -1, 1)
    {"meta": {"min_x": -2, "max_x": 2, "min_y": -1, "max_y": 1},
     (-2, -1): None, (-2, 0): None, (-1, -1): None, (-1, 0): None, (0, -1): None,
     (0, 0): None, (1, -1): None, (1, 0): None}
    >>> generate_board(-1, 1, -2, 2)
    {"meta": {"min_x": -1, "max_x": 1, "min_y": -2, "max_y": 2},
     (-1, -2): None, (-1, -1): None, (-1, 0): None, (-1, 1): None, (0, -2): None,
     (0, -1): None, (0, 0): None, (0, 1): None}
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

    for current_x in range(min_x, max_x):
        for current_y in range(min_y, max_y):
            board[(current_x, current_y)] = None

    return board
