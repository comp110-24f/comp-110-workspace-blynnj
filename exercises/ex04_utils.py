"""Utility functions for lists"""

__author__: str = "730749523"


def all(x_list: list[int], number: int) -> bool:
    """return true if all numbers match, otherwise return false"""
    for i in x_list:
        if (
            i != number
        ):  # check if numbers in the list are not equal to the input number
            return False
    return len(x_list) > 0  # return true if list completes and is not empty


def max(input: list[int]) -> int:
    """return largest number in list, result ValueError if empty"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    max_number = input[0]
    for i in input:  # iterate through every item in the list
        if i > max_number:
            max_number = i  # update max number
    return max_number


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """check if two lists are deeply equal."""

    if len(list1) == 0 and len(list2) == 0:
        return True  # bth lists are empty

    if len(list1) == 0 or len(list2) == 0:
        return False  # one list is empty, the other is not

    if len(list1) != len(list2):
        return False  # lists have different lengths

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False  # return False if any elements are different

    return True  # lists are equal


def extend(list1: list[int], list2: list[int]) -> None:
    """mutate list1 by appending values in list2 to the end"""
    for i in list2:
        list1.append(i)  # append each item to list1
