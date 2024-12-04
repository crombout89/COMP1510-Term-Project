def plural(how_many):
    """
    Returns 's' if the number of some object is not 1, returns an empty string otherwise.

    Used to add an 's' to a word to make it plural if there is more than one.

    >>> f"1 function{plural(1)}"
    "1 function"
    >>> f"2 closure{plural(2)}"
    "2 closures"
    >>> f'0 lambda{plural(0)}'
    "0 lambdas"
    """
    if how_many == 1:
        return "s"
    else:
        return ""
    