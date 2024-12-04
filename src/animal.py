import random

from .character import get_item_from_inventory
from .config import BERRY_TREATMENTS
from .descriptions import sick_animal_description, cured_animal_description
from .entity import stringify_item, generate_item, pick_up_item


def validate_berry(color: str, ailments: list[str]) -> bool:
    """
    Validate and treat an animal's ailment using a berry based on its color.

    :param color: A string representing the color of the berry.
    :param ailments: A list of strings representing the character's current ailments.
    :precondition: color must be a valid key in the BERRY_TREATMENTS dictionary.
    :precondition: ailments must be a list of strings representing the animal's ailments.
    :postcondition: If the berry can treat an ailment, it will be removed from the list of ailments.
    :return: True if an ailment was successfully treated, False otherwise.

    >>> BERRY_TREATMENTS = {
    ...     "Red": "Burn",
    ...     "Blue": "Fever",
    ...     "Green": "Nausea"
    ... }
    >>> ailments = ["Burn", "Starving"]
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
    if BERRY_TREATMENTS[color] in ailments:
        ailments.remove(BERRY_TREATMENTS[color])
        return True
    else:
        if "Starving" in ailments:
            ailments.remove("Starving")
            return True
        else:
            return False


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
            character["AnimalsHelped"] += 1
            character["UntilNextLevel"] -= 1
            # Handle Final Challenge or Level Up
            if name == "FinalChallenge":
                character["FinalChallengeCompleted"] = True
                print("Congratulations! You have completed the Final Challenge! 🎉")

                return
