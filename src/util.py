def plural(how_many: int) -> str:
    """
    Returns 's' if the number of some object is not 1, returns an empty string otherwise.

    Used to add an 's' to a word to make it plural if there is more than one.

    :param how_many: how many of some object there are
    :precondition: how_many must be a number
    :postcondition: determines whether a plural is needed depending on how_many
    :return: 's' if the how_many is not 1, an empty string otherwise

    >>> f"1 function{plural(1)}"
    "1 function"
    >>> f"2 closure{plural(2)}"
    "2 closures"
    >>> f'0 lambda{plural(0)}'
    "0 lambdas"
    """
    if how_many != 1:
        return "s"
    else:
        return ""
