"""File to define Fish class."""

__author__ = '730630815'


class Fish:
    """Fish Class."""
    age: int

    def __init__(self) -> None:
        """Initiation Method"""
        self.age: int = 0

    def one_day(self) -> None:
        """Increases age by one day."""
        self.age += 1
