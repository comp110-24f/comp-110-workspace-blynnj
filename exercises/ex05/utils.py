""""""

__author__: str = "730749523"


def only_evens(a: list[int]) -> list[int]:
    # returns even elements in input list
    evens: list[int] = []
    for num in a:
        if num % 2 == 0:
            evens.append(num)
    return evens


def sub(b: list[int], start: int, end: int) -> list[int]:
    # returns subset between input start and end
    if start < 0:
        start = 0

    if end > len(b):
        end = len(b)

    if len(b) == 0 or start >= len(b) or end <= 0:
        return []

    subset: list[int] = []
    for item in range(start, end):
        subset.append(b[item])
    return subset


def add_at_index(c: list[int], element: int, index: int) -> None:
    # mutate input list
    if index < 0 or index > len(c):
        raise IndexError("Index is out of bounds for the input list")

    c.append(0)
    for item in range(len(c) - 1, index, -1):
        c[item] = c[item - 1]
    c[index] = element
