"""Ex04- Building list functions to practice computational thinking."""
__author__ = "730668363"

def all(int_list: list[int], input: int) -> bool:
    check_idx: int = 0
    int_check: bool = False
    while check_idx < len(int_list):
        while input == int_list[check_idx]:
            check_idx += 1
        return True
    if input != int_list[check_idx]:
        return False

