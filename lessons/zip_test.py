"""Test my zip function."""
__author__ = "730668363"

from lessons.zip import zip

def test_empty_lists() -> None:
    """zip([], []) should return {}."""
    assert zip([], []) == {}

