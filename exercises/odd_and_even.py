"""QZ02 Writing Function Practice: odd_and_even."""
__author__ = "730668363"

def odd_and_even(num: list[int]) -> list[int]:
    final_list = []
    for idx in range(0, len(num)):
        if (num[idx] % 2 != 0) and (idx % 2 == 0) :
            final_list.append(num[idx])
    return final_list