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
    
"""Second practice attempt."""
class ChristmasTreeFarm:
    """Christmas Tree Farm Class created."""
    plots: list[int]

    def __init__(self, plots: int, initial_planting: int):
        """Sets the initial_planting number of trees annd establishes the rest of the plots with no trees as 0."""
        self.plots = []
        i: int = 0
        while i < initial_planting:
            self.plots.append(1)
            i += 1
        while i < plots:
            self.plots.append(0)
            i += 1

    def plant(self, plot_index: int) -> None:
        """Plants new trees of size 1."""
        self.plots[plot_index] = 1
        # Clears the original plot by updating the value at that index in the list to 1.

    def growth(self) -> None:
        """Increases size of trees by 1."""
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] != 0:
                self.plots[i] += 1
            i+= 1

    def harvest(self, replant: bool) -> int:
        """Harvests tree of size 5 or greater, and replants depdending on the replant parameter."""
        harvest: int = 0
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] >= 5:
                harvest += 1
                if replant:
                    self.plots[i] = 1
                else:
                    self.plots[i] = 0
            i += 1
        return harvest
       
    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Size is the sum of the given ChristmasTreeFarms, and whose initial_planting is the sum of the numbe rof planted trees in both."""
        total_plots = len(self.plots) + len(rhs.plots)
        total_trees: int = 0
        for plot in self.plots:
            if plot > 0:
                total_trees += 1
        for plot in rhs.plots:
            if plot > 0:
                total_trees += 1
        return ChristmasTreeFarm(total_plots, total_trees)

