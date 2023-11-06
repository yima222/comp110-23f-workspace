def shrink(nums: list[str]) -> list[int]:
    shrunk_list: list[int] = list()
    for number in nums:
        if (number % 2 == 0) and (number < 7):
            shrunk_list.append(number)
    return shrunk_list

print(shrink([4, 5, 6, 8]))

def test_key_error() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {'blue': 'sky', 'purple': 'sky'}
        invert(my_dictionary)