from config import BERRY_TREATMENTS


def validate_berry(color: str, ailments: list[str]) -> bool:
    if BERRY_TREATMENTS[color] in ailments:
        ailments.remove(BERRY_TREATMENTS[color])
        return True
    else:
        if "Starving" in ailments:
            ailments.remove("Starving")
            return True
        else:
            return False
