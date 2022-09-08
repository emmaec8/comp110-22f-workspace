"""EX02 - One-shot wordle - Closer to wordle."""
__author__ = "730383494"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
letter_count: int = 0
letter: str = guess[letter_count]
emoji_string: str = ""
while len(guess) != len(secret_word):
    guess = input("That was not 6 letters! Try again: ")
if len(guess) == len(secret_word):
    if guess == secret_word:
        print("Woo! You got it!")
    else:
        while len(emoji_string) <= len(secret_word):
            if letter == secret_word[letter_count]:
                emoji_string = emoji_string + GREEN_BOX
                letter_count = letter_count + 1
            else:
                emoji_string = emoji_string + WHITE_BOX
                letter_count = letter_count + 1
        print("Not quite. Play again soon!")
            
print(emoji_string)

