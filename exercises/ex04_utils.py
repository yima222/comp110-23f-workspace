"""Ex04- Building list functions to practice computational thinking."""
__author__ = "730668363"


def all(int_list: list[int], input: int) -> bool:
    """Searches through a list of integers to determine if all the integers is the same as the input."""
    check_idx: int = 0
    if len(int_list) == 0:
        return False
    while (check_idx < len(int_list)):
        if input != int_list[check_idx]:
            return False
        elif input == int_list[check_idx]:
            # Nested while loop to allow program to check all the numbers in the list
            while check_idx < len(int_list):
                if input != int_list[check_idx]:
                    return False
                elif input == int_list[check_idx]:
                    check_idx += 1
            return True
        

def max(int_list: list[int]) -> int:
    """Searches through a list of integers to find the largest integer."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    elif len(int_list) > 0:
        max_idx: int = 0
        # max_int allows program to update the number
        # if the current number in the list is greater than
        # the one before it
        max_int: int = int(int_list[0])
        while max_idx < len(int_list):
            present_int: int = int(int_list[max_idx])
            if present_int > max_int:
                max_int = present_int
            max_idx += 1
        return max_int


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Searches through two lists to determine if all the elements are the same in both lists."""
    list_idx: int = 0
    if len(list1) != len(list2):
        return False
    while (list_idx < len(list1)) and (list_idx < len(list2)):
        if list1[list_idx] != list2[list_idx]:
            return False
        elif list1[list_idx] == list2[list_idx]:
            list_idx += 1
    return True

