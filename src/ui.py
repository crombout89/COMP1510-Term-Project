import random

from .animal import validate_berry
from .character import get_item_from_inventory
from .entity import generate_item, stringify_item
from .config import UNTIL_NEXT_LEVEL_MULTIPLIER


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
    print("Thanks to your purr-severance and kindness, the forest is thriving again.")
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
    :raises KeyError: If required keys are missing from the `character` or `board` dictionaries.
    :raises ValueError: If the user enters an unsupported or invalid action.
    :raises SystemExit: If the user exceeds the maximum number of invalid input attempts
                        or interrupts the program.
    :raises Exception: For unexpected errors that occur during action processing.
    :return: A dictionary representing the processed action with keys "Type" and "Data".

        >>> character = {
    ...     "Position": (0, 0),
    ...     "Tummy": 50,
    ...     "ExtraEnergy": 0,
    ...     "Inventory": ["Catnip", "Fish"],
    ...     "Level": 2
    ... }
    >>> board = {
    ...     "Tiles": [["Grass", "Moss"], ["Tree", "Rock"]]
    ... }

    # Example 1: User enters a movement command
    >>> get_action_input(character, board)  # User enters 'W' +SKIP
    Enter an action: W
    {'Type': 'Move', 'Data': (0, -1)}

    # Example 2: User enters an Eat command
    >>> get_action_input(character, board)  # User enters 'Eat Catnip' +SKIP
    Enter an action: Eat Catnip
    You eat the Catnip. Yum!
    {'Type': 'Eat', 'Data': ['Catnip']}

    # Example 3: User enters a Check command
    >>> get_action_input(character, board)  # User enters 'Check Tummy' +SKIP
    Enter an action: Check Tummy
    Your tummy level is: 50
    {'Type': 'Check', 'Data': ['Tummy']}

    # Example 4: User enters an invalid action
    >>> get_action_input(character, board)  # User enters 'Fly' +SKIP
    Enter an action: Fly
    Invalid action. Valid actions are: W, A, S, D, Climb, Eat, Nap, Check, Help.

    # Example 5: User attempts to Nap in an invalid location
    >>> get_action_input(character, board)  # User enters 'Nap' +SKIP
    Enter an action: Nap
    You can't nap here! You are at (0, 0), but you need to find some moss.

    # Example 6: User calls Help
    >>> get_action_input(character, board)  # User enters 'Help' +SKIP
    Enter an action: Help
    Available actions: W, A, S, D (move), Climb, Eat, Nap, Check, Help.
    Use 'Check <Tummy|Level|Inventory>' to check specific attributes.
    """
    valid_actions = ["W", "A", "S", "D", "Climb", "Eat", "Nap", "Check", "Help"]
    valid_attributes = ["Tummy", "Level", "Inventory"]
    retries = 0
    max_retries = 5

    # Validate that required keys exist in character and board dictionaries
    required_character_keys = ["Position", "Tummy", "ExtraEnergy", "Inventory"]
    for key in required_character_keys:
        if key not in character:
            raise KeyError(f"Missing key '{key}' in character data.")

    if "Tiles" not in board:
        raise KeyError("Missing 'Tiles' in board data.")

    while retries < max_retries:
        try:
            # Get the user's action
            selected_action = input("Enter an action: ").strip()

            # Handle empty input
            if not selected_action:
                print("Input cannot be empty. Please enter a valid action.")
                retries += 1
                continue

            # Normalize input and split into tokens
            selected_action = selected_action.title()
            action_tokens = selected_action.split()
            action = {
                "Type": action_tokens[0],  # e.g., "Eat"
                "Data": action_tokens[1:] if len(action_tokens) > 1 else []  # e.g., ["Catnip"]
            }

            # Validate action type
            if action["Type"] not in valid_actions:
                print(f"Invalid action. Valid actions are: {', '.join(valid_actions)}")
                retries += 1
                continue

            # Handle specific actions
            if action["Type"] == "Climb":
                if not CLIMB(character, board):
                    print("There is no tree for you to climb here!")
                    continue
                else:
                    print("You successfully climbed the tree!")

            elif action["Type"] == "Eat":
                if not action["Data"]:
                    print("Specify what to eat! Example: 'Eat Catnip'")
                    retries += 1
                    continue
                item = action["Data"][0]

                # Validate inventory
                if "Inventory" not in character or not isinstance(character["Inventory"], list):
                    print("Your inventory is missing or corrupted. Unable to eat.")
                    retries += 1
                    continue

                # Check if item exists in inventory
                if item not in character["Inventory"]:
                    print(f"You cannot eat {item}. It's not in your inventory.")
                    retries += 1
                    continue

                # Call the EAT function
                if not EAT(character, item):
                    print(f"Failed to eat {item}. Try again.")
                    retries += 1
                    continue

            elif action["Type"] == "Nap":
                if not NAP(character, board):
                    current_location = CURRENT_LOCATION(character)
                    print(f"You can't nap here! You are at {current_location}, but you need to find some moss.")
                    retries += 1
                    continue

            elif action["Type"] == "Check":
                if not action["Data"]:
                    print("Specify what to check! Example: 'Check Tummy'")
                    retries += 1
                    continue
                attribute = action["Data"][0]
                if attribute not in valid_attributes:
                    print(f"Invalid attribute to check. Valid options are: {', '.join(valid_attributes)}")
                    retries += 1
                    continue

                # Call the appropriate check function
                if attribute == "Tummy":
                    CHECK_TUMMY(character)
                elif attribute == "Inventory":
                    print(f"Your inventory contains: {', '.join(character['Inventory'])}")
                elif attribute == "Level":
                    print(f"Your current level is: {character.get('Level', 'Unknown')}")

            elif action["Type"] == "Help":
                print("Available actions: W, A, S, D (move), Climb, Eat, Nap, Check, Help.")
                print("Use 'Check <Tummy|Level|Inventory>' to check specific attributes.")
                continue

            elif action["Type"] in ["W", "A", "S", "D"]:
                # Determine movement direction
                if action["Type"] == "W":
                    action["Data"] = (0, -1)
                elif action["Type"] == "A":
                    action["Data"] = (-1, 0)
                elif action["Type"] == "S":
                    action["Data"] = (0, 1)
                elif action["Type"] == "D":
                    action["Data"] = (1, 0)
                action["Type"] = "Move"

                # Validate movement (optional, depending on your game logic)
                if not CAN_MOVE(character, board, action["Data"]):
                    print("You can't move in that direction!")
                    retries += 1
                    continue

            # Return the action if all validations pass
            return action

        except KeyError as e:
            print(f"Unexpected error: Missing key {e}. Please check your input.")
            retries += 1
        except ValueError as e:
            print(f"Unexpected error: {e}. Please try again.")
            retries += 1
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            raise SystemExit
        except EOFError:
            print("\nInput terminated. Exiting...")
            raise SystemExit
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            retries += 1

        # Handle max retries
        if retries >= max_retries:
            print("Too many invalid attempts. Exiting...")
            raise SystemExit


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

    >>> character = {
    ...     "Level": 2,
    ...     "UntilNextLevel": 1,
    ...     "Inventory": {"Berries": {"Red": 2, "Green": 1, "Blue": 0}},
    ...     "AnimalsHelped": 3,
    ...     "FinalChallengeCompleted": False
    ... }
    >>> entity = {"Name": "Bunny", "Ailments": ["Injured"]}
    >>> # Mock implementations of required functions:
    >>> def GET_ITEM_FROM_INVENTORY(character, berry): return berry in character["Inventory"]["Berries"] and character["Inventory"]["Berries"][berry] > 0
    >>> def VALIDATE_BERRY(berry, ailments): return berry == "Red" and "Injured" in ailments
    >>> BERRY_TREATMENTS = {"Red": "Injured", "Green": "Sick"}
    >>> def GENERATE_ITEM(character, is_random): return "Magic Herb"
    >>> def PICK_UP_ITEM(character, item): character["Inventory"].setdefault(item, 0); character["Inventory"][item] += 1
    >>> help_animal(character, entity)  # Simulate helping the animal
    You have come across a sad Bunny, and they aren't doing very well...
    Bunny: I don't feel so good, I have Injured. Can you help me?
    Which color berry would you like to give the animal? red
    Hooray! You have 'Red' in your inventory!
    The berry 'Red' successfully treated one of the animal's ailments! 🩹
    You used one 'Red' berry. Remaining: 1
    The Bunny has been completely cured of their ailments!
    The Bunny is so grateful! It gives you 3 random items as a reward!
    You received: Green Berry!
    You received: Catnip!
    You received: Yellow Berry!
    Congratulations! You leveled up to Level 2!
    You need to help 15 more animals to reach the next level.
    Current Level: 2, Animals Helped: 4
    """
    name = entity.get("Name", "")
    ailments = entity.get("Data", [])
    # inventory = character.get("Inventory", {}).get("Berries", {})
    level = character.get("Level", 1)

    # Special handling for the Final Challenge
    if name == "FinalChallenge":
        print("You are accepting the Final Challenge!")
        print("You need to give the sick animal a special medicine made from a recipe of berries to cure them,"
              "or press ENTER to skip.")
    else:
        print(f"You have come across a {name}, and they aren't doing very well...")
        print(f"{name}: I don't feel so good, I am {', '.join(ailments)}. Can you help me?")
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
        try:
            has_item = get_item_from_inventory(character, berry)
        except Exception as e:
            print(f"Error checking inventory for '{berry}': {e}")
            return
        else:
            if not has_item:
                print(f"Oh no! You don't have any '{berry_color}' berries in your inventory.")
                continue

        print(f"Hooray! You have '{berry_color}' berry in your inventory!")

        # Validate the berry as a treatment for the ailments
        try:
            valid_treatment = validate_berry(berry_color, ailments)
        except Exception as e:
            print(f"Error validating '{berry}' as a treatment: {e}")
            return
        else:
            if not valid_treatment:
                print(f"The '{berry_color}' was not effective, the animal's ailments were not cured. 😢")
                return

        print(f"The berry '{berry}' successfully treated one of the animal's ailments! 🩹")

        # This is already implemented by validate_berry
        """
        # Find and remove the treated ailment
        try:
            treated_ailment = BERRY_TREATMENTS[berry]
        except KeyError as e:
            print(f"Error: '{berry}' is not a valid treatment: {e}")
            return
        else:
            if treated_ailment in ailments:
                ailments.remove(treated_ailment)
        """

        # This is already implemented by get_item_from_inventory
        """
        # Deduct the berry from the inventory
        try:
            if inventory.get(berry, 0) > 0:
                inventory[berry] -= 1
            else:
                raise ValueError(f"Not enough '{berry}' berries in inventory.")
        except ValueError as e:
            print(f"Error deducting berry: {e}")
            return
        else:
            print(f"You used one '{berry}' berry. Remaining: {inventory[berry]}")
        """

        # Check if all ailments are cured
        if len(ailments) == 0:
            print(f"The {name} has been completely cured of their ailments!")

            # Generate rewards
            try:
                reward = random.randint(2, 1 + level)
            except ValueError as e:
                print(f"Error generating rewards: {e}")
                reward = 0
            else:
                print(f"The {name} is so grateful! It gives you {reward} items as a reward!")

            # Reward the player with random items
            for _ in range(reward):
                try:
                    reward_item = generate_item(character, True)  # Generate a random item
                    pick_up_item(character, reward_item)  # Add the item to the player's inventory
                except Exception as e:
                    print(f"Error generating or picking up reward item: {e}")
                else:
                    print(f"You received: {stringify_item(reward_item)}!")

            # Update character stats (AnimalsHelped and UntilNextLevel)
            try:
                character["AnimalsHelped"] = character.get("AnimalsHelped", 0) + 1
                character["UntilNextLevel"] = max(0, character.get("UntilNextLevel", 0) - 1)
            except Exception as e:
                print(f"Error updating character stats: {e}")
                return
            else:
                # Handle Final Challenge or Level Up
                if name == "FinalChallenge":
                    character["FinalChallengeCompleted"] = True
                    print("Congratulations! You have completed the Final Challenge! 🎉")
                    return
                # This is already implemented in update_level
                """
                if character["UntilNextLevel"] == 0:
                    try:
                        character["Level"] += 1  # Increment the level in the character dictionary
                    except Exception as e:
                        print(f"Error leveling up: {e}")
                        return
                    else:
                        print(f"Congratulations! You leveled up to Level {character['Level']}!")

                        # Reset UntilNextLevel based on the new level
                        # UNTIL_NEXT_LEVEL_MULTIPLIER = 5  # You can adjust this multiplier
                        character["UntilNextLevel"] = UNTIL_NEXT_LEVEL_MULTIPLIER * character["Level"]
                        print(f"You need to help {character['UntilNextLevel']} more animals to reach the next level.")
                
            finally:
                print(f"Current Level: {character['Level']}, Animals Helped: {character['AnimalsHelped']}")
            """
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

    >>> example_character = {
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
    >>> example_item = {
    ...     "Type": "Item",
    ...     "Name": "Catnip",
    ...     "Data": None
    ... }
    >>> example_character["Inventory"]["Catnip"]
    0
    >>> pick_up_item(example_character, example_item)
    💼 You picked up a Catnip.
    >>> example_character["Inventory"]["Catnip"]
    1
    >>> example_item = {
    ...     "Type": "Item",
    ...     "Name": "Berry",
    ...     "Data": "Red"
    ... }
    >>> example_character["Inventory"]["Berries"]["Red"]
    0
    >>> pick_up_item(example_character, example_item)
    💼 You picked up a Red Berry.
    >>> example_character["Inventory"]["Berries"]["Red"]
    1
    """
    if entity["Type"] != "Item":
        raise TypeError(f"Expected entity type 'Item', got '{entity['Type']}'")
    if entity["Name"] == "Catnip" or entity["Name"] == "Silvervine":
        character["Inventory"][entity["Name"]] += 1
    else:
        character["Inventory"]["Berries"][entity["Data"]] += 1
    print(f"💼 You picked up a {stringify_item(entity)}.")


def describe_location(character: dict, board: dict):
    pass


