"""Docstring."""
__author__ = "730630815"
def all(intlist: list[int], indiv_int:int) -> bool:
    for num in intlist:
        if num != indiv_int:
            return False
    return True
def max(intlist: list[int]) -> int:
    if len(intlist) == 0:
        raise ValueError("max() arg is an empty List")
    curr_max = intlist[0]
    for num in intlist:
        if num >= curr_max:
            curr_max = num
    return curr_max
def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    for index, num in enumerate(list_one):
        if num != list_two[index]:
            return False
    return True