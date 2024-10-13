"""Making a wordle game!"""

__author__: str = "730749523"


def input_guess(secret_word_len: int) -> str:
    guess = input(f"Enter a {secret_word_len} charcter word: ")
    while len(guess) != secret_word_len:  # loops until the guess if the right length
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Check if a character in the word guessed is in the secret word"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """retrun emojis that correspond with the accuracy of the guess"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_string: str = ""
    index: int = 0

    while index < len(guess):
        if guess[index] == secret[index]:
            emoji_string += GREEN_BOX  # letter in the word and right spot
        elif contains_char(secret, guess[index]):
            emoji_string += YELLOW_BOX  # letter is in the word, but not that spot
        else:
            emoji_string += WHITE_BOX  # letter is not in the word

        index += 1

    return emoji_string


def main(secret: str) -> None:
    """The entrypint of the program and maion game loop."""
    turns: int = 0
    max_turns: int = 6
    won: bool = False

    while turns < max_turns and not won:
        turns += 1
        print(f"=== Turn {turns}/{max_turns} ===")
        guess: str = input_guess(secret_word_len=len(secret))
        emoji_result: str = emojified(guess, secret)
        print(emoji_result)

        if guess == secret:
            won = True

    if won:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
