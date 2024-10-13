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


def is_eqaul(a_list: list[int], b_list: list[int]) -> bool:
    """determine if lists are equal or not"""
    if len(a_list) != len(b_list):  # lists can't be equal if they are different lengths
        return False
    for i in range(len(a_list)):
        if a_list[i] != b_list[i]:
            return False  # if any items in lists are different, return false
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """mutate list1 by appending values in list2 to the end"""
    for i in list2:
        list1.append(i)  # append each item to list1
