"""QZ03: Class Writing Practice - ChristmasTreeFarm."""
from __future__ import annotations

class ChristmasTreeFarm:
    """"A Christmas Tree Farm!"""
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        """Sets up the Christmas Tree Farm."""
        self.plots = []
        i: int = 0
        while i < initial_planting:
            self.plots.append(1)
            i += 1
        while i < plots:
            self.plots.append(0)
            i += 1
    
    def plant(self, plot_index: int) -> None:
        """Plants a new tree of size 1 at the indicated plot_index."""
        self.plots[plot_index] = 1
    
    def growth(self) -> None:
        """Grows the trees by 1."""
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] != 0:
                self.plots[i] += 1
            i += 1
    
    def harvest(self, replant: bool) -> int:
        """Harvests trees that are >= size 5."""
        total: int = 0
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] >= 5:
                total += 1
                if replant:
                    self.plots[i] = 1
                else:
                    self.plots[i] = 0
            i += 1
        return total
    
    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Overloading Operator to sum up the size of the ChristmasTreeFarm objects."""
        trees: int = 0
        for plot in self.plots:
            if plot > 0:
                trees += 1
        for plot in rhs.plots:
            if plot > 0:
                trees += 1
        plot_size = len(self.plots) + len(rhs.plots)
        return ChristmasTreeFarm(plot_size, trees)    