"""Using lists and its its utilities."""
__author__ = 730383494


def all(list_ints: list[int], integer: int) -> bool:
    """Checks if all integers in a list are the same as a single integer."""
    counter: int = 0
    if len(list_ints) == 0:
        return False
    while counter < len(list_ints):
        if list_ints[counter] == integer:
            counter = counter + 1
        else:
            return False
    return True


def max(list_ints: list[int]) -> int:
    """Chooses largest number in a list."""
    if len(list_ints) == 0:
        raise ValueError("max() arg is an empty List")
    counter: int = 0
    number: int = list_ints[0]
    while counter < len(list_ints):
        if list_ints[counter] > number:
            number = list_ints[counter]
        counter = counter + 1
    return number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Decides if two lists are the exact same."""
    counter: int = 0
    if len(list_1) != len(list_2):
        return False
    while len(list_1) == len(list_2) and counter < len(list_1):
        if list_1[counter] == list_2[counter]:
            counter = counter + 1
        else:
            return False
    return True