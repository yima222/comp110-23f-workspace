"""EX06: Practice with dictionary functions."""
__author__ = "730668363"

def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Given an input dictionary, ivert will reverse the order of the keys and values."""
    inverted_dicts = dict()
    for string_keys in dictionary:
        string_values = dictionary[string_keys]
        if string_values in inverted_dicts:
            raise ValueError("KeyError")
        inverted_dicts[string_values] = string_keys
    return inverted_dicts


def favorite_color(dictionary: dict[str, str]) -> str:
    """Given a dict of names and colors, returns the color that appears most frequently."""
    pop_color: dict()
    for names in dictionary:
        color = dictionary[names]
        if color in pop_color:
            pop_color[color] += 1
        else:
            pop_color[color] = 1
print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))

def count(org_list: list[str]) -> dict[str, int]:
    org_dictionary: dict()
    idx: int = 0
    current_value: str = org_list[idx]
    cv_count: int = 0
    while idx <= len(org_list):
        if current_value in org_list:
            org_dictionary[org_list] = current_value
            cv_count += 1
            idx += 1
        else:
            cv_count += 1
            org_dictionary[current_value] = cv_count
        return org_dictionary
#print(count(["hello", "hello", "bye"]))


#def alphabetizer(a_list: list[str]) -> dict[str, list[str]]:


def update_attendance(presence: dict[str, list[str]], week_day: str, student: str) -> dict[str, list[str]]:
    if student and week_day in presence:
        presence[week_day] = student
    return presence
    
    

attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday" , "Vrinda")
update_attendance(attendance_log, "Wednesday" , "Kaleb")
print(attendance_log)



