"""File to define Bear class"""

class Bear:
    
    age: int
    hunger_score: int

    def __init__(self) -> None:
        self.age: int = 0
        self.hunger_score: int = 0
    
    def one_day(self) -> None:
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        self.hunger_score += num_fish