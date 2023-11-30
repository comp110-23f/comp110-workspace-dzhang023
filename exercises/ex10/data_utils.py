"""Dictionary related utility functions."""

__author__ = "730630815"


import csv

# Define your functions below


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Reads csv_file and formats it as a list of columns."""
    result: list[dict[str, str]] = []
    with open(path) as file_object:
        csv_file = csv.reader(file_object)
        for ind, row in enumerate(csv_file):
            if ind == 0:
                key_row: list[str] = row
            else:
                indiv_row: dict[str, str] = {}
                for index, value in enumerate(row):
                    indiv_row[key_row[index]] = value
                result.append(indiv_row)
    return result

def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Returns values in a table column."""
    result: list[str] = []
    for row in table:
        result.append(row[column])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Returns values by column in a dictionary instead of a list.""" 
    result: dict[str, list[str]] = {}
    for column_header in table[0]:
        result[column_header] = column_values(table, column_header)
    return result


def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Returns smaller table with set amount of rows."""
    result: dict[str, list[str]] = {}
    for column in table.keys():
        smaller_list: list[str] = []
        for i in range(num_rows):
            smaller_list.append(table[column][i])
        result[column] = smaller_list
    return result


def select(table: dict[str, list[str]], wanted_columns: list[str]) -> dict[str, list[str]]:
    """Returns smaller table with designated columns."""
    result: dict[str, list[str]] = {}
    for column_name in wanted_columns:
        result[column_name] = table[column_name]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables."""
    combined_tables: dict[str, list[str]] = {}
    for key in table_one:
        combined_tables[key] = table_one[key]
    for key in table_two:
        if key in combined_tables.keys():
            for value in table_two[key]:
                combined_tables[key].append(value)
        else:
            combined_tables[key] = table_two[key]
    return combined_tables


def count(key_list: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for key in key_list:
        if key in result.keys():
            result[key] += 1
        else:
            result[key] = 1
    return result