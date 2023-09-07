"""EX01 - Chardle - A cute step toward wordle."""
__author__ = "730668363"

five_character_word: str = input("Enter a 5-character word: ")
if len(str(five_character_word)) != int(5):
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")
if len(str(single_character)) != int(1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + five_character_word)

instances : int = 0
if str(five_character_word[0]) == str(single_character):
    print(single_character + " found at index 0")
    instances = instances + 1
if str(five_character_word[1]) == str(single_character):
    print(single_character + " found at index 1")
    instances = instances + 1
if str(five_character_word[2]) == str(single_character):
    print(single_character + " found at index 2")
    instances = instances + 1
if str(five_character_word[3]) == str(single_character):
    print(single_character + " found at index 3")
    instances = instances + 1
if str(five_character_word[4]) == str(single_character):
    print(single_character + " found at index 4")
    instances = instances + 1
if instances == int(1):
    print(str(instances) + " instance of " + single_character + " found in " + five_character_word)
else:
    if instances == int(0):
        print("No instances of " + single_character + " found in " + five_character_word)
    else:
        print(str(instances) + " instances of " + single_character + " found in " + five_character_word)
         
