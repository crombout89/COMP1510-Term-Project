import copy
import random
import typing

from .config import (ANIMAL_OPTIONS, AILMENT_OPTIONS, BERRY_COLOR_OPTIONS,
                     ANIMAL_PROBABILITY, SILVERVINE_PROBABILITY, CATNIP_PROBABILITY, BERRY_PROBABILITY)
from .character import current_location


def generate_animal(character: dict) -> dict:
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
    def generate_berry_decision() -> bool:
        # Normally, berries can only be found in trees, so we only generate a berry if the character is in a tree.
        # Berry has the lowest priority of all item types so if we're decising whether to generate a berry,
        # we know that we're on the last item option. So if the "always" parameter is set, we always need to generate
        # a berry as the default item.
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
    def generate_final_challenge_entity():
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
