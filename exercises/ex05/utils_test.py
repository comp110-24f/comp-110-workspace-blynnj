"""test the utility lists"""

__author__: str = "730749523"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_with_mixed_numbers() -> None:
    """Test that only_evens returns even numbers from a mixed list."""
    result: list[int] = only_evens([1, 2, 3, 4, 5, 6])
    assert result == [2, 4, 6]


def test_only_evens_with_all_odds() -> None:
    """Test that only_evens returns an empty list when there are no even numbers."""
    result: list[int] = only_evens([1, 3, 5, 7])
    assert result == []


def test_only_evens_does_not_mutate_input() -> None:
    """Test that only_evens does not modify the original list."""
    original: list[int] = [1, 2, 3]
    only_evens(original)
    assert original == [1, 2, 3]  # make sure the original list is not changed


def test_sub_with_valid_indices() -> None:
    """Test that sub returns the right subset from a valid range."""
    result: list[int] = sub([10, 20, 30, 40, 50], 1, 4)
    assert result == [20, 30, 40]  # end index is exclusive


def test_sub_with_empty_list() -> None:
    """Test that sub returns an empty list when given an empty list."""
    result: list[int] = sub([], 0, 1)
    assert result == []  # Empty input should return empty output


def test_sub_does_not_mutate_input() -> None:
    """Test that sub does not modify the original list."""
    original: list[int] = [1, 2, 3, 4, 5]
    sub(original, 1, 3)
    assert original == [1, 2, 3, 4, 5]  # make sure the original list is not changed


def test_add_at_index_success() -> None:
    """Test that add_at_index correctly adds an element at the specified index."""
    lst: list[int] = [1, 2, 3]
    add_at_index(lst, 4, 1)
    assert lst == [1, 4, 2, 3]  # Check the list after insertion


def test_add_at_index_raises_indexerror() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    lst: list[int] = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(lst, 4, 5)  # Invalid index


def test_add_at_index_inserts_at_zero_index() -> None:
    """Test that add_at_index can add an element at index 0."""
    lst: list[int] = [2, 3, 4]
    add_at_index(lst, 1, 0)
    assert lst == [1, 2, 3, 4]  # Ensure element is added at the start
