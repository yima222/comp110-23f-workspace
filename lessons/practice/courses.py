"""QZ03 Function Writing Practice - Courses."""
from __future__ import annotations

class Course:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        """Finds 400+ courses with the given prereq."""
        if self.level < 400:
            return False
        else:
            for prereqs in self.prerequisites:
                if prereqs == prereq:
                    return True
            return False

def find_courses(courses: list[Course], prereq: str) -> list[str]:
    """Finds a list of 400+ courses whose prerequisites list contains the input_prerequisites."""
    results: list[str] = []
    for classes in courses:
        if classes.level >= 400:
            for p in classes.prerequisites:
                if p == prereq:
                    results.append(classes.name)
    return results



"""Second round of practice attempting."""
class Course:
    """Models he idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        if self.level < 400:
            return False
        else:
            for p in self.prerequisites:
                if p == prereq:
                    return True
            return False


def find_courses(classes: list[Course], prereq: str) -> list[str]:
    search_results: list[str] = []
    for course in classes:
        if course.level >= 400:
            for p in course.prerequisites:
                if p == prereq:
                    search_results.append(course.name)
    return search_results
