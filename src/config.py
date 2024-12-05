# Board sizes
GROUND_X_SCALE = 12
GROUND_Y_SCALE = 12
TREE_SCALE_OPTIONS = (1, 3, 5, 7, 9)

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
CATNIP_EXTRA_ENERGY = 25  # How much extra energy to give to the player if they eat Catnip
SILVERVINE_EXTRA_ENERGY = 50  # How much extra energy to give to the player if they eat Silvervine
NAP_EXTRA_ENERGY = 5  # How much extra energy to give to the player if they take a nap

# Entity attribute options
ANIMAL_OPTIONS = ("Mouse 🐁", "Squirrel 🐿️", "Duck 🪿", "Mole 🐀", "Skunk 🦨", "Hedgehog 🦔", "Grasshopper 🦗",
                  "Robin 🐦", "Raccoon 🦝", "Owl 🦉", "Raven 🐦‍⬛", "Bunny 🐇", "Cricket 🪳", "Spider 🕷", "Snake 🐍")
AILMENT_OPTIONS = ("Injured", "Poisoned", "Dehydrated", "Burned", "Sad", "Starving")
BERRY_COLOR_OPTIONS = ("Red", "Green", "Blue", "Yellow", "Purple")

# Other configurations
BERRY_TREATMENTS = (
    # "Berry colour": "Treats this ailment"
    ("Red", "Injured"),
    ("Green", "Poisoned"),
    ("Blue", "Dehydrated"),
    ("Yellow", "Burned"),
    ("Purple", "Sad")
)
CHARACTER_DEFAULT_ATTRIBUTES = (
    ("Name", "CHARACTER_NAME_PLACEHOLDER"),
    ("Level", 1),
    ("UntilNextLevel", 5),
    ("InTree", False),
    ("GroundCoordinates", (0, 0)),
    ("TreeCoordinates", (0, 0)),
    ("Tummy", 100),
    ("ExtraEnergy", 0),
    ("AnimalsHelped", 0),
    ("FinalChallengeCompleted", None),
)
CHARACTER_DEFAULT_INVENTORY_TOP_LEVEL = (
    ("Catnip", 0),
    ("Silvervine", 0)
)
CHARACTER_DEFAULT_INVENTORY_BERRIES = (
    ("Red", 1),
    ("Green", 1),
    ("Blue", 1),
    ("Yellow", 1),
    ("Purple", 1)
)
DIRECTION_MAPPING = (
    # "Direction input": (Direction vector)
    ("W", (0, -1)),  # Decrement y coordinate to move up
    ("A", (-1, 0)),  # Decrement x coordinate to move left
    ("S", (0, 1)),  # Increment y coordinate to move down
    ("D", (1, 0))  # Increment x coordinate to move right
)
