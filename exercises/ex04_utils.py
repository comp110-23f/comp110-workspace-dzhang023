"""Docstring."""
__author__ = "730630815"


def all(int_list: list[int], indiv_int: int) -> bool:
    """Finds if all of the numbers in a list are equal to another specified number."""
    index = 0
    while index <= len(int_list):
        if int_list[index] != indiv_int:
            return False
        index += 1
    return True


def max(int_list: list[int]) -> int:
    """Finds the maximum value in a list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    curr_max = int_list[0]
    index = 0
    while index <= len(int_list):
        if int_list[index] >= curr_max:
            curr_max = int_list[index]
        index += 1
    return curr_max


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Finds if two provided lists are equal to one another."""
    if len(list_one) != len(list_two):
        return False
    index = 0
    while index <= len(list_one):
        if list_one[index] != list_two[index]:
            return False
        index += 1
    return True
