"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730668363"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, initialize: list[float]):
        """Initializes the values attribute."""
        self.values = initialize
    
    def __str__(self) -> str:
        """Allows the print function call to print the actual values of Simpy."""
        simpy_output: str = f"Simpy({self.values})"
        return simpy_output
    
    def fill(self, input_value: float, num_of_values: int) -> None:
        """Fills the input float value the num_of_values times into the Simpy values attribute."""
        idx: int = 0
        while idx != num_of_values:    
            self.values.append(input_value)
            idx += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Adds values to the values attribute of Simpy Class given a start and stop value and sometimes a step value."""
        assert step != 0.0
        arange_value: float = start
        while arange_value != stop:
            self.values.append(arange_value)
            arange_value += step

    def sum(self) -> float:
        """Adds up all the values in the values attribute of the Simpy Class."""
        total: float = sum(self.values)
        return total

    def __add__(self, right_hand_operand: Simpy | float) -> Simpy:
        input_rt_operand = right_hand_operand
        if right_hand_operand is Simpy:
            assert len(self) == len(right_hand_operand)
            final_sum: list[float] = list()
            for values in self:
                values += input_rt_operand.values
                final_sum.append(values)
            return final_sum
a = Simpy([1.0, 1.0, 1.0])
b = Simpy([2.0, 3.0, 4.0])
c = a + b
print(c)