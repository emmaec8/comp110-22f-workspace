"""EX01 - Chardle - A cute step toward Wordle."""
from itertools import count


_author_ = "730383494"

character_word: str = input("Enter a 5-character word: ")
if len(character_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character + " in " + character_word)
number_of_matching_characters = 0
if character_word [0] == single_character:
    print(single_character + " found at index 0")
    number_of_matching_characters = number_of_matching_characters + 1
if character_word [1] == single_character:
    print(single_character + " found at index 1")
    number_of_matching_characters = number_of_matching_characters + 1
if character_word [2] == single_character:
    print(single_character + " found at index 2")
    number_of_matching_characters = number_of_matching_characters + 1
if character_word [3] == single_character:
    print(single_character + " found at index 3")
    number_of_matching_characters = number_of_matching_characters + 1
if character_word [4] == single_character:
    print(single_character + " found at index 4")
    number_of_matching_characters = number_of_matching_characters + 1
if number_of_matching_characters == 0:
    print("No instances")
if number_of_matching_characters == 1:
    print("1 instance of " + single_character + " found in " + character_word)
if number_of_matching_characters == 2:
    print("2 instances of " + single_character + " found in " + character_word)
if number_of_matching_characters == 3:
    print("3 instances of " + single_character + " found in " + character_word)
if number_of_matching_characters == 4:
    print("4 instances of " + single_character + " found in " + character_word)
if number_of_matching_characters == 5:
    print("5 instances of " + single_character + " found in " + character_word)
