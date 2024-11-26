from board import valid_location
from src.character import current_location


def move(character: dict, board: dict, direction: tuple[int, int]) -> bool:
    coordinate_type = ("Tree" if character["InTree"] else "Ground") + "Coordinates"
    new_coordinates = (character[coordinate_type][0] + direction[0],
                       character[coordinate_type][1] + direction[1])
    if valid_location(board, new_coordinates):
        character[coordinate_type] = new_coordinates
        return True
    else:
        return False


def climb(character: dict, board) -> bool:
    location = current_location(character)
    if board[location] == "TreeTrunk":
        if character["InTree"]:
            character["InTree"] = False
        else:
            character["TreeCoordinates"] = (0, 0)
            character["InTree"] = True
        return True
    else:
        # TODO: print a message to the console telling the user that they can't climb because they are not
        #  at a tree trunk
        return False


def nap(character: dict, board: dict) -> bool:
    location = current_location(character)
    if board[location] == "Moss":
        character["ExtraEnergy"] += 5
        # TODO: print a message to the console telling the user that they now have 5 more ExtraEnergy
        return True
    else:
        # TODO: print a message to the console telling the user that they can only nap on moss
        return False


def perform_action(character: dict, board: dict, action: dict) -> bool:
    if action["Type"] == "Move":
        return move(character, board, action["data"])
    elif action["Type"] == "Climb":
        return climb(character, board)
    elif action["Type"] == "Eat":
        return eat(character, action["data"])
    elif action["Type"] == "Nap":
        return nap(character, board)
    else:
        return False
