from src.action import perform_action
from src.board import generate_ground_board, generate_tree_board
from src.character import create_character, update_level, check_tummy
from src.entity import generate_entity, pick_up_item
from src.ui import (print_game_backstory, get_action_input, game_over,
                    game_complete)
from src.animal import help_animal


def describe_location(player, current_board):
    pass


def game():
    """
    Drive the game.
    """
    print_game_backstory()
    ground = generate_ground_board()
    current_board = ground
    player = create_character("Mittens")
    while not update_level(player):
        action = get_action_input(player)
        while not perform_action(player, current_board, action):
            action = get_action_input(player)
        if action["Type"] == "Climb":
            if check_tummy(player):
                if player["InTree"]:
                    current_board = generate_tree_board()
                else:
                    current_board = ground
            else:
                game_over()
                return
        elif action["Type"] == "Move":
            if check_tummy(player):
                entity = generate_entity(current_board, player)
                if entity["Type"] == "Animal":
                    help_animal(player, entity)
                elif entity["Type"] == "Item":
                    pick_up_item(player, entity)
                else:
                    describe_location(player, current_board)
            else:
                game_over()
                return

    game_complete()


def main():
    """
    Drive the program
    """
    game()


if __name__ == '__main__':
    main()
