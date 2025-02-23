import logging

from src.action import perform_action
from src.animal import help_animal
from src.board import generate_ground_board, generate_tree_board, describe_current_location
from src.character import create_character, update_level, check_tummy
from src.entity import generate_entity, pick_up_item
from src.sfx import sfx_setup, play_main_game_music
from src.ui import (print_game_backstory, get_action_input, game_over,
                    game_complete)


def game():
    """
    Drive the game.
    """
    logging.basicConfig(filename="../game.log",
                        filemode="a",
                        format="[%(asctime)s %(filename)s %(funcName)s %(msecs)d %(name)s %(levelname)s] %(message)s",
                        datefmt="%Y-%M-%d %H:%M:%S",
                        level=logging.DEBUG)
    sfx_setup()
    print_game_backstory()
    ground = generate_ground_board()
    current_board = ground
    player = create_character("Mittens")
    logging.info("Game started.")
    logging.info("Ground board: " + str(ground))
    play_main_game_music()
    while not update_level(player):
        describe_current_location(player, current_board)
        logging.info("Character: " + str(player))
        action = get_action_input(player)
        while not perform_action(player, current_board, action):
            action = get_action_input(player)
            logging.info("Action: " + str(action))
        if action["Type"] == "Climb":
            if check_tummy(player):
                if player["InTree"]:
                    current_board = generate_tree_board()
                    logging.info("Tree board: " + str(current_board))
                else:
                    current_board = ground
                    logging.info("Returned to ground board.")
            else:
                game_over()
                return
        elif action["Type"] == "Move":
            if check_tummy(player):
                entity = generate_entity(current_board, player)
                logging.info("Entity: " + str(entity))
                if entity and entity["Type"] == "Animal":
                    help_animal(player, entity)
                    play_main_game_music()
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
        logging.info("Game exited.")
        exit(0)


if __name__ == '__main__':
    main()
