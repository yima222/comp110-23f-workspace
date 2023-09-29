"""Ex02 - One Shot Wordle- step closer to wordle."""
__author__ = "730668363"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_pattern: str = ""

# Correct length
while len(str(guess)) != len(str(secret_word)):           
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

# Letter check & box hints
# Delete statement if the IF is the same as WHILE
check_idx: int = 0
while check_idx < len(secret_word):
    alt_idx: int = 0 
    present: bool = False
    # while six letter guess contains letters in the secret word add yellow or green boxes where appropriate, if not, add a white box
    while alt_idx < len(secret_word):
        if guess[check_idx] == secret_word[alt_idx]:
            present = True
        alt_idx = alt_idx + 1
    if guess[check_idx] == secret_word[check_idx]:  
        secret_pattern = secret_pattern + GREEN_BOX  
    elif present == True:
        secret_pattern = secret_pattern + YELLOW_BOX  
    else:
        secret_pattern = secret_pattern + WHITE_BOX
    check_idx = check_idx + 1  
    
print(secret_pattern)
if guess != secret_word:
    print("Not quite. Play again soon!")
elif guess == secret_word:
    print("Woo! You got it!")