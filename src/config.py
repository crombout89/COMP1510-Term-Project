# Board sizes
GROUND_X_SCALE = 12
GROUND_Y_SCALE = 12
TREE_SCALE_OPTIONS = [1, 3, 5, 7, 9]

# Probabilities
# Higher number is less likely because they are used as the upper bound of random.randint
# A value of 5 is a 1/5 probability, a value of 10 is a 1/10 probability, etc
ANIMAL_PROBABILITY = 5
SILVERVINE_PROBABILITY = 100
CATNIP_PROBABILITY = 20
BERRY_PROBABILITY = 5

# Multipliers
UNTIL_NEXT_LEVEL_MULTIPLIER = 5  # Multiplier for many animals the player has to help before leveling up
CATNIP_TUMMY_MULTIPLIER = 2  # Multiplier for how many points to add to the tummy if a character eats Catnip
SILVERVINE_TUMMY_MULTIPLIER = 4  # Multiplier for how many points to add to the tummy if a character eats Silvervine

# Base values
SUBTRACT_FROM_TUMMY_IF_MOVE = 1  # How many points to subtract from the tummy if a character moves one tile
SUBTRACT_FROM_TUMMY_IF_CLIMB = 5  # How many points to subtract from the tummy if a character climbs up or down a tree
ADD_TO_TUMMY_IF_EAT_ITEM = 25  # How many points to add to the tummy if a character eats an item
CATNIP_EXTRA_ENERGY = 25   # How much extra energy to give to the player if they eat Catnip
SILVERVINE_EXTRA_ENERGY = 50  # How much extra energy to give to the player if they eat Silvervine

# Entity attribute options
ANIMAL_OPTIONS = ["Mouse", "Squirrel", "Chipmunk", "Mole", "Shrew", "Hedgehog", "Sparrow", "Robin", "Finch", "Crow",
                  "Raven", "Bunny", "Cricket", "Spider", "Snake"]
AILMENT_OPTIONS = ["Injured", "Poisoned", "Dehydrated", "Burned", "Sad", "Starving"]
BERRY_COLOR_OPTIONS = ["Red", "Green", "Blue", "Yellow", "Purple"]

# Other configurations
BERRY_TREATMENTS = {
    # "Berry colour": "Treats this ailment"
    "Red": "Injured",
    "Green": "Poisoned",
    "Blue": "Dehydrated",
    "Yellow": "Burned",
    "Purple": "Sad",
}
CHARACTER_DEFAULT_ATTRIBUTES = {
    "Name": "CHARACTER_NAME_PLACEHOLDER",
    "Level": 1,
    "UntilNextLevel": 5,
    "InTree": False,
    "GroundCoordinates": (0, 0),
    "TreeCoordinates": (0, 0),
    "Tummy": 100,
    "ExtraEnergy": 0,
    "AnimalsHelped": 0,
    "FinalChallengeCompleted": None,
    "Inventory": {
        "Berries": {
            "Red": 1,
            "Green": 1,
            "Blue": 1,
            "Yellow": 1,
            "Purple": 1
        },
        "Catnip": 0,
        "SilverVine": 0
    }
}
