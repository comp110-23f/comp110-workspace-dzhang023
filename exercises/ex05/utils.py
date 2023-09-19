"""Docstring."""
__author__= "730630815"
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