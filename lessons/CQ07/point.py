"""Docstring."""

__author__ = "730630815"

from typing import Self


class Point:
    """Gives an x and y coordinate to a point."""

    def __init__(self, x_init: float, y_init: float) -> None:
        """Assigns initial values for x and y."""
        self.x: float = x_init
        self.y: float = y_init

    def scale_by(self, factor: int) -> None:
        """Changes the x and y values of a given point and scaling factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Self:
        """Creates a new point given a scaling factor."""
        new_x: float = self.x * factor
        new_y: float = self.y * factor
        return Point(new_x, new_y)
