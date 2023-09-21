"""Structured Wordle with defining and calling functions."""
__author__ = "730668363"

def contains_char(search_for_char: str, char_check: str) -> str:
    assert len(char_check) == 1
    """Looks for the input of char in the declared word."""
    search_for_char_idx: int = 0
    if char_check == (search_for_char[search_for_char_idx]):
        return True
    else:
        return False
    search_for_char_idx = search_for_char_idx + 1