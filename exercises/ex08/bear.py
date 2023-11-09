"""File to define Bear class."""

__author__ = '730630815'


class Bear:
    """Bear Class."""
    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initiation Method."""
        self.age: int = 0
        self.hunger_score: int = 0

    def one_day(self) -> None:
        """Simulates behavior after one day."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Simulates eating."""
        self.hunger_score += num_fish
