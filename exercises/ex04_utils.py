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
def only_evens(list_ints: list[int]) -> list[int]:
    evenints = []
    for num in list_ints:
        if num % 2 == 0:
            evenints.append(num)
    return evenints
def concat(list1: list[int], list2: list[int]) -> list[int]:
    biglist = []
    for num in list1:
        biglist.append[num]
    for num in list2:
        biglist.append[num]
    return biglist
def sub(list_ints: list[int],startind:int, endind: int) -> list[int]:
    endlist = []
    for num in list_ints[startind:endind]:
        endlist.append(num)
    return endlist