import random
from typing import Dict


def sick_animal_description(animal: Dict[str, str]) -> str:
    """
    Generate a random description for a sick animal based on its type or name.

    :param animal: A dictionary representing the animal entity.
                   Example: {"Type": "Animal", "Name": "Rabbit", "Data": ["Injury", "Exhaustion"]}
    :precondition: animal must be a dictionary representing the animal entity.
    :postcondition: Returns a randomly selected string from the list of descriptions.
    :return: A string describing the sick animal.
    """
    # Validate input
    if not isinstance(animal, dict) or not animal:
        return "A mysterious creature lies here, suffering in silence."

    # Ensure the animal has a "Name" key
    name = animal.get("Name", "creature")  # Default to "creature" if no name is provided

    # Handle ailments, defaulting to "unknown ailments" if none exist
    ailments = ", ".join(animal.get("Data", [])) or "unknown ailments"
    if len(animal.get("Data", [])) > 1:
        ailments = " and ".join([", ".join(animal["Data"][:-1]), animal["Data"][-1]])

    descriptions = [
        f"A very frail {name} lies here, shivering and weak. Its big eyes look up at you, pleading for help.",
        f"You see a sickly {name} curled up on the ground, its breathing shallow and labored.",
        f"A wounded {name} rests here, its fur matted and its body trembling. It needs care urgently.",
        f"A fragile little {name} lies here, letting out faint cries. It looks like it hasn't eaten in days.",
        f"A trembling {name} is lying on its side, struggling to lift its head. It looks utterly exhausted.",
        f"The {name}'s body is covered in scratches and bruises. Its eyes are dull, and it has no strength to move.",
        f"The poor {name} lets out a faint, pitiful sound as it struggles to breathe. It needs help quickly.",
        f"A battered and weary {name} lies here, its body showing signs of neglect and pain.",
    ]

    description = random.choice(descriptions)
    description += f" It appears to be suffering from {ailments}."
    return description


def cured_animal_description(animal: Dict[str, str]) -> str:
    """
    Generate a random description for a cured animal based on its type or name.
    The descriptions reflect gratitude and trust between the animal and the cat.

    :param animal: A dictionary representing the animal entity.
                   Example: {"Type": "Animal", "Name": "Rabbit", "Data": ["Injury", "Exhaustion"]}
    :precondition: animal must be a dictionary representing the animal entity.
    :postcondition: Returns a randomly selected string from the list of descriptions.
    :return: A string describing the cured animal.
    """
    # Validate input
    if not isinstance(animal, dict) or not animal:
        return "An unknown creature looks at you with gratitude before disappearing."

    # Ensure the animal has a "Name" key
    name = animal.get("Name", "creature")  # Default to "creature" if no name is specified

    # Randomized descriptions for cured animals
    descriptions = [
        f"The {name} nuzzles against you, its trust in you clear, before hopping off happily.",
        f"The {name} looks at you with kind, shining eyes before brushing against your fur in gratitude.",
        f"The {name} gently presses its head against yours in a loving gesture, then runs off into the forest.",
        f"The {name}'s tail wags happily, and it playfully nudges you before heading off.",
        f"The {name} gives you a final, grateful glance, as though promising to remember your kindness.",
        f"The {name} leaps away joyfully, but not before giving you a warm, trusting look.",
        f"The {name} purrs softly and rubs against you before bounding off into the distance.",
    ]

    return random.choice(descriptions)


def forest_patch_description() -> str:
    """
    Generate a random description for an empty forest patch.

    :return: A string describing a randomized forest patch.
    """
    grass_descriptions = [
        "A patch of soft green grass sways gently in the breeze.🌱",
        "A small clearing reveals lush grass, speckled with dew.🌱💦",
        "The ground here is covered in short, vibrant grass, cool beneath your paws.🌱",
        "A patch of grass grows unevenly here, with tufts sticking out at odd angles.🌾",
        "The grass here is dotted with tiny wildflowers, adding bursts of color.🌿🪻"
    ]

    flower_descriptions = [
        "A cluster of delicate wildflowers blooms here, their petals swaying gently.🌺",
        "Bright yellow daisies pop up from the ground, cheerful and vibrant.🌼🌿",
        "Tiny bluebells grow together in a small patch, their color vivid against the green.🪻🌿",
        "A scattering of white flowers dots the forest floor, their scent faint but pleasant.🤍🌸",
        "A few small flowers grow here, their colors muted but beautiful.🌹🌷"
    ]

    rock_descriptions = [
        "A smooth, flat stone lies here, partially covered in dirt.🪨",
        "A cluster of small, round rocks is scattered across the ground.🪨🪨",
        "A single large boulder juts out of the ground, its surface cool and rough.🪨🧊",
        "Pebbles and stones litter the area, their patterns and shapes fascinating.⚪🪨",
        "A jagged rock rises from the dirt, its surface weathered by time.🗿"
    ]

    dirt_descriptions = [
        "The ground here is bare, with patches of dry grass exposed.🌾🟤",
        "Loose soil covers the area, scattered with fallen leaves.🟤🍂",
        "A patch of dirt interrupts the grass, its surface soft and crumbly.🟤🌱",
        "The earth here is packed tightly, with a few cracks running through it.🟤⚡",
        "Bare dirt stretches across this spot, with a faint trail left by passing animals.🟤🐾"
    ]

    leaf_descriptions = [
        "A thick layer of fallen leaves carpets the ground, crunching softly underfoot.🍂🍁",
        "Golden and brown leaves are scattered here, remnants of autumn.🍁🍂",
        "Dry leaves lie in a small pile, rustling slightly in the breeze.🍂🍃",
        "The forest floor is littered with leaves, their edges curled and brittle.🥀🍂",
        "A single, vibrant red leaf lies here, standing out against the earthy tones.🍁❤️"
    ]

    mushroom_descriptions = [
        "A small cluster of mushrooms sprouts here, their caps dotted with white specks.🍄⚪",
        "Tiny mushrooms grow in a ring, their delicate shapes almost magical.🍄✨",
        "A single large mushroom stands here, its cap wide and flat.🍄🟤",
        "Several small, brightly colored mushrooms grow here, adding a splash of red and yellow.🍄🔴🟡",
        "A few pale mushrooms sprout from the dirt, their stems thin and fragile.🍄🤍"
    ]

    # Combine all descriptions into one list
    all_descriptions = (
        grass_descriptions +
        flower_descriptions +
        rock_descriptions +
        dirt_descriptions +
        leaf_descriptions +
        mushroom_descriptions
    )

    # Return a random choice
    return random.choice(all_descriptions)


def tree_patch_description() -> str:
    """
    Generate a random description for empty tree patches.

    :return: A random string describing the empty tree patch.
    """

    treetop_descriptions = [
        "The treetop sways gently in the breeze, a serene spot high above the ground.🍃🌬️",
        "Sunlight filters through the leaves, creating a warm, dappled pattern on the treetop.🌞🌳",
        "An empty treetop provides a clear view of the forest below, peaceful and quiet.🌳👀",
        "Soft leaves rustle overhead, making the treetop a perfect place to unwind.🍃🌈",
        "The treetop is alive with the sounds of nature, a tranquil retreat from the forest floor.🌳🍂",
        "Leaves gently sway, casting playful shadows on the ground below, inviting you to stay.🌿🌞",
        "The air is fragrant with the scent of pine, making this treetop a refreshing escape.🌲🌬️",
        "A gentle breeze dances through the treetops, carrying the whispers of the forest.🍃💨",
        "The treetop offers a serene vantage point, where the sky meets the forest canopy.🌳☁️",
        "Clusters of leaves provide a natural canopy, creating a peaceful haven above.🍃🌌"
    ]

    # Combine all descriptions into one list
    all_descriptions = treetop_descriptions

    # Return a random choice
    return random.choice(all_descriptions)


def moss_description() -> str:
    """
    Generate a random description for a moss patch.

    :return: A string describing a randomized moss patch.
    """
    moss_descriptions = [
        "A soft patch of moss spreads across the ground, inviting for a quick nap.🌿💤",
        "Thick, lush moss cushions the earth here, a perfect resting spot.🍃😊",
        "A vibrant green moss blanket covers the ground, cool and refreshing underfoot.🌱🌼",
        "Moss grows in a thick layer, its texture like velvet, beckoning you to relax.🍃🛌",
        "A tuft of moss peeks out from between the roots, soft and inviting.🌿✨"
    ]
    return random.choice(moss_descriptions)