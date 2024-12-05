from src.action import perform_action
from src.board import generate_ground_board, generate_tree_board, describe_current_location
from src.character import create_character, update_level, check_tummy
from src.entity import generate_entity, pick_up_item
from src.sfx import sfx_setup, play_main_game_music
from src.ui import (print_game_backstory, get_action_input, game_over,
                    game_complete)
from src.animal import help_animal


def game():
    """
    Drive the game.
    """
    sfx_setup()
    print_game_backstory()
    ground = generate_ground_board()
    current_board = ground
    player = create_character("Mittens")
    while not update_level(player):
        play_main_game_music()  # Ensure the music is reset when the player returns to the main game loop
        describe_current_location(player, current_board)
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
                if entity and entity["Type"] == "Animal":
                    help_animal(player, entity)
                elif entity and entity["Type"] == "Item":
                    pick_up_item(player, entity)
            else:
                game_over()
                return

    game_complete()


def main():
    """
    Drive the program
    """
    try:
        game()
    except KeyboardInterrupt:
        print("\n🛑 Game ended. Goodbye!")
        exit(0)


if __name__ == '__main__':
    main()
