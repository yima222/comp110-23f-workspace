"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730668363"


class Simpy:
    """Defines a Simpy Class and its available methods for use."""
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
        self.values = [input_value] * num_of_values

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

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloading operator that adds Simpy and Simpy objects or Simpy and float together."""
        final_sum: list[float] = list()
        if type(rhs) is Simpy:
            assert len(self.values) == len(rhs.values)
            idx: int = 0
            while idx < len(self.values):
                new_value = self.values[idx] + rhs.values[idx]
                final_sum.append(new_value)
                idx += 1
        elif type(rhs) is float:
            idx: int = 0
            while idx < len(self.values):
                new_value = self.values[idx] + rhs
                final_sum.append(new_value)
                idx += 1
        sum_simpy: Simpy = Simpy([final_sum])
        return sum_simpy
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overloading operator that raises Simpy object to a power of Simpy or a float."""
        final_values: list[float] = list()
        if type(rhs) is Simpy:
            idx: int = 0
            while idx < len(self.values):
                powered_value = self.values[idx] ** rhs.values[idx]
                final_values.append(powered_value)
                idx += 1
        elif type(rhs) is float:
            idx: int = 0
            while idx < len(self.values):
                powered_value = self.values[idx] ** rhs
                final_values.append(powered_value)
                idx += 1
        powers_simpy: Simpy = Simpy([final_values])
        return powers_simpy

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloading operator to compare whether self is equal to a seocnd Simpy object or float."""
        final_evaluation: list[bool] = list()
        if type(rhs) is Simpy:
            idx: int = 0
            while idx < len(self.values):
                comparison: bool = False
                if self.values[idx] == rhs.values[idx]:
                    comparison = True
                    final_evaluation.append(comparison)
                else:
                    comparison = False
                    final_evaluation.append(comparison)
                idx += 1               
        elif type(rhs) is float:
            idx: int = 0
            comparison: bool = False
            while idx < len(self.values): 
                if self.values[idx] == rhs:
                    comparison = True
                    final_evaluation.append(comparison)
                else:
                    comparison = False
                    final_evaluation.append(comparison)
                idx += 1
        return final_evaluation  

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overloading operator to compare whether self is greater than a seocnd Simpy object or float."""
        final_comparison: list[bool] = list()
        if type(rhs) is Simpy:
            idx: int = 0
            while idx < len(self.values):
                comparison: bool = False
                if self.values[idx] > rhs.values[idx]:
                    comparison = True
                    final_comparison.append(comparison)
                else:
                    comparison = False
                    final_comparison.append(comparison)
                idx += 1               
        elif type(rhs) is float:
            idx: int = 0
            comparison: bool = False
            while idx < len(self.values): 
                if self.values[idx] > rhs:
                    comparison = True
                    final_comparison.append(comparison)
                else:
                    comparison = False
                    final_comparison.append(comparison)
                idx += 1
        return final_comparison

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Retrieves either one float value dictated by the int index or a Simpy object of values that satisfy the bool comparison."""
        if type(rhs) is int:
            retrieve_item: float = self.values[rhs]
            return retrieve_item
        elif type(rhs) is list:    
            final_get: list[float] = list()
            for idx in range(len(rhs)):
                if rhs[idx] is True:
                    final_get.append(self.values[idx])
            return final_get 