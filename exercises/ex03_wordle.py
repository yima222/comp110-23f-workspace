"""Ex03- Structured Wordle with defining and calling functions."""
__author__ = "730668363"


def contains_char(search_for_char: str, char_check: str) -> bool:
    """Looks for the input of char in the declared word."""
    # Length of the input must be one character
    assert len(char_check) == 1
    char_present: bool = False
    idx: int = 0
    while (char_present is False) and (idx < len(search_for_char)):
        # Tell them True if the guessed character is in the word 
        # (this doesn't indicate the index at which the guessed char is in the word)
        if char_check == (search_for_char[idx]):
            char_present is True
            return True
        else:
            idx = idx + 1
    return False


def emojified(secret_word: str, guess: str) -> str:
    """Checks for the characters of the secret word in the guess inputted."""
    # Length of the guess must be the same as the secret word
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    secret_pattern: str = ""
    check_idx: int = 0
    while check_idx < len(secret_word):
        alt_idx: int = 0 
    # while six letter guess contains letters in the secret word add yellow or green boxes where appropriate, if not, add a white box
        if guess[check_idx] == secret_word[check_idx]:
            secret_pattern = secret_pattern + GREEN_BOX 
            alt_idx = alt_idx + 1 
        # Enter the argugments for contain_char in order to call the function correctly
        elif contains_char(guess, (secret_word[check_idx])) is True:
            secret_pattern = secret_pattern + YELLOW_BOX  
        else:
            secret_pattern = secret_pattern + WHITE_BOX
        check_idx = check_idx + 1  
    return secret_pattern


def input_guess(guess_exp_len: int) -> str:
    """Prompts user for a correct length of guess for the secret word."""
    guess: str = input(f"Enter a {guess_exp_len} character word: ")
    while len(guess) != guess_exp_len:    
        guess = input(f"That wasn't {guess_exp_len} chars! Try again: ")
    # The correct length guess is returned after exiting the above while loop
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Code for the wordle game
    secret_word: str = "codes"
    guess: str = ""
    num_turn: int = 1
    max_turns: int = 6
    while num_turn <= max_turns and guess != secret_word:
        print(f"=== Turn {num_turn}/{max_turns} ===")
        guess = str(input_guess(len(secret_word)))
        print(emojified(guess, secret_word))
        num_turn = num_turn + 1
    # Once the six turns are all used, print the below results accordingly
    # This is when the code exits the while loop above
    if guess == secret_word:
        return print(f"You won in {num_turn - 1}/{max_turns} turns!")
    else:
        return print(("X/6 - Sorry, try again tomorrow!"))
   

if __name__ == "__main__":
    main()