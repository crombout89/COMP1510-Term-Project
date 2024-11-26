import copy
import random
import typing

from config import (AILMENT_OPTIONS, BERRY_COLOR_OPTIONS, ANIMAL_PROBABILITY, SILVERVINE_PROBABILITY,
                    CATNIP_PROBABILITY, BERRY_PROBABILITY)
from character import current_location


def generate_item(character: dict, always: bool = False) -> typing.Optional[dict]:
    def generate_berry_decision():
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
        ailments.remove("Starving")
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
        return generate_animal()
    else:
        return generate_item(character)