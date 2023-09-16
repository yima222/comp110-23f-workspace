"""EX02- One Shot Wordle- a step closer towards Wordle!"""
__author__: "730668363"

secret_word: str = "python"
six_letter_guess: str = input("What is your 6-letter guess? ")
chances: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word_idx: int = int(str(six_letter_guess[0]))
secret_pattern: str = ()

if str(six_letter_guess) == secret_word:
    print(secret_pattern)
    print("Woo! You got it!") 
elif str(six_letter_guess) != secret_word and len(str(six_letter_guess)) == int(6):
    print("Not quite. Play again soon!")
else:
    while chances <= int(3):
        if len(str(six_letter_guess)) != int(6):
            chances += 1
        guess_again: str = input("That was not 6 letters! Try again: ")
    else: chances = int (3)
    print("Not quite. Play again soon!")

if len(str(six_letter_guess)) == int(6):
    while secret_word_idx < len(str(secret_word)):
        if int(str(six_letter_guess[0])) == secret_word_idx:
            secret_word_idx += 1
            print(f"{GREEN_BOX}{secret_pattern}")

