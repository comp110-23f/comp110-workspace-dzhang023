"""Summing elements using different loops."""
__author__ = "730630815"


def w_sum(vals: list[float]) -> float:
    """Sums using a while loop."""
    sum: float = 0
    index = 0
    while index != len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sums using a for loop."""
    sum: float = 0
    for value in vals:
        sum += value
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sums using a for loop with a set range."""
    sum: float = 0
    val_list_len = len(vals)
    for index in range(val_list_len):
        sum += vals[index]
    return sum