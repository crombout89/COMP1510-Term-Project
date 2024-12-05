from .config import BERRY_TREATMENTS
from .description import sick_animal_description, cured_animal_description
from .entity import generate_reward
from .ui import get_berry_input
from .sfx import play_heal_sfx, play_finale_music, play_sad_animal_music
from .util import dict_from_tuple_of_tuples


def validate_berry(color: str, ailments: list[str]) -> bool:
    """
    Validate and treat an animal's ailment using a berry based on its color.

    :param color: A string representing the color of the berry.
    :param ailments: A list of strings representing the character's current ailments.
    :precondition: color must be a valid key in the BERRY_TREATMENTS dictionary.
    :precondition: ailments must be a list of strings representing the animal's ailments.
    :postcondition: If the berry can treat an ailment, it will be removed from the list of ailments;
                    prints a message to the console telling the user whether the treatment was valid
    :return: True if an ailment was successfully treated, False otherwise.

    >>> TEST_BERRY_TREATMENTS = {
    ...     "Red": "Burn",
    ...     "Blue": "Fever",
    ...     "Green": "Nausea"
    ... }
    >>> test_ailments = ["Burn", "Starving"]
    >>> validate_berry("Red", ailments)
    True
    >>> ailments
    ['Starving']  # Burn is treated

    >>> validate_berry("Blue", ailments)
    False  # No Blue berry effect on current ailments
    >>> ailments
    ['Starving']  # No change

    >>> validate_berry("Green", ["Starving"])
    True  # Treats starvation
    >>> validate_berry("Yellow", ["Starving"])  # Yellow berry does not exist in BERRY_TREATMENTS
    False  # No treatment available
    """
    berry_treatments = dict_from_tuple_of_tuples(BERRY_TREATMENTS)
    if berry_treatments[color] in ailments or "Starving" in ailments:
        if berry_treatments[color] in ailments:
            ailments.remove(berry_treatments[color])
        else:
            ailments.remove("Starving")
        print(f"The {color} Berry successfully treated one of the animal's ailments! 🩹")
        return True
    else:
        print(f"The {color} Berry was not effective, the animal's ailments were not cured. 😢")
        return False


def help_animal_success(character: dict, entity: dict):
    play_heal_sfx()
    print(f"The {entity['Name']} has been completely cured of their ailments!")
    print(cured_animal_description(entity))

    generate_reward(character, entity["Name"])

    # Update character stats (AnimalsHelped and UntilNextLevel)
    character["AnimalsHelped"] += 1
    character["UntilNextLevel"] -= 1
    # Handle Final Challenge
    if entity["Name"] == "FinalChallenge":
        character["FinalChallengeCompleted"] = True
        play_finale_music()
        print("Congratulations! You have completed the Final Challenge! 🎉")
    print("Press ENTER to continue...")


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
    play_sad_animal_music()
    # Special handling for the Final Challenge
    if entity["Name"] == "FinalChallenge":
        print("You are accepting the Final Challenge!")
        print("You need to give the sick animal a special medicine made from a recipe of berries to cure them,"
              "or press ENTER to skip.")
    else:
        print(sick_animal_description(entity))
        print("You need to give them the correct berries to cure their ailments! Or, press ENTER to skip.")

    # Main loop to treat the animal
    while len(entity["Data"]) > 0:
        berry = get_berry_input(character)

        # Validate the berry as a treatment for the ailments
        if not berry or not validate_berry(berry['Data'], entity["Data"]):
            return

    help_animal_success(character, entity)
