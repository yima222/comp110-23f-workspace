"""Combining two lists into a dictionary."""
__author__ = "730668363"

def zip(l1: list[str], l2: list[int]) -> dict[str, int]:
    """Combines an input str list 1 and an input int list 2 into a dictionary with the keys being list 1 and values being list 2."""
    final_zip = dict()
    if len(l1) == len(l2) and (len(l1) != 0) and (len(l2) != 0):
        idx: int = 0
        while (idx < len(l1)) and (idx < len(l2)):
            final_zip[(l1[idx])] = (l2[idx])
            idx += 1
        return final_zip
    else:
        return final_zip
    
