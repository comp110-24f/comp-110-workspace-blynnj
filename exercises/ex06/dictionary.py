"""Dictionary utility functions"""

__author__: str = "730749523"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    inverted_dict: dict[str, str] = {}  # empty dictionary for the inverted pairs

    for key in dict1:
        value = dict1[key]
        if (
            value in inverted_dict
        ):  # see if the value is a key in the inverted dictionary
            raise KeyError("Duplicate value found for key")
        inverted_dict[value] = key

    return inverted_dict


def favorite_colors(dict2: dict[str, str]) -> str:
    color_count: dict[str, str] = (
        {}
    )  # dictionary to count the number of the same colors

    for name in dict2:
        color = dict2[name]
        if color in color_count:
            color_count[
                color
            ] += "1"  # if color is alredy in the dictionary, icrease it by 1
        else:
            color_count[color] = "1"

    most_popular_color: str = ""
    max_count: str = "0"

    for name in dict2:
        color = dict2[name]
        if (
            dict2[color] > max_count
        ):  # check if the current color is more popular than the first oneS
            most_popular_color = color
            max_count = dict2[color]

    return most_popular_color


def count(list1: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = {}  # empty dictionary for built-up result

    for item in list1:
        if item in count_dict:  # see if the item is alredy in the dictionary
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict


def alphabetizer(list2: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}

    for word in list2:
        first_letter = word[0].lower()  # turn the first letter into lowercase

        if first_letter in result:
            result[first_letter].append(word)
        else:
            result[first_letter] = [word]  # make new list for the word

    return result


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    if day in attendance_log:
        attendance_log[day].append(student)  # add the student to the attendance list
    else:
        attendance_log[day] = [student]
