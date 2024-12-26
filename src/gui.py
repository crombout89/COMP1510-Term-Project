import logging
import sys
import PySide6.QtCore

from PySide6 import QtCore, QtWidgets, QtGui

from src.board import generate_ground_board
from src.character import create_character
from src.sfx import sfx_setup, play_main_game_music
from src.ui import print_game_backstory


def main():
    """
    This is the entry point of the GUI.
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
    logging.info("PySide6 version: " + PySide6.__version__)
    logging.info("Qt version used to compile PySide6: " + PySide6.QtCore.__version__)
    logging.info("Package information: " + str(sys.path[0]) + str(__package__) + str(__name__))
    logging.info("Game started.")
    logging.info("Ground board: " + str(ground))
    logging.info("Character: " + str(player))
    play_main_game_music()


if __name__ == '__main__':
    main()
