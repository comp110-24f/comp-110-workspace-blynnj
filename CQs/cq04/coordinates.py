"""Formated pairs of input stings"""

__author__: str = "730749523"


def get_coords(xs: str, ys: str) -> None:
    """print formatted pairs of two input strings"""
    i = 0
    while i < len(xs):
        j = 0
        while j < len(ys):
            print((xs[i], ys[j]))  # prints in a specifed format
            j += 1
        i += 1
