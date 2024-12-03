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