import copy
import itertools
import random
import typing

from .config import (ANIMAL_OPTIONS, AILMENT_OPTIONS, BERRY_COLOR_OPTIONS,
                     ANIMAL_PROBABILITY, SILVERVINE_PROBABILITY, CATNIP_PROBABILITY, BERRY_PROBABILITY)
from .character import current_location
from .description import sick_animal_description


def generate_animal(character: dict) -> dict:
    """
    Generate an animal entity with a random name and set of ailments based on the character's level.

    :param character: A dictionary representing the character, which includes the character's level.
    :postcondition: Returns an animal with a unique set of ailments and the number of ailments based on the
                    character's level.
    :return: A dictionary representing the generated animal, including its type, name, and ailments.

    >>> my_character = {"Level": 3}
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
        "Name": random.choice(ANIMAL_OPTIONS),
        "Data": []  # Initialize Data key to ensure it exists
    }

    ailments = set()
    max_ailments = random.randint(1, character["Level"])

    for _ in range(max_ailments):
        ailments.add(random.choice(AILMENT_OPTIONS))

    new_animal["Data"] = list(ailments)
    new_animal["Description"] = sick_animal_description(new_animal)

    return new_animal


def generate_item(character: dict, always: bool = False) -> typing.Optional[dict]:
    """
    Generate an item entity, which can be Silvervine, Catnip, or Berry, based on certain conditions.
    :param character: A dictionary representing the character's state, including if they are in a tree or not.
    :param always: A boolean indicating whether to always generate a berry.
    :postcondition: The generated item will have a type and name, and may include additional data (like berry
                    color).
    :return: A dictionary representing the generated item, or None if no item is generated.

    >>> my_character = {"InTree": True}
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

    >>> game_board = {
    ...     (0, 0): None,
    ...     (1, 1): "TreeTrunk",
    ... }
    >>> my_character = {"FinalChallengeCompleted": False, "InTree": False}
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
    if board.get(location) in ["TreeTrunk", "Moss"]:
        return None
    if random.randint(1, ANIMAL_PROBABILITY) == 1:
        return generate_animal(character)
    else:
        return generate_item(character)


def stringify_item(entity: dict) -> str:
    """
    Convert an item into a string representation.

    :param entity: the item to be converted to string
    :precondition: entity must be a well-formed dictionary representing the item
    :postcondition: if the item is a berry, return the colour of the berry concatenated with "Berry",
                    otherwise, return the name of the item
    :raises TypeError:
    :return: a string representation of the item

    >>> example_item = {
    ...     "Type": "Item",
    ...     "Name": "Berry",
    ...     "Data": "Red"}
    >>> stringify_item(example_item)
    "Red Berry"
    >>> example_item = {
    ...     "Type": "Item",
    ...     "Name": "Catnip",
    ...     "Data": None}
    >>> stringify_item(example_item)
    "Catnip"
    """
    if entity["Type"] != "Item":
        raise TypeError(f"Expected entity type 'Item', got '{entity['Type']}'")
    if entity["Name"] == "Berry":
        return entity["Data"] + " Berry"
    else:
        return entity["Name"]


def item_input_to_entity(item_input: list[str]) -> dict:
    """
    Construct an entity dictionary from a list of strings representing the user input for an item.

    Essentially does the reverse of stringify_item.

    Accepts a tokenized representation of a user input of "ItemName" or "Attribute ItemName".
    For example, "Catnip" or "Red Berry" respectively. Tokens other than the first and second one will be ignored.
    This function does not validate whether the tokens are valid item selections as that is the responsibility of
    functions that consume the item.

    :param item_input: a list of strings representing the user input for an item
    :precondition: item_input must be a list containing a single string representing the item name,
                   or a list containing two strings where the second string is the name of the item and the first string
                   is the attribute of the item
    :postcondition: constructs an entity dictionary from a list of strings representing the user input for an item
    :return: an entity dictionary representing the item

    >>> item_input_to_entity(["Catnip"])
    {'Type': 'Item', 'Data': None, 'Name': 'Catnip'}
    >>> item_input_to_entity(["Red", "Berry"])
    {'Type': 'Item', 'Data': 'Red', 'Name': 'Berry'}
    >>> item_input_to_entity(["Nonsensical", "Nonsense", "ThisWillBeIgnored"])
    {'Type': 'Item', 'Data': 'Nonsensical', 'Name': 'Nonsense'}
    """
    entity = {
        "Type": "Item",
        "Data": None
    }
    if len(item_input) == 1:
        entity["Name"] = item_input[0]
    else:
        entity["Name"] = item_input[1]
        entity["Data"] = item_input[0]
    return entity


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
    elif entity["Name"] == "Berry" and entity["Data"] is not None:
        character["Inventory"]["Berries"][entity["Data"]] += 1
        print(f"💼 You picked up a {entity['Data']} berry.")
    else:
        print(f"The item is malformed and could not be picked up!")


def generate_reward(character: dict, animal_name: str):
    """
    Generate a reward for helping an animal.

    Randomly generates between 1 and a number of items corresponding to the level of the character.

    :param animal_name: the name of the animal giving the reward
    :precondition: animal_name must be a string representing an animal
    :param character: the character being rewarded
    :precondition: character must be a well-formed dictionary representing a character
    :postcondition: adds between 1 and a number of random items corresponding to the level of the character to the
                    inventory of the character
    """
    rewards_count = random.randint(1, character["Level"])
    print(f"The {animal_name} gave you {rewards_count} items as a sign of their gratitude!")
    print("You received the following items:")
    for reward in zip(range(rewards_count), itertools.count(1)):
        reward_item = generate_item(character, True)  # Generate a random item
        pick_up_item(character, reward_item)  # Add the item to the player's inventory
        print(f" {reward[1]}. a {stringify_item(reward_item)}")
