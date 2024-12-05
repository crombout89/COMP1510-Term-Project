import os

from src import game
from src.animal import help_animal_success


def main():
    """
    Drive the program.
    """
    os.chdir("src")
    game.main()


if __name__ == '__main__':
    main()
