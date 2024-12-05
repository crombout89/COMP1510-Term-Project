import os

from src import game


def main():
    """
    Drive the program.
    """
    os.chdir("src")
    game.main()


if __name__ == '__main__':
    main()
