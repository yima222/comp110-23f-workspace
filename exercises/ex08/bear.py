"""File to define Bear class."""


class Bear:
    """Class to represent bears in the river."""
    age: int
    hunger_score: int

    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Constructor for Bear class."""
        self.age = age
        self.hunger_score = hunger_score
        return None
    
    def one_day(self):
        """Changes to the attributes in Bear in one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increases hunger_score by num_fish eaten."""
        self.hunger_score += num_fish
        return None