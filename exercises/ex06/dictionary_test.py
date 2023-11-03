"""Docstring."""

__author__ = "730630815"

import pytest
from dictionary import invert, favorite_color, count


# invert testing#

def test_invert_letters():
    test_dict_for_inversion: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    print(invert(test_dict_for_inversion))


def test_invert_numbers():
    test_dict_for_inversion: dict[str, str] = {'One': 'Two', 'Three': 'Four', 'Five': 'Six', 'Seven': 'Eight'}
    print(invert(test_dict_for_inversion))


def test_invert_error_testing():
    with pytest.raises(KeyError):
        test_dict_for_inversion: dict[str, str] = {'a': 'b', 'c': 'b', 'd': 'e', 'f': 'e'}
        print(invert(test_dict_for_inversion))
    print('KeyError raised.')


# favorite color testing#

def test_fave_color_blue():
    test_dict_for_colors: dict[str, str] = {'Alex': 'blue', "Ben": "blue", "Carl": 'blue', "Daniel": 'red',
                                            'Evan': 'red', "Francis": 'yellow'}
    print(favorite_color(test_dict_for_colors))


def test_fave_color_red():
    test_dict_for_colors: dict[str, str] = {'Alex': 'red', "Ben": "red", "Carl": 'blue', "Daniel": 'red', 'Evan': 'red',
                                            "Francis": 'yellow'}
    print(favorite_color(test_dict_for_colors))


def test_fave_color_tie():
    test_dict_for_colors: dict[str, str] = {'Alex': 'red', "Ben": "blue", "Carl": 'blue', "Daniel": 'red',
                                            'Evan': 'red', "Francis": 'blue'}
    print(favorite_color(test_dict_for_colors))


# count testing#

def test_count_singular_values():
    test_list_for_count: list[str] = ['a', 'b', 'c', 'd', 'e', 'f']
    print(count(test_list_for_count))


def test_count_multiple_values():
    test_list_for_count: list[str] = ['a', 'a', 'd', 'd', 'e', 'a', 'b']
    print(count(test_list_for_count))


def test_count_error():
    test_list_for_count: list[str] = [1, '3', 'd', 'd', 'e', 'a', 'b']
    print(count(test_list_for_count))


# alphabetize testing

def test_alpha_x():
    pass


def test_alpha_y():
    pass


def test_alpha_z():
    pass


# update attendance testing#

def test_update_attendance_x():
    pass


def test_update_attendance_y():
    pass


def test_update_attendance_z():
    pass
