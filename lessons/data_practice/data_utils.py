"""Docstring."""

__author__ = '730630815'


def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column."""
    result: list[str] = []
    for row in table:
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Returns values by column in a dictionary instead of a list.""" 
    result: dict[str, list[str]] = {}
    for column_header in table[0]:
        result[column_header] = column_vals(table, column_header)
    return result


d: list[dict[str, str]] = [{'Day': 'Monday', 'Low': '56', 'High': '75'}, {'Day': 'Tuesday', 'Low': '53', 'High': '72'}, {'Day': 'Wednesday', 'Low': '50', 'High': '72'}]

print(columnar(d))