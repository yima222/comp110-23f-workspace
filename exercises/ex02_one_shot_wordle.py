"""EX02- One Shot Wordle- a step closer towards Wordle!"""
__author__: "730668363"

secret_word: str = "python"
six_letter_guess: str = input("What is your 6-letter guess? ")
chances: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
check_idx: int = 0
secret_word_idx: int = str(secret_word[0])
secret_pattern: str = ""


if len(str(six_letter_guess)) != len(str(secret_word)):
    while chances <= int(3):
        if len(str(six_letter_guess)) != len(str(secret_word)):
            chances += 1
            guess_again: str = input("That was not 6 letters! Try again: ")
        elif chances == int (3) and str(six_letter_guess) != str(secret_word):
            print("Not quite. Play again soon!")
if len(str(six_letter_guess)) == len(str(secret_word)):
    while check_idx < len(str(secret_word)):
        if str(six_letter_guess[check_idx]) == str(secret_word[check_idx]):  
            secret_pattern = secret_pattern + GREEN_BOX      
        elif str(six_letter_guess[check_idx]) != str(secret_word[check_idx]):
            alt_idx: int = 0  
            present: bool = str(six_letter_guess[alt_idx]) != str(secret_word[check_idx]) and False                
            while present and alt_idx < len(str(secret_word)):
                if str(six_letter_guess[alt_idx]) == str(secret_word[check_idx]):
                    present = True
                elif str(six_letter_guess[alt_idx]) != str(secret_word[check_idx]):
                    alt_idx = alt_idx + 1
            secret_pattern = secret_pattern + YELLOW_BOX
        else:
            secret_pattern = secret_pattern + WHITE_BOX
        check_idx = check_idx + 1  
    print(secret_pattern)
    if str(six_letter_guess) != secret_word:
        print("Not quite. Play again soon!")
    elif str(six_letter_guess) == secret_word:
        print("Woo! You got it!")








