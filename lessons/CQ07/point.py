"""Creating a Point Class."""

class Point:
    # attributes
    x: float
    y: float
    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init
    # 2. Mutating Method here