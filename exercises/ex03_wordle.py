"""Actual wordle game with only 6 guesses."""
__author__ = "730383494"


def contains_char(string_any_length: str, single_character: str) -> bool:
    """Checks to see if a single character is found in a string of any length."""
    assert len(single_character) == 1
    index_count: int = 0
    while index_count < len(string_any_length):
        if string_any_length[index_count] == single_character:
            return True
        else:
            index_count = index_count + 1
    return False
 

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Uses contains_char function to test for yellow or white box."""
    assert len(guess) == len(secret)
    emoji_string: str = ""
    letter_counter: int = 0
    while letter_counter < len(guess):
        if guess[letter_counter] == secret[letter_counter]:
            emoji_string = emoji_string + GREEN_BOX
        elif contains_char(secret, guess[letter_counter]) == True:
            emoji_string = emoji_string + YELLOW_BOX
        else:
            emoji_string = emoji_string + WHITE_BOX
        letter_counter = letter_counter + 1
    return emoji_string


def input_guess(expected_length: int) -> str:
    """Checks for length of guess to be of an expected length."""
    guess: str = input("Enter a " + str(expected_length) + " " + "character word: ")
    while expected_length != len(guess):
        guess = input("That wasn't " + str(expected_length) + " " + "chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    winner: bool = False
    while turns <= 6 and not winner:
        print(f"=== Turn {turns}/6 === ")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            winner = True
        turns = turns + 1
    if winner:
        print("You won in " + str(turns - 1) + str("/6 turns"))
    else:
        print("X/6 - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()
