"""While loop over a string!"""

__author__: int = 730749523


def num_instances(phrase: str, search_char: str) -> int:
    """return number of times search_char appears in phrase"""
    count: int = 0
    index: int = 0

    while index < len(phrase):
        if phrase[index] == search_char:
            count = (
                count + 1
            )  # count increases everytime search_char is found on the phrase
        index = index + 1  # moves through all the letters

    return count
