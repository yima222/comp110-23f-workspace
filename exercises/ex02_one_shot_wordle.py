"""EX02- One Shot Wordle- a step closer towards Wordle!"""
__author__: "730668363"

secret_word: str = "python"
six_letter_guess: str = input("What is your 6-letter guess? ")
guess_again: str = input("Try again: ")
chances = int(4)
while chances <= int(4):
    if len(str(six_letter_guess)) != int(6):
        print(f"That was not 6 letters!{guess_again} ")
        chances += 1
