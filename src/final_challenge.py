from src.animal import help_animal
from src.entity import generate_entity


def start_final_challenge(character: dict) -> None:
    """
    Initialize the final challenge for the character.

    :param character: A dictionary containing information about the player character.
    :precondition: character must be a dictionary with keys for "InTree", "GroundCoordinates",
                   and "FinalChallengeCompleted".
    :raises KeyError: If required keys are missing from the character dictionary.
    :postcondition: Sets up the character for the final challenge by updating relevant keys and printing instructions.

    This function:
    - Sets the "InTree" key to False.
    - Sets the "GroundCoordinates" key to (0, 0).
    - Sets the "FinalChallengeCompleted" key to False.
    - Prints a message to the user explaining the final challenge and how to complete it.

    >>> game_character = {
    ...     "InTree": True,
    ...     "GroundCoordinates": (5, 5),
    ...     "FinalChallengeCompleted": True
    ... }
    >>> start_final_challenge(game_character)
    The final challenge is to find the hidden treasure on the ground.
    Search carefully and use all your skills to complete the task!
    Beware of obstacles and enemies that may block your path.
    >>> game_character["InTree"]
    False
    >>> game_character["GroundCoordinates"]
    (0, 0)
    >>> game_character["FinalChallengeCompleted"]
    False
    """
    def print_final_challenge_instructions():
        print("\n🗣️ You suddenly hear the professor calling you from the center of the forest.")
        print("You drop what you're doing and run to him.")
        print("The Professor is tending to a legendary creature, the Moonlit Lynx, the great protector of the forest.")
        print("The Professor tells you that the Moonlit Lynx is gravely ill.\n"
              "Without the forest's guardian to watch over it, everything will soon wither away.\n"
              "The only way to cure the Lynx is a special recipe of all the different berries in the forest.\n"
              "The recipe needs need two of each coloured berry. No more, no less.\n"
              "The Professor can use his technology to stabilize the Lynx, for now. \n"
              "It's up to you to get the berries!\n"
              "The fate of the forest rests in your paws!\n")
        input("Press Enter to continue...")
    # Ensure required keys are in the character dictionary
    required_keys = ["InTree", "GroundCoordinates", "FinalChallengeCompleted"]
    for key in required_keys:
        if key not in character:
            raise KeyError(f"Missing required key '{key}' in character dictionary.")

    # Update character attributes for the final challenge
    character["InTree"] = False
    character["GroundCoordinates"] = (0, 0)
    character["FinalChallengeCompleted"] = False

    print_final_challenge_instructions()

    help_animal(character, generate_entity({(0, 0): None}, character))
