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
    :return: A dictionary representing the processed action with keys "Type" and "Data".
    """
    # Validate the parameters
    if not isinstance(character, dict):
        raise TypeError("'character' must be a dictionary.")
    if not isinstance(board, dict):
        raise TypeError("'board' must be a dictionary.")

    valid_actions = ["W", "A", "S", "D", "Climb", "Eat", "Nap", "Check", "Help"]
    valid_attributes = ["Tummy", "Level", "Inventory"]

    while True:
        # Get the user's selected action
        try:
            selected_action = input("Enter an action: ").strip()
        except KeyboardInterrupt:
            print("\nInput interrupted. Exiting...")
            raise
        except EOFError:
            print("\nInput terminated unexpectedly.")

        # Check if the input is empty
        if not selected_action:
            print("Invalid action. Please enter a valid action to continue.")
            continue

        # Convert to title case and tokenize
        selected_action = selected_action.title()
        action_tokens = selected_action.split()
        action = {
            "Type": action_tokens[0],
            "Data": action_tokens[1:] if len(action_tokens) > 1 else []
        }

        # Validate "Type" cases
        if action["Type"] not in valid_actions:
            print(f"Invalid action. Valid actions are: {', '.join(valid_actions)}")

        # Handle specific "Type" cases
        if action["Type"] == "Check":
            # Validate the attributes in "Data"
            if not action["Data"] or action["Data"][0] not in valid_attributes:
                print(f"Invalid attribute. Valid attributes are: {', '.join(valid_attributes)}")





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
    ailments = entity.get("Ailments", [])
    inventory = character.get("Inventory", {}).get("Berries", {})
    level = character.get("Level", 1)

    # Special handling for the Final Challenge
    if name == "FinalChallenge":
        print("You are accepting the Final Challenge!")
        print("You need to give the sick animal a special medicine made from a recipe of berries to cure them,"
              "or press ENTER to skip.")
    else:
        print(f"You have come across a sad {name}, and they aren't doing very well...")
        print(f"{name}: I don't feel so good, I have {', '.join(ailments) if ailments else 'None'}. Can you help me?")
        print("You need to give them the correct berries to cure their ailments! Or, press ENTER to skip.")

    # Main loop to treat the animal
    while len(ailments) > 0:
        berry = input("Which color berry would you like to give the animal? ").strip().lower()
        if not berry:
            print("You skipped giving the animal a berry.")
            return

        berry = berry.title()  # Convert to title case for consistency

        # Check if the player has the berry in their inventory
        try:
            has_item = GET_ITEM_FROM_INVENTORY(character, berry)
        except Exception as e:
            print(f"Error checking inventory for '{berry}': {e}")
            return
        else:
            if not has_item:
                print(f"Oh no! You don't have any '{berry}' berries in your inventory.")
                continue

        print(f"Hooray! You have '{berry}' in your inventory!")

        # Validate the berry as a treatment for the ailments
        try:
            valid_treatment = VALIDATE_BERRY(berry, ailments)
        except Exception as e:
            print(f"Error validating '{berry}' as a treatment: {e}")
            return
        else:
            if not valid_treatment:
                print(f"The '{berry}' was not effective, the animal's ailments were not cured. 😢")
                return

        print(f"The berry '{berry}' successfully treated one of the animal's ailments! 🩹")

        # Find and remove the treated ailment
        try:
            treated_ailment = BERRY_TREATMENTS[berry]
        except KeyError as e:
            print(f"Error: '{berry}' is not a valid treatment: {e}")
            return
        else:
            if treated_ailment in ailments:
                ailments.remove(treated_ailment)

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
                print(f"The {name} is so grateful! It gives you {reward} random items as a reward!")

            # Reward the player with random items
            for _ in range(reward):
                try:
                    reward_item = GENERATE_ITEM(character, True)  # Generate a random item
                    pick_up_item(character, reward_item)  # Add the item to the player's inventory
                except Exception as e:
                    print(f"Error generating or picking up reward item: {e}")
                else:
                    print(f"You received: {reward_item}!")

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

                if character["UntilNextLevel"] == 0:
                    try:
                        character["Level"] += 1  # Increment the level in the character dictionary
                    except Exception as e:
                        print(f"Error leveling up: {e}")
                        return
                    else:
                        print(f"Congratulations! You leveled up to Level {character['Level']}!")

                        # Reset UntilNextLevel based on the new level
                        UNTIL_NEXT_LEVEL_MULTIPLIER = 5  # You can adjust this multiplier
                        character["UntilNextLevel"] = UNTIL_NEXT_LEVEL_MULTIPLIER * character["Level"]
                        print(f"You need to help {character['UntilNextLevel']} more animals to reach the next level.")
            finally:
                print(f"Current Level: {character['Level']}, Animals Helped: {character['AnimalsHelped']}")

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
