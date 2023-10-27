"""Summing the elements of a list using different loops."""
__author__ = "730668363"


def w_sum(vals: list[float]) -> float:
    """Adds values in a list using the while loop."""
    val_idx: int = 0
    sum_value: float = 0.0
    while (val_idx < len(vals)):
        sum_value += vals[val_idx]
        val_idx += 1
    return sum_value


def f_sum(vals: list[float]) -> float:
    """Adds values in a list using the for...in... loop."""
    total_sum: float = 0.0
    for numbers in vals:
        total_sum += numbers
    return total_sum


def f_range_sum(vals: list[float]) -> float:
    """Adds values in a list using the for...in range(...)."""
    sum_all: float = 0.0
    for idx in range(0, len(vals)):
        values: float = vals[idx]
        sum_all += values
    return sum_all
