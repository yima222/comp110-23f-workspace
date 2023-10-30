"""EX06: Practice with dictionary functions."""
__author__ = "730668363"

def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Given an input dictionary, ivert will reverse the order of the keys and values."""
    inverted_dicts = dict()
    for key in dictionary:
        if key == value:
            raise KeyError("KeyError")
        else:
            value = dictionary[key]
            inverted_dicts[value] = key
    return inverted_dicts
print(invert({'apple': 'cat'}))

def favorite_color(color_dicts: dict[str, str]) -> str:
    """Takes a dict input list of names and favorite colors to return a str of the frequent color."""


def count(org_list: list[str]) -> dict[str, int]:
    org_dictionary: dict()
    idx: int = 0
    current_value: str = org_list[idx]
    cv_count: int = 0
    while idx <= len(org_list):
        if current_value in org_dictionary:
            cv_count += 1
            idx += 1
        else:
            cv_count += 1
            org_dictionary[current_value] = cv_count
        return org_dictionary
    

#def alphabetizer(a_list: list[str]) -> dict[str, list[str]]:


def update_attendance(presence: dict[str, list[str]], week_day: str, student: str) -> dict[str, list[str]]:
    attendance_log: ()
    if student in week_day:
        attendance_log[week_day] = student
    return attendance_log
attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday" , "Vrinda")
update_attendance(attendance_log, "Wednesday" , "Kaleb")
