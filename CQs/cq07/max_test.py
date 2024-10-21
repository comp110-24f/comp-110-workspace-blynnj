__author__: str = "730749523"

from find_max import find_and_remove_max


def test_expected_value() -> None:
    result: int = find_and_remove_max([-5, -1, -3, -2])
    expected: int = -1
    assert result == expected


def test_mutate_list() -> None:
    nums: list[int] = [5, 1, 5, 2]
    find_and_remove_max(nums)
    expected: list[int] = [1, 2]
    assert nums == expected


def test_edge_case() -> None:
    nums: list[int] = [2, 3, 3, -1, 3]
    result: int = find_and_remove_max(nums)
    expected_value: int = 3
    expected_list: list[int] = [2, -1]
    assert result == expected_value
    assert nums == expected_list
