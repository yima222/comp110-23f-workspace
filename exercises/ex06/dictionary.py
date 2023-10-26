"""EX06: Practice with dictionary functions."""
__author__ = "730668363"

#def invert(dictionary: dict[str, str]) -> dict[str, str]:



#def favorite_color(color_dicts: dict[str, str]) -> str:



def count(org_list: list[str]) -> dict[str, int]:
    org_dictionary: dict()
    idx: int = 0
    current_value: str = list[idx]
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
    if student in week_day:
        presence[student] = week_day
    return presence
attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday" , "Vrinda")
update_attendance(attendance_log, "Wednesday" , "Kaleb")
print(attendance_log)