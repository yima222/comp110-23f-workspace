"""EX06: Practice with dictionary functions."""
__author__ = "730668363"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Given an input dictionary, invert will reverse the order of the keys and values."""
    inverted_dicts: dict[str, str] = dict()
    for string_keys in dictionary:
        string_values = dictionary[string_keys]
        if string_values in inverted_dicts:
            raise ValueError("KeyError")
        inverted_dicts[string_values] = string_keys
    return inverted_dicts


def favorite_color(dictionary: dict[str, str]) -> str:
    """Given a dict of names and colors, returns the color that appears most frequently."""
    pop_color: str = ""
    high_count: int = 0
    # Can't figure out the current_count: int = 0, so what if I declared a dictionary to keep track of the color count like in the count function.
    current_count: dict[str, int] = dict()
    for names in dictionary:
        color = dictionary[names]
        if color in current_count:
            current_count[color] += 1
        else:
            current_count[color] = 1
        if current_count[color] > high_count:
            high_count = current_count[color]
            pop_color = color
    return pop_color


def count(org_list: list[str]) -> dict[str, int]:
    """Given a list of str, returns a dict regarding the count of the keys from list."""
    org_dictionary: dict[str, int] = dict()
    current_value_count: int = 0
    for values in org_list:
        if values in org_dictionary:
            current_value_count += 1
            org_dictionary[values] = current_value_count
        else:
            current_value_count = 1
            org_dictionary[values] = current_value_count
    return org_dictionary


def alphabetizer(a_list: list[str]) -> dict[str, list[str]]:
    """Takes a list of str and sort it in a dict alphabetically."""
    ordered_dict: dict[str, list[str]] = dict()
    for word in a_list:
        idx: int = 0
        letter1 = word[0].lower()
        if letter1 in ordered_dict and (word[idx] == letter1):
            ordered_dict[letter1] += [word]
        else:
            ordered_dict[letter1] = [word]
    return ordered_dict


def update_attendance(presence: dict[str, list[str]], week_day: str, student: str) -> dict[str, list[str]]:
    """Adds students to week_day given a presence dict through mutating the dict."""
    if week_day in presence:
        presence[week_day] += [student]
    else:
        presence[week_day] = [student]
    return presence