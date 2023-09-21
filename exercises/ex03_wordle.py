"""Structured Wordle with defining and calling functions."""
__author__ = "730668363"

def contains_char(search_for_char: str, char_check: str) -> str:
    assert len(char_check) == 1
    """Looks for the input of char in the declared word."""
    idx: int = 0
    if char_check == (search_for_char[idx]):
        return True
    else:
        return False

print(contains_char("abc", "a"))