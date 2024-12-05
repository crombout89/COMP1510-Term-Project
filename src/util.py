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


def dict_from_tuple_of_tuples(tuple_of_tuples: tuple) -> dict:
    """
    Convert a tuple of tuples into a dictionary.

    :param tuple_of_tuples: the tuple of tuples to be converted
    :precondition: tuple_of_tuples must be a tuple of tuples, each nested tuple must only be of length two
                   and have the key as the first element and the value as the second element
    :postcondition: constructs a dictionary from the tuple of tuples
    :return: the dictionary corresponding to the tuple of tuples

    >>> example_structure = (
    ...     ("key1", "value1"),
    ...     ("key2", 2),
    ...     ("key3", False),
    ...     (4, "value4"),
    ...     ((1, 2), (3, 4)),
    ...     (None, None),
    ... )
    >>> dict_from_tuple_of_tuples(example_structure)
    {'key1': 'value1', 'key2': 2, 'key3': False, 4: 'value4', (1, 2): (3, 4), None: None}
    """
    return dict((key, value) for key, value in tuple_of_tuples)
