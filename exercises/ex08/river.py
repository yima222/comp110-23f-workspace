"""File to define River class."""
from __future__ import annotations
__author__ = "730668363"
from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Class to represent River."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of the bears and fishes and removes them accordingly."""
        surviving_bears: list[Bear] = list()
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        fish_count: list[Fish] = list()
        for fishes in self.fish:
            if fishes.age <= 3:
                fish_count.append(fishes)
        self.fish = fish_count
        return None
    
    def remove_fish(self, amount: int):
        """Removes the number of fish equal to amount."""
        for fish in range(0, amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Removes the same numberof fish as being eaten by the bear."""
        for bears in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bears.eat(3)
        return None
    
    def check_hunger(self):
        """Checks the hunger_score of bears and removes them if < 0."""
        bears_count: list[Bear] = list()
        for bears in self.bears:
            if bears.hunger_score >= 0:
                bears_count.append(bears)
        self.bears = bears_count
        return None
        
    def repopulate_fish(self):
        """If there's a pair of fish, then add 4 fishes to the river."""
        for fishes in self.fish:
            if len(self.fish) // 2:
                idx: int = 0
                while idx < 4:
                    self.fish.append(Fish())
                    idx += 1
        return None
    
    def repopulate_bears(self):
        """If there's a pair of bears, add 2 bears to the river."""
        for bears in self.bears:
            if len(self.bears) // 2:
                self.bears.append(Bear())        
        return None
    
    def view_river(self):
        """Prints out the number of bears and fishes in the river simulation on given days."""
        num_fish: int = len(self.fish)
        num_bear: int = len(self.bears)
        day_status: str = f"~~~ Day {self.day}: ~~~"
        fish_status: str = f"Fish population: {num_fish}"
        bear_status: str = f"Bear population: {num_bear}"
        print(day_status)
        print(fish_status)
        print(bear_status)
        return None
            
    def one_river_day(self):
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

    def one_river_week(self):
        """Simulates the river populations of bears and fishes in one week."""
        day_idx: int = 0
        while day_idx < 7:
            self.one_river_day()
            day_idx += 1
        
            