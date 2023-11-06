"""Testing the invert, count, favorite_color, alphabetizer, update_attendance functions."""
__author__ = "730668363"

from dictionary import invert, favorite_color, count, alphabetizer, update_attendance
# invert function unit tests


def test_empty_dict_invert() -> None:
    """Edge Case: Test invert function when there's no key-value in input dict, invert({}) should return {}."""
    assert invert({}) == {}


def test_one_pair() -> None:
    """Use Case: Test invert function when there is only one pair of key-value, invert({'Happy': 'Friday'}) = {'Friday': 'Happy'}."""
    my_dictionary: dict[str, str] = {'Happy': 'Friday'}
    assert invert(my_dictionary) == {'Friday': 'Happy'}


def test_multiple_pairs() -> None:
    """Use Case: Test invert function when there's more than one pair of key-value, invert({'Happy': 'Friday', 'Great': 'Saturday', 'Restful': 'Sunday'}) = {'Friday': 'Happy', 'Saturday': 'Great', 'Sunday': 'Restful'}."""
    the_dictionary: dict[str, str] = {'Happy': 'Friday', 'Great': 'Saturday', 'Restful': 'Sunday'}
    assert invert(the_dictionary) == {'Friday': 'Happy', 'Saturday': 'Great', 'Sunday': 'Restful'}


# favorite_color function unit tests
def test_empty_dict_fc() -> None:
    """Edge Case: Test favorite_color function when there's no key-value in input dict, favorite_color({}) should return {}."""
    assert favorite_color({}) == ""


def test_one_popular_color() -> None:
    """Use Case: Test favorite_color when there's just one most frequently appearing color in input dict, favorite_color({"Lenoir": "blue", "Chase": "purple", "Agora": "blue"}) = "blue"."""
    fc_dictionary1: dict[str, str] = {"Lenoir": "blue", "Chase": "purple", "Agora": "blue"}
    assert favorite_color(fc_dictionary1) == "blue"


def test_tied_popular_color() -> None:
    """Use Case: Test favorite_color when there's a tie for most popular color, favorite_color({"Lenoir": "blue", "Chase": "purple", "Agora": "blue", "Bento": "purple", "Cholanad": "red"}) = "blue"."""
    fc_dictionary2: dict[str, str] = {"Lenoir": "blue", "Chase": "purple", "Agora": "blue", "Bento": "purple", "Cholanad": "red"}
    assert favorite_color(fc_dictionary2) == "blue"


# count function unit tests
def test_empty_list_count() -> None:
    """Edge Case: Test count function when there are no items in the input list, count([]) should return {}."""
    assert count([]) == {}


def test_one_count_for_all_items() -> None:
    """Use Case: Test count function when there's only one count of every item fromm input list, count(["panda", "bear", "squirrel", "chipmunk"]) = {"panda": 1, "bear": 1, "squirrel": 1, "chipmunk": 1}."""
    animal_list1: list[str] = ["panda", "bear", "squirrel", "chipmunk"]
    assert count(animal_list1) == {"panda": 1, "bear": 1, "squirrel": 1, "chipmunk": 1} 


def test_varied_count_items() -> None:
    """Use Case: Test count function when there's varied counts of the items in the input list, count(["panda", "bear", "panda", "squirrel", "panda", "bear"]) = {"panda": 3, "bear": 2, "squirrel": 1}."""
    animal_list2: list[str] = ["panda", "bear", "panda", "squirrel", "panda", "bear"]
    assert count(animal_list2) == {"panda": 3, "bear": 2, "squirrel": 1}


# alphabetizer function unit tests
def test_empty_list_alphabetizer() -> None:
    """Edge Case: Test alphabetizer function when there are no items in the input list, alphabetizer([]) should return {}."""
    assert alphabetizer([]) == {}


def test_one_value_per_letter() -> None:
    """Use Case: Test alphabetizer function when there's only one item from input list that match the first letter in the keys of dict, alphabetizer(["skittles", "kitkat", "milkyway", "hershey"]) = {'s': ['skittles'], 'k': ['kitkat'], 'm': ['milkyway'], 'h': ['hershey']}."""
    candy_list1: list[str] = ["skittles", "kitkat", "milkyway", "hershey"]
    assert alphabetizer(candy_list1) == {'s': ['skittles'], 'k': ['kitkat'], 'm': ['milkyway'], 'h': ['hershey']}


def test_varied_values_per_letter() -> None:
    """Use Case: Test alphabetizer function when there are varied counts of items from input list that match the first letter in the keys of dict, alphabetizer(["skittles", "kitkat", "milkyway", "snickers", "krispies", "kreme"]) = {'s': ['skittles', 'snickers'], 'k': ['kitkat', 'krispies', 'kreme'], 'm': ['milkyway']}."""
    candy_list2: list[str] = ["skittles", "kitkat", "milkyway", "Snickers", "krispies", "kreme"]
    assert alphabetizer(candy_list2) == {'s': ['skittles', 'snickers'], 'k': ['kitkat', 'krispies', 'kreme'], 'm': ['milkyway']}


# update_attendance function unit tests
def test_empty_dict_ua() -> None:
    """Edge Case: Test update_attendance function when there are no strs for weekday and student in input, update_attendance(attendance_log1, "", "") should return original dict."""
    attendance_log1: dict[str, list[str]] = {"Monday": ["Lenoir", "Chase"], "Tuesday": ["Agora"]}
    update_attendance(attendance_log1, "", "")
    assert update_attendance(attendance_log1, "", "") == attendance_log1


def test_one_student_per_day() -> None:
    """Use Case: Test update_attendance when there's one student per existing weekday being added to the log, update_attendance(attendance_log2, "Monday", "Agora") == {"Monday": ["Lenoir", "Chase", "Agora"], "Tuesday": ["Agora"]}."""
    attendance_log2: dict[str, list[str]] = {"Monday": ["Lenoir", "Chase"], "Tuesday": ["Agora"]}
    update_attendance(attendance_log2, "Monday", "Agora")
    assert update_attendance(attendance_log2, "Monday", "Agora") == {"Monday": ["Lenoir", "Chase", "Agora"], "Tuesday": ["Agora"]}


def test_one_student_new_day() -> None:
    """Use Case: Test update_attendance when there's one existing student being added with a new weekday, update_attendance(attendance_log3, "Friday", "Agora") == {"Monday": ["Lenoir", "Chase"], "Tuesday": ["Agora"], "Friday": ["Agora"]}."""
    attendance_log3: dict[str, list[str]] = {"Monday": ["Lenoir", "Chase"], "Tuesday": ["Agora"]}
    update_attendance(attendance_log3, "Friday", "Agora")
    assert update_attendance(attendance_log3, "Friday", "Agora") == {"Monday": ["Lenoir", "Chase"], "Tuesday": ["Agora"], "Friday": ["Agora"]}