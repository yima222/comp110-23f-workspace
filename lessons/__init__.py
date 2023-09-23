"""Structured Wordle with defining and calling functions."""
__author__ = "730668363"

def contains_char(search_for_char: str, char_check: str) -> str:
    """Looks for the input of char in the declared word."""
    assert len(char_check) == 1
    idx: int = 0
    while idx < len(search_for_char):
        alt_idx: int = 0
        if char_check == (search_for_char[idx]):
            return True
        idx = idx + 1
    if char_check != (search_for_char[alt_idx]):
        return False
    alt_idx = alt_idx + 1

def emojified(guess: str, secret_word: str) -> str:
    """Checks for the characters of the secret word in the guess inputted."""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    secret_pattern: str = ""
    check_idx: int = 0
    if guess[check_idx] == secret_word[check_idx]:
        secret_pattern = secret_pattern + GREEN_BOX
        check_idx = check_idx + 1
    elif contains_char is True:
        secret_pattern = secret_pattern + YELLOW_BOX 
    elif contains_char is False:
        secret_pattern = secret_pattern + WHITE_BOX
    return(secret_pattern)

print(contains_char("hello", "o"))