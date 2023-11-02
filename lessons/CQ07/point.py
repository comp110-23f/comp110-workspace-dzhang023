"""Docstring."""

from __future__ import annotations


__author__ = "730630815"


class Point:
    """Gives an x and y coordinate to a point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float) -> None:
        """Assigns initial values for x and y."""
        self.x: float = x_init
        self.y: float = y_init

    def scale_by(self, factor: int) -> None:
        """Changes the x and y values of a given point and scaling factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Creates a new point given a scaling factor."""
        new_x: float = self.x * factor
        new_y: float = self.y * factor
        new_point: Point = Point(new_x, new_y)
        return new_point
