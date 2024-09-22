"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730749523"


def input_word() -> str:
    """enter a five letter word"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # exit if the input is invaild
    return word


def input_letter() -> str:
    """enter a single letter"""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    """check instances where the letter is in the word"""
    print("Searching for" + letter + "in" + word)
    count: int = 0
    index: int = 0
    while index < len(word):
        if word[index] == letter:
            print(str(letter) + "found at index" + str(index))
            count += 1
        index += 1

    if count == 0:
        print("No instances of" + str(letter) + "found in" + str(word))
    elif count == 1:
        print("1 instance of" + str(letter) + "found in" + str(word))
    else:
        print(str(count) + "instances of" + str(letter) + "found in" + str(word))


def main() -> None:
    """main function for Chardle game"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
