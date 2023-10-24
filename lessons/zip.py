"""Docstring."""


def zip(string_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Given two lists, one with key values and one with integer values, returns a dictionary pairing the two."""
    final_dict: dict[str, int] = {}
    if (len(string_list) != len(int_list)) or (len(string_list) == 0):
        return final_dict
    for index, key in enumerate(string_list):
        final_dict[key] = int_list[index]
    return final_dict
