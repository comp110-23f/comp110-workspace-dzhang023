"""File to define River class."""

__author__ = '730630815'

from exercises.ex08.bear import Bear
# re add from exercises.ex08 import
from exercises.ex08.fish import Fish


class River:
    """River class."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Removes old animals."""
        new_fish_list: list[Fish] = []
        new_bear_list: list[Bear] = []
        for animal in self.fish:
            if animal.age <= 3:
                new_fish_list.append(animal)
        for animal in self.bears:
            if animal.age <= 5:
                new_bear_list.append(animal)
        self.fish = new_fish_list
        self.bears = new_bear_list

    def bears_eating(self) -> None:
        """Simulates fish consumption by bears."""
        for indiv_bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                indiv_bear.eat(3)

    def check_hunger(self) -> None:
        """Removes starving bears."""
        new_bear_list: list[Bear] = []
        for indiv_bear in self.bears:
            if indiv_bear.hunger_score >= 0:
                new_bear_list.append(indiv_bear)
        self.bears = new_bear_list

    def repopulate_fish(self) -> None:
        """Repopulates fish."""
        new_fish_amount: int = (len(self.fish) // 2) * 4
        for x in range(new_fish_amount):
            self.fish.append(Fish())

    def repopulate_bears(self) -> None:
        """Repopulates bears."""
        new_bear_amount: int = len(self.bears) // 2
        for x in range(new_bear_amount):
            self.bears.append(Bear())

    def remove_fish(self, amount: int) -> None:
        """Removes the fish at the front of the fish list."""
        for x in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)

    def view_river(self) -> None:
        """Prints the information for any given day."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulates one week."""
        for x in range(7):
            self.one_river_day()
