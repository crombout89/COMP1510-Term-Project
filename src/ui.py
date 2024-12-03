def print_game_instructions():
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
          "discover their own hidden powers!")

    # Game Objectives
    print("\n ✨ Your Mission: ✨")
    print("- Use your purr-oblem-solving skills to figure out which berry cures each animal’s ailment.")
    print("- Heal enough animals to help them level up and bring balance back to Whisker Woods.")
    print("- Reach Level 3, where Mittens becomes the ultimate Meowgical Healer and saves the forest for good!")

    print("\nAre you ready to embark on this berry sweet adventure?")
    print("Paws, think, and heal! The forest is rooting for you. 🐾🍓✨")
    return


def game_over():
    """ Print a game over message indicating the player has passed out from hunger. """

    print("💔 Oh no! You've passed out from hunger!")
    print("Without the energy to continue, your adventure comes to an end.")
    print("But don’t worry —- every hero gets another chance!")
    return


def game_complete():
    """ Print a congratulatory message to the player for completing the game. """

    print("🎉 Congratulations! You've completed Whisker Woods Rescue! 🎉")
    print("Thanks to your purrseverance and kindness, the forest is thriving again.")
    print("Mittens has become the ultimate Meowgical Healer, and all the animals are healthy and happy!")
    print("You're truly the hero of Whisker Woods! 🐾✨")
    return


def get_action_input(character: dict, board: dict) -> dict:
    """
    Ask the user for an action, process the input, and return an action dictionary.

    :param character: A dictionary containing information about the player character.
    :param board: A dictionary containing information about the board.
    :precondition: character must be a dictionary.
    :precondition: board must be a dictionary.
    :postcondition: Returns a dictionary representing the processed action with keys "Type" and "Data".
    :return: A dictionary representing the processed action with keys "Type" and "Data".
    """


def help_animal(character: dict, entity: dict):
    pass


def pick_up_item(character: dict, entity: dict):
    """
    Adds an item to the character's inventory and prints a message to the console telling the user
    what item was picked up.

    :param character: the character to receive the item
    :precondition: character must be a well-formed dictionary representing a character
    :param entity: the entity containing the item to be picked up
    :precondition: character must be a well-formed dictionary representing an entity and whose type is "Item"
    :postcondition: increments the corresponding item in the inventory of the character by one,
                    and prints a message to the console telling the user
    :raises ValueError: if entity is not an item
    """
    if entity["Type"] != "Item":
        raise ValueError(f"The key 'Type' of entity must be 'Item', not '{entity['Type']}'")
    if entity["Name"] == "Catnip" or entity["Name"] == "Silvervine":
        print(f"You picked up a {entity['Name']}.")
        character["Inventory"][entity["Name"]] += 1
    else:
        print(f"You picked up a {entity['Data']} Berry.")
        character["Inventory"]["Berries"][entity["Data"]] += 1


def describe_location(character: dict, board: dict):
    pass


def start_final_challenge(character):
    character["InTree"] = False
    character["GroundCoordinates"] = (0, 0)
    character["FinalChallengeCompleted"] = False
    # TODO: Print user prompts
