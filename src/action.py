def perform_action(character: dict, board: dict, action: dict) -> bool:
    if action["Type"] == "Move":
        return move(character, board, action["data"])
    elif action["Type"] == "Climb":
        return climb(character)
    elif action["Type"] == "Eat":
        return eat(character, action["data"])
    elif action["Type"] == "Nap":
        return nap(character, board)
    else:
        return False
