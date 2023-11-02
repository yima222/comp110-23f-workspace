"""Tests the Point Class created in point.py."""
from point import Point

my_point: Point = Point(2.0, 3.0)
print(my_point)

scale_by: Point = my_point.scale(3)
print(scale_by)