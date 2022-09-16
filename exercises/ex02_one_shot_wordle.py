"""EX02 - One-shot wordle - Closer to wordle."""
__author__ = "730383494"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
letter_count: int = 0
emoji_string: str = ""
while len(guess) != len(secret_word):
    guess = input("That was not 6 letters! Try again: ")

while letter_count < len(secret_word):
    if guess[letter_count] == secret_word[letter_count]:
        emoji_string = emoji_string + GREEN_BOX
    else:
        character_found: bool = False
        indices_of_secret: int = 0
        while character_found == False and indices_of_secret < len(secret_word):
            if secret_word[indices_of_secret] == guess[letter_count]:
                character_found = True
            indices_of_secret = indices_of_secret + 1
        if character_found:
            emoji_string = emoji_string + YELLOW_BOX
        else:  
            emoji_string = emoji_string + WHITE_BOX
    letter_count = letter_count + 1
      
print(emoji_string)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")