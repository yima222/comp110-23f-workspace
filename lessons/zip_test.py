"""Test my zip function."""
__author__ = "730668363"

from lessons.zip import zip


def test_empty_lists() -> None:
    """zip([], []) should return {}."""
    assert zip([], []) == {}


def test_zip_one_key_and_value() -> None:
    """zip(["Happy"], [1]) = {'Happy': 1}."""
    test_list1: list[str] = "Happy"
    test_list2: list[int] = 1
    assert zip([test_list1], [test_list2]) == {'Happy': 1}


def test_multiple_key_and_values() -> None:
    """zip(["Happy", "Tuesday"], [1, 2]) = {'Happy': 1, 'Tuesday': 2}."""
    test_list1: list[str] = "Happy", "Tuesday"
    test_list2: list[int] = 1, 2
    zip([test_list1], [test_list2]) == {'Happy': 1, 'Tuesday': 2}