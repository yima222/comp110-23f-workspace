"""Creating a Point Class."""
from __future__ import annotations
__author__ = "730668363"


class Point:
    """Creates a class Point that produces a set of corrdinate points."""
    # attributes
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """The constructor for the class Point."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Update the existing x and y by multiplying by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """A Method that doesn't mutate the point but modifies the x and y to create a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __mul__(self, factor: int | float):
        """Multiplication overload to modify the original point by the factor."""
        self.x *= factor
        self.y *= factor
        new_point: Point = Point(self.x, self.y)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Addition overload to modify the original point by factor."""
        self.x += factor
        self.y += factor
        new_point: Point = Point(self.x, self.y)
        return new_point

    def __str__(self) -> str:
        """Prints the point values."""
        point_info: str = f"x: {self.x}; y: {self.y}"
        return point_info