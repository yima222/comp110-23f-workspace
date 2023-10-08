"""Ex04- Building list functions to practice computational thinking."""
__author__ = "730668363"

def all(int_list: list[int], input: int) -> bool:
    check_idx: int = 0
    while (check_idx < len(int_list)):
        if input != int_list[check_idx]:
            return False
        elif input == int_list[check_idx]:
            while check_idx < len(int_list):
                if input != int_list[check_idx]:
                    return False
                elif input == int_list[check_idx]:
                    check_idx += 1
            return True
        

def max(int_list: list[int]) -> int:
    max_idx: int = 0


def is_equal(list1: list[int], list2: list[list]) -> bool:
    list_idx: int = 0
    equal: bool = False
    while (equal is False) and (list_idx < (len(list1) and len(list2))):
        if list1[list_idx] == list2[list_idx]:
            equal is True
            list_idx += 1
        else:
            return False
    return True

print(all([1, 1, 1, 1], 1 ))