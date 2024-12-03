from .config import BERRY_TREATMENTS


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
