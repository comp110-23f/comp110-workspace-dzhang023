"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730630815"


class Simpy:
    """Class for numerical ops."""
    values: list[float]

    def __init__(self, input_list: list[float]) -> None:
        """Initiation function."""
        self.values = input_list

    def __str__(self) -> str:
        """String value function."""
        return f"Simpy({self.values})"
    
    def fill(self, fill_val: float, num_val: int) -> None:
        """Fills values with given number."""
        self.values = []
        for x in range(num_val):
            self.values.append(fill_val)

    def arange(self, start_val: float, stop_val: float, step_val: float = 1.0) -> None:
        """Function to create a range of values."""
        assert step_val != 0.0
        self.values = []
        current_val: float = start_val
        if step_val > 0:
            while current_val < stop_val:
                self.values.append(current_val)
                current_val += step_val
        if step_val < 0:
            while current_val > stop_val:
                self.values.append(current_val)
                current_val += step_val

    def sum(self) -> float:
        return sum(self.values)

    def __add__(self, operand: Simpy | float) -> Simpy:
        new_list: list[float] = []
        if type(operand) == float:
            for value in self.values:
                new_list.append(value + operand)
        else:
            assert len(operand.values) == len(self.values)
            for index, x in enumerate(operand.values):
                new_list.append(x + self.values[index])
        return Simpy(new_list)
    
    def __pow__(self, operand: Simpy | float) -> Simpy:
        new_list: list[float] = []
        if type(operand) == float:
            for value in self.values:
                new_list.append(value ** operand)
        else:
            assert len(operand.values) == len(self.values)
            for index, x in enumerate(operand.values):
                new_list.append(self.values[index] ** x)
        return Simpy(new_list)
    
    def __eq__(self, operand: Simpy | float) -> list[bool]:
        new_list: list[float] = []
        if type(operand) == float:
            for value in self.values:
                new_list.append(value == operand)
        else:
            assert len(operand.values) == len(self.values)
            for index, x in enumerate(operand.values):
                new_list.append(self.values[index] == x)
        return new_list
    
    def __gt__(self, operand: Simpy | float) -> list[bool]:
        new_list: list[float] = []
        if type(operand) == float:
            for value in self.values:
                new_list.append(value > operand)
        else:
            assert len(operand.values) == len(self.values)
            for index, x in enumerate(operand.values):
                new_list.append(self.values[index] > x)
        return new_list
    
    def __getitem__(self, operand: int | list[bool]) -> float | Simpy:
        new_list: list[float] = []
        if type(operand) == int:
            return self.values[operand]
        else:
            assert len(operand) == len(self.values)
            for index, x in enumerate(operand):
                if x:
                    new_list.append(self.values[index])
            return Simpy(new_list)