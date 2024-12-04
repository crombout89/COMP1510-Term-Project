import typing

from .character import get_item_from_inventory
from .config import ADD_TO_TUMMY_IF_EAT_ITEM, DIRECTION_MAPPING
from .entity import item_input_to_entity
from .action import check, direction_input_to_action

# Actions that require function calls in perform_action
# get_action_input should return the action dictionary so it can be passed to perform_action
# The lambda functions represent how to format the "Data" key of the action dictionary
EXTERNAL_ACTIONS = {
    # "Action input": A lambda function to be called by get_action_input
    "Climb": lambda d: None,
    "Eat": lambda d: item_input_to_entity(d),
    "Nap": lambda d: None,
}

# Actions that call a function that displays some information
# get_action_input should call the corresponding function and then ask the user for the next action
INFORMATION_ACTIONS = {
    # "Action input": A lambda function to be called by get_action_input
    "Check": lambda c, a: check(c, a),
    "Help": lambda c, a: print_game_backstory(),
    "": lambda c, a: print_game_help()  # If the user presses enter without typing anything
}


def print_game_instructions():
    print(" ✨ Your Mission: ✨")
    print("- Use your purr-oblem-solving skills to figure out which berry cures each animal’s ailment.")
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
    print("Welcome to Whisker Woods Rescue! 🐾🐈")
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
    print("\n")
    print("Type one of the following actions and press ENTER:")
    print(" - 'W' to move up")
    print(" - 'A' to move left")
    print(" - 'S' to move down")
    print(" - 'D' to move right")
    print(" - 'Check Tummy' to check your tummy and extra energy")
    print(" - 'Check Level' to check your level and how many animals you need to help before you level up")
    print(" - 'Check Inventory' to check what you have in your inventory")
    print(" - 'Eat <item>' to eat a non-berry item like Catnip or Silvervine")
    print(" - 'Eat <colour> Berry' to eat a berry of the corresponding colour")
    print(" - 'Climb' to climb up or down a tree trunk")
    print(" - 'Nap' to take a nap on a patch of moss")
    print(" - 'Help' to the see the backstory and instructions from the start of the game")


def game_over():
    """ Print a game over message indicating the player has passed out from hunger. """

    print("💔 Oh no! You've passed out from hunger!")
    print("Without the energy to continue, your adventure comes to an end.")
    print("But don’t worry —- every hero gets another chance!")
    return


def game_complete():
    """ Print a congratulatory message to the player for completing the game. """

    print("🎉 Congratulations! You've completed Whisker Woods Rescue! 🎉")
    print("Thanks to your purr-severance and kindness, the forest is thriving again.")
    print("You have become the ultimate Meowgical Healer, and all the animals are healthy and happy!")
    print("You're truly the hero of Whisker Woods! 🐾✨")
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
    ...     "Inventory": ["Catnip", "SilverVine"]
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
    action = {}

    while True:
        selected_action = (input("What do you want to do? (Just press ENTER if you don't know) ")
                           .strip().title().split())
        action["Type"], action["Data"] = selected_action[0], selected_action[1:]

        if action["Type"] in EXTERNAL_ACTIONS:
            return action
        elif action["Type"] in DIRECTION_MAPPING.keys():
            return direction_input_to_action(action["Data"][0])
        elif action["Type"] in INFORMATION_ACTIONS.keys():
            INFORMATION_ACTIONS[action["Type"]](character, action["Data"][0])
        else:
            print("🚫 That's not a valid action!")


def get_berry_input(character) -> typing.Optional[dict]:
    while True:
        berry_color = input("Which color berry would you like to give the animal? ").strip().lower().title()
        if not berry_color:
            print("You skipped giving the animal a berry.")
            return None
        else:
            # Check if the player has the berry in their inventory
            berry = {"Type": "Item", "Name": "Berry", "Data": berry_color}
            if get_item_from_inventory(character, berry):
                return berry
            else:
                print(f"Oh no! You don't have any '{berry['Data']}' berries in your inventory.")
