import copy
import random
import typing

from .config import (ANIMAL_OPTIONS, AILMENT_OPTIONS, BERRY_COLOR_OPTIONS,
                     ANIMAL_PROBABILITY, SILVERVINE_PROBABILITY, CATNIP_PROBABILITY, BERRY_PROBABILITY)
from .character import current_location


def generate_animal(character: dict) -> dict:
    """
    Generate an animal entity with a random name and set of ailments based on the character's level.

    :param character: A dictionary representing the character, which includes the character's level.
    :postcondition: Returns an animal with a unique set of ailments and the number of ailments based on the
                    character's level.
    :return: A dictionary representing the generated animal, including its type, name, and ailments.

    >>> character = {"Level": 3}
    >>> animal = generate_animal(character)
    >>> animal["Type"]
    'Animal'
    >>> animal["Name"] in ANIMAL_OPTIONS
    True  # The animal's name should be one of the options
    >>> 1 <= len(animal["Data"]) <= 3  # Number of ailments should be between 1 and character's level
    True
    """
    new_animal = {
        "Type": "Animal",
        "Name": random.choice(ANIMAL_OPTIONS)
    }

    # Ailments is a set to ensure an animal (that's not the final challenge) does not have duplicate ailments
    # If more than one of the same ailment is generated, all but the first instance of the ailment will be ignored
    ailments = set()

    # An animal's number of ailments is between 1 and the level of the character for whom the animal is generated
    max_ailments = random.randint(1, character["Level"])

    for _ in range(max_ailments):
        ailments.add(random.choice(AILMENT_OPTIONS))

    new_animal["Data"] = list(ailments)  # Convert the set of ailments to a list
    return new_animal


def generate_item(character: dict, always: bool = False) -> typing.Optional[dict]:
    """
    Generate an item entity, which can be Silvervine, Catnip, or Berry, based on certain conditions.
    :param character: A dictionary representing the character's state, including if they are in a tree or not.
    :param always: A boolean indicating whether to always generate a berry.
    :postcondition: The generated item will have a type and name, and may include additional data (like berry
                    color).
    :return: A dictionary representing the generated item, or None if no item is generated.

    >>> character = {"InTree": True}
    >>> item = generate_item(character)
    >>> item["Type"] == "Item"
    True  # The item should be of type Item
    >>> item["Name"] in ["Silvervine", "Catnip", "Berry", None]
    True  # The item should be one of the defined options
    >>> item["Name"] == "Berry" and item["Data"] in BERRY_COLOR_OPTIONS
    True  # If the item is a Berry, it should have a valid color
    """
    def generate_berry_decision() -> bool:
        # Normally, berries can only be found in trees, so we only generate a berry if the character
        # is in a tree.
        # Berry has the lowest priority of all item types so if we're deciding whether to generate a berry,
        # we know that we're on the last item option. So if the "always" parameter is set, we always need
        # to generate a berry as the default item.
        return always or character["InTree"] and random.randint(1, BERRY_PROBABILITY) == 1

    new_item = {
        "Type": "Item",
        "Name": "",
        "Data": None
    }
    if random.randint(1, SILVERVINE_PROBABILITY) == 1:
        new_item["Name"] = "Silvervine"
        return new_item
    elif random.randint(1, CATNIP_PROBABILITY) == 1:
        new_item["Name"] = "Catnip"
        return new_item
    elif generate_berry_decision():
        berry_color = random.choice(BERRY_COLOR_OPTIONS)
        new_item["Name"] = "Berry"
        new_item["Data"] = berry_color
        return new_item
    else:
        return None


def generate_entity(board: dict, character: dict) -> typing.Optional[dict]:
    """
    Generate an entity (animal or item) based on the character's location and state.

    :param board: A dictionary representing the game board.
    :param character: A dictionary representing the character's state, including final challenge status.
    :precondition: board must be a valid dictionary containing the game board coordinates.
    :precondition: character must be a valid dictionary containing the "FinalChallengeCompleted" key.
    :postcondition: If the character is at the final challenge location, a specific entity will be generated.
    :return: A dictionary representing the generated entity (animal or item), or None if no entity is generated.

    >>> board = {
    ...     (0, 0): None,
    ...     (1, 1): "TreeTrunk",
    ... }
    >>> character = {"FinalChallengeCompleted": False, "InTree": False}
    >>> entity = generate_entity(board, character)
    >>> if entity:
    ...     entity["Type"] in ["Animal", "Item"]
    ...     True  # The generated entity should be either an Animal or an Item
    True
    >>> character["FinalChallengeCompleted"] = True
    >>> generate_entity(board, character) is None
    True  # Should not generate an entity if the final challenge is completed
    """
    def generate_final_challenge_entity() -> dict:
        # Generate a list of ailments where each ailment except "Starving" appears twice
        # The resultant list of ailments will require two of each berry to treat
        ailments = copy.deepcopy(AILMENT_OPTIONS)
        ailments.remove("Starving")  # We remove "Starving" because it would mess up the two of each berry requirement
        ailments *= 2
        return {
            "Type": "Animal",
            "Name": "FinalChallenge",
            "Data": ailments,
        }

    location = current_location(character)
    if character["FinalChallengeCompleted"] is False and location == (0, 0):
        return generate_final_challenge_entity()
    if board[location] == "TreeTrunk" or board[location] == "Moss":
        # Don't generate any entities on tree trunks or moss
        return None
    if random.randint(1, ANIMAL_PROBABILITY) == 1:
        return generate_animal(character)
    else:
        return generate_item(character)
