import itertools
import logging
import typing

import pygame

from .board import current_location

from .config import ADD_TO_TUMMY_IF_EAT_ITEM, DIRECTION_MAPPING, BERRY_TREATMENTS
from .entity import item_input_to_entity, get_item_from_inventory
from .sfx import play_finale_music
from .util import dict_from_tuple_of_tuples, plural

# Actions that require function calls in perform_action
# get_action_input should return the action dictionary so it can be passed to perform_action
# The lambda functions represent how to format the "Data" key of the action dictionary
EXTERNAL_ACTIONS = (
    # "Action input": A lambda function to be called by get_action_input
    ("Climb", lambda d: None),
    ("Eat", lambda d: item_input_to_entity(d)),
    ("Nap", lambda d: None),
)

# Actions that call a function that displays some information
# get_action_input should call the corresponding function and then ask the user for the next action
INFORMATION_ACTIONS = (
    # "Action input": A lambda function to be called by get_action_input
    ("Check", lambda c, a: check(c, a)),
    ("Help", lambda c, a: print_game_backstory()),
    ("", lambda c, a: print_game_help())  # If the user presses enter without typing anything
)


def print_game_instructions():
    print(" ✨ Your Mission: ✨")
    print("- Use your purr-oblem-solving skills to figure out which berry cures each animal’s ailment.")
    print("- Climb up trees to find berries with magical healing powers!")
    print("- Heal enough animals to help them level up and bring balance back to Whisker Woods.")
    print("- Reach Level 3, where Mittens becomes the ultimate Meowgical Healer and saves the forest for good!")
    print("- Keep an eye on your tummy while you explore! Moving and climbing is hard work,")
    print("  and if your tummy gets empty, you'll pass out from hunger!")
    print(f"  Eat any berry to refill your tummy by {ADD_TO_TUMMY_IF_EAT_ITEM}.")
    print("  Eat Catnip or Silvervine to refill it by even more, and get extra energy where you can move and climb for")
    print("  a while without affecting your tummy!")


def print_game_backstory():
    """ Print the game's backstory and instructions for winning. """

    # Backstory
    print("====================================")
    print("Welcome to Whisker Woods Rescue! 🐾🐈")
    print("====================================\n")
    print("Deep in the heart of Whisker Woods, a magical forest brimming with life,\n"
          "animals have fallen ill from mysterious ailments. But don’t worry—there’s hope!")
    print("Meet Mittens, the Meowgical Healer, a kind-hearted kitty with a knack for\n"
          "mixing berries into purrfect remedies.")
    print("Equipped with her trusty whisker sense and a satchel of enchanted berries,\n"
          "she's on a mission to restore health to her forest friends, one paw at a time.")
    print("\nThe animals are counting on you to guide Mittens through this pawsome adventure.\n"
          "Every creature has a unique ailment that only the right berry can cure.\n"
          "Mittens' healing magic helps animals grow stronger, level up, and paw-sibly\n"
          "discover their own hidden powers!\n")

    print_game_instructions()

    print("\nAre you ready to embark on this berry sweet adventure?")
    print("Paws, think, and heal! The forest is rooting for you. 🐾🍓✨")
    return


def print_game_help():
    print("Type one of the following actions and press ENTER:")
    print(" - 'W' to move up")
    print(" - 'A' to move left")
    print(" - 'S' to move down")
    print(" - 'D' to move right")
    print(" - 'Check Tummy' to check your tummy and extra energy")
    print(" - 'Check Level' to check your level and how many animals you need to help before you level up")
    print(" - 'Check Inventory' to check what you have in your inventory")
    print(" - 'Check Location' to check where you are and how to get to the center of the board")
    print(" - 'Eat <item>' to eat a non-berry item like Catnip or Silvervine")
    print(" - 'Eat <colour> Berry' to eat a berry of the corresponding colour")
    print(" - 'Climb' to climb up or down a tree trunk")
    print(" - 'Nap' to take a nap on a patch of moss")
    print(" - 'Help' to the see the backstory and instructions from the start of the game")
    print()


def game_over():
    """ Print a game over message indicating the player has passed out from hunger. """

    print("\n💔 Oh no! You've passed out from hunger!")
    print("Without the energy to continue, your adventure comes to an end.")
    print("But don’t worry —- every hero gets another chance!")
    return


def game_complete():
    """ Print a congratulatory message to the player for completing the game. """
    try:
        play_finale_music()
    except pygame.error:
        pass
    print("\n🎉 Congratulations! You've completed Whisker Woods Rescue! 🎉")
    print("Thanks to your purr-severance and kindness, the forest is thriving again.")
    print(f"You've become the ultimate Meowgical Healer, and all the animals are healthy and happy!")
    print("Your trusty owner, the Professor, praises you for earning the trust and love of all creatures in"
          "the forest.")
    print("You've forged bonds with both real and imaginary friends, and now the forest is a place of joy and "
          "laughter!")
    # print("While the main challenges may have ended, your adventures in Whisker Woods continue.")
    # print("Feel free to explore, help new friends, and create your own stories in this magical land! 🐾✨")
    return


def get_action_input(character: dict) -> dict:
    """
    Ask the user for an action, process the input, and return an action dictionary.

    :param character: A dictionary containing information about the player character.
    :raises ValueError: If the user enters an unsupported or invalid action.
    :raises KeyError: If required keys are missing from the `character` or `board` dictionaries.
    :return: A dictionary representing the processed action with keys "Type" and "Data".

    >>> game_character = {
    ...     "InTree": False,
    ...     "GroundCoordinates": [5, 5],
    ...     "Tummy": 50,
    ...     "Inventory": ["Catnip", "Silvervine"]
    ... }
    >>> game_board = {
    ...     (5, 5): "Empty",
    ...     (6, 5): "Empty",
    ...     (6, 6): "TreeTrunk"
    ... }

    >>> get_action_input(game_character, game_board)  # User enters 'W'
    Enter an action: W
    {'Type': 'Move', 'Data': ['0', '-1']}

    >>> get_action_input(game_character, game_board)  # User enters 'Eat Catnip'
    Enter an action: Eat Catnip
    You eat the Catnip. Yum!
    {'Type': 'Eat', 'Data': ['Catnip']}

    >>> get_action_input(game_character, game_board)  # User enters 'Check Tummy'
    Enter an action: Check Tummy
    Your tummy level is: 50
    {'Type': 'Check', 'Data': ['Tummy']}
    """
    while True:
        user_input = input("\nWhat do you want to do? (Just press ENTER if you don't know) \n> ")
        selected_action = user_input.strip().title().split()
        selected_action += [""] * (2 - len(selected_action))  # Pad the selected_action list to prevent an IndexError
        action = {"Type": selected_action[0], "Data": selected_action[1:]}
        logging.info(f"User input: '{user_input}', Parsed as: {selected_action}, Generated proto-action: {action}")

        if action["Type"] in dict_from_tuple_of_tuples(EXTERNAL_ACTIONS):
            action["Data"] = dict_from_tuple_of_tuples(EXTERNAL_ACTIONS)[action["Type"]](action["Data"])
            return action
        elif action["Type"] in dict_from_tuple_of_tuples(DIRECTION_MAPPING).keys():
            return direction_input_to_action(action["Type"])
        elif action["Type"] in dict_from_tuple_of_tuples(INFORMATION_ACTIONS).keys():
            dict_from_tuple_of_tuples(INFORMATION_ACTIONS)[action["Type"]](character, action["Data"][0])
        else:
            print("🚫 That's not a valid action!")


def print_berry_help():
    table_header = "| <colour> Berry | Treats this Ailment |"
    border = "-" * len(table_header)
    print(border)
    print(table_header)
    print(border)
    for berry in dict_from_tuple_of_tuples(BERRY_TREATMENTS).items():
        print(f"| {berry[0].ljust(14)} | {berry[1].ljust(19)} |")
    print(border)


def get_berry_input(character) -> typing.Optional[dict]:
    while True:
        user_input = input("Which color berry would you like to give the animal?"
                           " (Type 'Help' if you don't know) \n> ")
        berry_color = user_input.strip().title()
        logging.info(f"User input: '{user_input}', Parsed as: {berry_color}")
        if not berry_color:
            print("You skipped giving the animal a berry.")
            return None
        elif berry_color == "Help":
            print_berry_help()
        else:
            # Check if the player has the berry in their inventory
            berry = {"Type": "Item", "Name": "Berry", "Data": berry_color.split()[0]}
            if get_item_from_inventory(character, berry):
                return berry
            else:
                print(f"Oh no! You don't have any '{berry['Data']}' berries in your inventory.")


def direction_input_to_action(direction_input: str) -> dict:
    """
    Determines the correct action dictionary for a selected movement direction.

    Uses WASD mapping, where W is up, A is left, S is down, and D is right.

    :param direction_input: a string representing the selected direction
    :precondition: direction_input must be one of "W", "A", "S" or "D" (non-case-sensitive)
    :postcondition: determines the correct action for the chosen direction
    :raises ValueError: if direction_input is not one of "W", "A", "S" or "D"
    :return: an action dictionary with "Move" as the key "Type" and the correct direction vector as the key "Data"

    >>> direction_input_to_action("W")
    {'Type': 'Move', 'Data': (0, -1)}
    >>> direction_input_to_action("A")
    {'Type': 'Move', 'Data': (-1, 0)}
    >>> direction_input_to_action("S")
    {'Type': 'Move', 'Data': (0, 1)}
    """
    action = {
        "Type": "Move"
    }
    try:
        action["Data"] = dict_from_tuple_of_tuples(DIRECTION_MAPPING)[direction_input.upper()]
    except KeyError:
        raise ValueError("Invalid direction input")
    else:
        return action


def check(character: dict, attribute: str) -> None:
    """
    Check a specific attribute of the character and display its value.

    :param character: A dictionary containing information about the player character.
    :param attribute: The attribute to check (e.g., 'Tummy', 'Level', 'Inventory').
    :precondition: character must be a dictionary containing the relevant attributes.
    :precondition: attribute must be a string representing a valid character attribute.
    :postcondition: Displays the value of the specified attribute.
    :raises ValueError: If the specified attribute does not exist in the character dictionary.
    :raises ValueError: If the attribute name is invalid or unsupported.

    >>> game_character = {
    ...     "Tummy": 50,
    ...     "Level": 2,
    ...     "Inventory": ["Catnip", "Silvervine"]
    ... }
    >>> check(character, "Tummy")
    Your tummy level is: 50
    >>> check(character, "Level")
    Your current level is: 2
    >>> check(character, "Inventory")
    Your inventory contains:
     - Catnip
     - Silvervine
    """
    def check_tummy_and_extra_energy():
        print(f"Your tummy level is: {character['Tummy']}")
        if character['ExtraEnergy'] > 0:
            print(f"You have extra energy for the next {character['ExtraEnergy']} move(s).")

    def check_level():
        print(f"Your current level is: {character['Level']}.\n"
              f"You have to help {character['UntilNextLevel']} more animals to level up.")

    def check_inventory():
        print("Your inventory contains:")
        top_level_items = [item for item in character["Inventory"].items() if type(item[1]) is int]
        berries = map(lambda b: (f"{b[0]} Berry" if b[1] == 1 else f"{b[0]} Berries", b[1]),
                      character["Inventory"]["Berries"].items())
        for inventory_item in itertools.chain(top_level_items, berries):
            print(f" - {inventory_item[1]} {inventory_item[0]}")

    def check_location():
        location = current_location(character)
        if character["InTree"]:
            print("You're in a tree.")
            print(f"Your current coordinates are {location}")
            if location == (0, 0):
                print("You're at the center of the tree and can climb down.")
            else:
                print("If you want to climb down, you have to go to the center of the tree at (0, 0)\n"
                      f"  Hint: Go {how_to_get_to_center(location)}.")
        else:
            print("You're on the ground.")
            print(f"Your current coordinates are {location}")
            if location == (0, 0):
                print("You're at the center of the forest.")
            elif character["FinalChallengeCompleted"] is False:
                print("If you want to attempt the final challenge,"
                      "you need to go to the center of the forest at (0, 0).\n"
                      f"  Hint: Go {how_to_get_to_center(location)}.")

    valid_attributes = {
        # "Attribute name": the_closure_to_call
        "Tummy": check_tummy_and_extra_energy,
        "Level": check_level,
        "Inventory": check_inventory,
        "Location": check_location,
    }

    # Ensure the attribute is valid
    if attribute in valid_attributes:
        valid_attributes[attribute]()
    else:
        print(f"🚫 '{attribute}' is not a supported attribute to check!")


def how_to_get_to_center(location: tuple[int, int]) -> str:
    """
    Tells the user how to get to the center of the board.

    Assumes that the center of the board is at coordinates (0, 0).

    Returns an empty string if location is already at the center

    :param location: a tuple representing a coordinate
    :precondition: location must be a tuple of two integers where
    :postcondition: determines how to get to the center of the board
    :return: a string telling the user how many tiles to move and in what direction to get to the center of the board

    >>> how_to_get_to_center((-2, -1))
    "2 tiles right and 1 tile down"
    >>> how_to_get_to_center((3, 0))
    "3 tiles left"
    >>> how_to_get_to_center((0, 4))
    "4 tiles up"
    """
    instruction_tokens = []
    if location[0] < 0:
        # If x coordinate is negative, they are in the left half of the map and need to go right
        instruction_tokens.append(f"{abs(location[0])} tile{plural(abs(location[0]))} right")
    elif location[0] > 0:
        # If x coordinate is positive, they are in the right half of the map and need to go left
        instruction_tokens.append(f"{abs(location[0])} tile{plural(abs(location[0]))} left")

    if location[1] < 0:
        # If x coordinate is negative, they are in the top half of the map and need to go down
        instruction_tokens.append(f"{abs(location[1])} tile{plural(abs(location[1]))} down")
    elif location[1] > 0:
        # If x coordinate is positive, they are in the bottom half of the map and need to go up
        instruction_tokens.append(f"{abs(location[1])} tile{plural(abs(location[1]))} up")

    if len(instruction_tokens) == 2:
        return f"{instruction_tokens[0]} and {instruction_tokens[1]}"
    elif len(instruction_tokens) == 1:
        return instruction_tokens[0]
    else:
        return ""
