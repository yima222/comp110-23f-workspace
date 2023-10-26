"""Combining two lists into a dictionary."""
__author__ = "730668363"

def zip(l1: list[str], l2: list[int]) -> dict[str, int]:
    final_zip = dict()
    if len(l1) != len(l2) or (l1 or l2 == ()):
        return final_zip
    elif len(l1) == len(l2):
        for idx in range(len(l2)):
            values: int = l1[idx]
            final_zip = l1[values]
        return final_zip

print(zip(["Happy", "Tuesday"], [1, 2]))
    
