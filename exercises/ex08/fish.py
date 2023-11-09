"""File to define Fish class"""

__author__ = '730630815'


class Fish:
    
    age: int

    def __init__(self) -> None:
        self.age: int = 0
    
    def one_day(self) -> None:
        self.age += 1