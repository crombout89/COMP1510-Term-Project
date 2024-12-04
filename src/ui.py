import random

from .animal import validate_berry
from .character import get_item_from_inventory, current_location, check_tummy
from .config import ADD_TO_TUMMY_IF_EAT_ITEM
from .descriptions import sick_animal_description, cured_animal_description
from .entity import generate_item, stringify_item
from .action import check

DIRECTION_MAPPING = {
    # "Direction input": (Direction vector)
    "W": (0, -1),  # Decriment y coordinate to move up
    "A": (-1, 0),  # Decriment x coordinate to move left
    "S": (0, 1),  # Incriment y coordinate to move down
    "D": (1, 0)  # Incriment x coordinate to move right
}

# Actions that require function calls in perform_action
# get_action_input should immediately return the action dictionary so it can be passed to perform_action
EXTERNAL_ACTIONS = ["Climb", "Eat", "Nap"]

# Actions that call a function that displays some information
# get_action_input should call the corresponding function and then ask the user for the next action
INFORMATION_ACTIONS = {
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
    print("Mittens has become the ultimate Meowgical Healer, and all the animals are healthy and happy!")
    print("You're truly the hero of Whisker Woods! 🐾✨")
    return


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
        action["Data"] = DIRECTION_MAPPING[direction_input.upper()]
    except KeyError:
        raise ValueError("Invalid direction input")
    else:
        return action


def get_action_input(character: dict, board: dict) -> dict:
    """
    Ask the user for an action, process the input, and return an action dictionary.

    :param character: A dictionary containing information about the player character.
    :param board: A dictionary containing information about the board.
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
        """
        if action["Type"] not in valid_actions:
            raise ValueError("Invalid action.")

        if action["Type"] == "Climb":
            if not climb(character, board):
                raise ValueError("No tree to climb!")

        elif action["Type"] == "Eat":
            if not action["Data"]:
                raise ValueError("Specify what to eat!")
            if action["Data"][0] not in character["Inventory"]:
                raise ValueError("Item not in inventory.")
            eat(character, action["Data"][0])

        elif action["Type"] == "Nap":
            if not nap(character, board):
                raise ValueError("Can't nap here!")

        elif action["Type"] == "Check":
            if action["Data"][0] not in ["Tummy", "Level", "Inventory"]:
                raise ValueError("Invalid attribute to check.")
        """


def help_animal(character: dict, entity: dict):
    """
    Allow the player to help a sick animal by using berries to cure its ailments.

    :param character: A dictionary representing the character's data, which includes:
                      - "Level": An integer representing the player's current level.
                      - "Inventory": A dictionary containing the player's inventory, including berries.
                      - "AnimalsHelped": An integer representing the number of animals helped.
                      - "UntilNextLevel": An integer tracking the progress toward leveling up.
    :param entity: A dictionary representing the animal's data, which includes:
                      - "Name": A string representing the animal's name.
                      - "Ailments": A list of strings representing the animal's ailments.
    :precondition: character must be a valid dictionary with the required keys and values as described above.
    :precondition: entity must be a valid dictionary with the required keys and values as described above.
    :raises: KeyError if a required key is missing from the character or entity dictionaries.
    :raises: TypeError if character or entity is not a dictionary or if their values are not of the expected type.
    :raises: ValueError if the berry quantity in the inventory is invalid (e.g. negative or missing).
    :postcondition: If the animal's ailments are successfully treated, the ailments are removed and the player receives
                    rewards.
    :postcondition: The character's inventory is updated to reflect the berries used.
    :postcondition: The character's statistics ("AnimalsHelped", "UntilNextLevel", and "Level") are updated
                    appropriately.
    :postcondition: If "FinalChallenge" is completed, character["FinalChallengeCompleted"] is set to True.
    """
    name = entity.get("Name", "")
    ailments = entity.get("Data", [])
    level = character.get("Level", 1)

    # Special handling for the Final Challenge
    if name == "FinalChallenge":
        print("You are accepting the Final Challenge!")
        print("You need to give the sick animal a special medicine made from a recipe of berries to cure them,"
              "or press ENTER to skip.")
    else:
        print(sick_animal_description(entity))
        print("You need to give them the correct berries to cure their ailments! Or, press ENTER to skip.")

    # Main loop to treat the animal
    while len(ailments) > 0:
        berry_color = input("Which color berry would you like to give the animal? ").strip().lower().title()
        if not berry_color:
            print("You skipped giving the animal a berry.")
            return

        berry = {
            "Type": "Item",
            "Name": "Berry",
            "Data": berry_color
        }

        # Check if the player has the berry in their inventory
        has_item = get_item_from_inventory(character, berry)
        if not has_item:
            print(f"Oh no! You don't have any '{berry_color}' berries in your inventory.")
            continue

        print(f"Hooray! You have '{berry_color}' berry in your inventory!")

        # Validate the berry as a treatment for the ailments
        valid_treatment = validate_berry(berry_color, ailments)
        if not valid_treatment:
            print(f"The '{stringify_item(berry)}' was not effective, the animal's ailments were not cured. 😢")
            return

        print(f"The berry '{stringify_item(berry)}' successfully treated one of the animal's ailments! 🩹")

        # Check if all ailments are cured
        if len(ailments) == 0:
            print(f"The {name} has been completely cured of their ailments!")
            print(cured_animal_description(entity))

            # Generate rewards
            rewards_count = random.randint(2, 1 + level)
            print(f"The {name} gave you {rewards_count} items as a sign of their gratitude!")

            # Reward the player with random items
            for _ in range(rewards_count):
                reward_item = generate_item(character, True)  # Generate a random item
                pick_up_item(character, reward_item)  # Add the item to the player's inventory
                print(f"You received: {stringify_item(reward_item)}!")

            # Update character stats (AnimalsHelped and UntilNextLevel)
            character["AnimalsHelped"] = character.get("AnimalsHelped", 0) + 1
            character["UntilNextLevel"] = max(0, character.get("UntilNextLevel", 0) - 1)
            # Handle Final Challenge or Level Up
            if name == "FinalChallenge":
                character["FinalChallengeCompleted"] = True
                print("Congratulations! You have completed the Final Challenge! 🎉")

                return


def pick_up_item(character: dict, entity: dict):
    """
    Add an item to the character's inventory and prints a message to the console telling the user
    what item was picked up.

    :param character: the character to receive the item
    :precondition: character must be a well-formed dictionary representing a character
    :param entity: the entity containing the item to be picked up
    :precondition: character must be a well-formed dictionary representing an entity and whose type is "Item"
    :postcondition: increments the corresponding item in the inventory of the character by one,
                    and prints a message to the console telling the user
    :raises TypeError: if entity is not an item

    >>> game_character = {
    ...     "Inventory": {
    ...         "Catnip": 0,
    ...         "Silvervine": 0,
    ...         "Berries": {
    ...             "Red": 0,
    ...             "Green": 0,
    ...             "Blue": 0,
    ...             "Yellow": 0,
    ...             "Purple": 0
    ...         }
    ...     }
    ... }
    >>> game_item = {
    ...     "Type": "Item",
    ...     "Name": "Catnip",
    ...     "Data": None
    ... }
    >>> game_character["Inventory"]["Catnip"]
    0
    >>> pick_up_item(game_character, game_item)
    💼 You picked up a Catnip.
    >>> game_character["Inventory"]["Catnip"]
    1
    """
    if entity["Type"] != "Item":
        raise TypeError(f"Expected entity type 'Item', got '{entity['Type']}'")

    if entity["Name"] in ["Catnip", "SilverVine"]:
        character["Inventory"][entity["Name"]] += 1
        print(f"💼 You picked up a {entity['Name']}.")
    elif entity["Name"] == "Berries" and entity["Data"] is not None:
        character["Inventory"]["Berries"][entity["Data"]] += 1
        print(f"💼 You picked up a {entity['Data']} berry.")
    else:
        print(f"Cannot pick up {entity['Name']} without valid data.")


def describe_location(character: dict, board: dict):
    pass


