"""Tests the Point Class created in point.py."""
from point import Point

my_point: Point = Point(2.0, 2.0)
print(my_point)

new_point: Point = my_point.scale_by(3)
print(new_point)