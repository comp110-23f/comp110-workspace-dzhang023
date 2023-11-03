"""Docstring."""

__author__ = "730630815"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary of strings."""
    final_dict: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in final_dict.keys():
            raise KeyError("Sorry, there cannot be more than one usage of a single key.")
        final_dict[dictionary[key]] = key
    return final_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """Given a dictionary of people and their favorite colors, the function returns the most common favorite color."""
    multiple_faves: bool = False
    favorite: str = ''
    counter_dict: dict[str, int] = {}
    for name in dictionary:
        if dictionary[name] not in counter_dict:
            counter_dict[dictionary[name].lower()] = 0
        else:
            counter_dict[dictionary[name].lower()] += 1
    current_max = 0
    for color in counter_dict:
        if counter_dict[color] == current_max:
            multiple_faves = True
        if counter_dict[color] > current_max:
            multiple_faves = False
            favorite = color
    if not multiple_faves:
        return "multiple favorite colors"
    else:
        return favorite


def count(value_list: list[str]) -> dict[str, int]:
    """Given a list of random repeated values, returns the counts of each respective value."""
    counter_dict: dict[str, int] = {}
    for value in value_list:
        if type(value) != str:
            raise TypeError("Only strings are allowed")
        if value not in counter_dict:
            counter_dict[value] = 1
        else:
            counter_dict[value] += 1
    return counter_dict


def alphabetizer(value_list: list[str]) -> dict[str, list[str]]:
    """Given a list of values, returns a dictionary organizing the values by letter."""
    alpha_dict: dict[str, list[str]] = {}
    for value in value_list:
        first_letter = value.lower()[0]
        if first_letter not in alpha_dict:
            alpha_dict[first_letter] = [value]
        else:
            alpha_dict[first_letter].append(value)
    return alpha_dict


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Given an attendance log, adds a student's attendance to the log based on what day it is."""
    if day not in attendance_log:
        attendance_log[day] = [student]
    else:
        attendance_log[day].append(student)
    return attendance_log
