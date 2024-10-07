"""Concat two things"""

__author__: str = "730749523"


def concat(x: str, y: str) -> str:
    """concatentes two strings"""
    return x + y


# global variables
word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    # prints only when called through this file directly, not when improted
    print(concat(word1, word2))
