__author__: str = "730749523"


def find_and_remove_max(list1: list[int]) -> int:
    if len(list1) == 0:
        return -1

    max_value = list1[0]
    for num in list1:
        if num > max_value:
            max_value = num

    while max_value in list1:
        index = list1.index(max_value)
        list1.pop(index)

    return max_value
