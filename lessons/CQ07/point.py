"""Creating a Point Class."""
from __future__ import annotations
__author__ = "730668363"


class Point:
    """Creates a class Point that produces a set of corrdinate points."""
    # attributes
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """The constructor for the class Point."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> Point:
        """A Method that doesn't mutate the point but modifies the x and y to create a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point