"""File to define Fish class."""


class Fish:
    """Class to represent fishes in the river."""
    age: int

    def __init__(self, age: int = 0):
        """Constructor for Fish class."""
        self.age = age
        return None
    
    def one_day(self):
        """Increase Fish age by 1 in one day."""
        self.age += 1
        return None