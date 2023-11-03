"""Docstring."""

__author__ = "730630815"

import pytest
from dictionary import invert, favorite_color, count, alphabetizer, update_attendance


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
    with pytest.raises(TypeError):
        test_list_for_count: list[str] = [1, '3', 'd', 'd', 'e', 'a', 'b']
        print(count(test_list_for_count))
    print("Only strings can be used.")


# alphabetize testing

def test_alpha_lowers():
    test_list_for_alpha: list[str] = ['animal', 'apple', 'angry', 'always', 'bear', 'bare', 'balding', 'apartment']
    print(alphabetizer(test_list_for_alpha))
    


def test_alpha_lower_upper():
    test_list_for_alpha: list[str] = ['animal', 'Apple', 'angry', 'ALways', 'Bear', 'bare', 'BAlding', 'apartment']
    print(alphabetizer(test_list_for_alpha))


def test_alpha_z():
    with pytest.raises(TypeError):
        test_list_for_alpha: list[str] = ['1e', '2vb', '(>?)', '!!', '@3', '@ba$re', '^BAlding', '2apartment']
        print(alphabetizer(test_list_for_alpha))
    print("only letters can start words")


# update attendance testing#

def test_update_attendance_thursday():
    test_attendance_log: dict[str, list[str]] = {'Monday': ["Student A", "Student B", "Student C"], 'Tuesday': ["Student B", "Student C"], 'Wednesday': ["Student C", "Student A"]} 
    day: str = 'Thursday'
    students_in_attendance: list[str] = ["Student A", "Student B", "Student C"]
    for student in students_in_attendance:
        update_attendance(test_attendance_log, day, student)
    print(test_attendance_log)

def test_update_attendance_adding_to_wednesday():
    test_attendance_log: dict[str, list[str]] = {'Monday': ["Student A", "Student B", "Student C"], 'Tuesday': ["Student B", "Student C"], 'Wednesday': ["Student C", "Student A"]} 
    day: str = 'Wednesday'
    students_in_attendance: list[str] = ["Student D", "Student E", "Student F"]
    for student in students_in_attendance:
        update_attendance(test_attendance_log, day, student)
    print(test_attendance_log)


def test_update_attendance_testing_day_of_week():
    test_attendance_log: dict[str, list[str]] = {'Monday': ["Student A", "Student B", "Student C"], 'Tuesday': ["Student B", "Student C"], 'Wednesday': ["Student C", "Student A"]} 
    day: str = '31st'
    students_in_attendance: list[str] = ["Student D", "Student E", "Student F"]
    with pytest.raises(TypeError):
        for student in students_in_attendance:
            update_attendance(test_attendance_log, day, student)
    print("Please use the actual day of the week")

