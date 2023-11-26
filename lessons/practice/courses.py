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