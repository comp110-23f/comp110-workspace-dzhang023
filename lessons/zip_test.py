"""Test my zip function."""

__author__ = '730630815'

from lessons.zip import zip


def test_five_characters() -> None:
    """Tests the zip function when given two lists of length 5."""
    key_list = ['A', 'B', 'C', 'D', 'E']
    val_list = [1, 2, 3, 4, 5]
    print(zip(key_list, val_list))


def test_empty_lists() -> None:
    """Tests zip function when given two empty lists."""
    key_list = []
    val_list = []
    print(zip(key_list, val_list))


def test_mismatched_lists() -> None:
    """Tests zip function when given two lists of different size."""
    key_list = ['A', 'B', 'C', 'D', 'E']
    val_list = [1, 2, 3, 4]
    print(zip(key_list, val_list))
    