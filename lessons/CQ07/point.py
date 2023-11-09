"""Docstring."""

from __future__ import annotations


__author__ = "730630815"


class Point:
    """Gives an x and y coordinate to a point."""
    x: float = 0
    y: float = 0

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Assigns initial values for x and y."""
        self.x: float = x_init
        self.y: float = y_init

    def __str__(self) -> str:   
        return "x: %s; y: %s" % (self.x, self.y)
    
    def __mul__(self, factor: int | float) -> None:
        self.x = self.x * factor
        self.y = self.y * factor

    def __add__(self, factor: int | float):
        self.x += factor
        self.y += factor

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
