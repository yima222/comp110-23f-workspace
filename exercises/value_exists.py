"""QZ02 Writing Function Practice: value_exists."""
__author__ = "730668363"

def value_exists(dict1: dict[str, int], search_value: int) -> bool:
    present: bool = False
    for value in dict1:
        if dict1[value] == search_value:
            present = True
    return present