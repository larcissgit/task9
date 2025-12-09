from typing import List, Any


def ensure_enough_places(enroll_method):
    def wrapper(self, student_name: str):
        if self.count() >= self.max_students:
            raise ValueError("No places left")
        return enroll_method(self, student_name)
    return wrapper


class Course:
    def __init__(self, name: str, max_students: int):
        self.name = name
        self.max_students = max_students
        self.students: List[str] = []

    @ensure_enough_places
    def enroll(self, student_name: str) -> None:
        self.students.append(student_name)

    def drop(self, student_name: str) -> None:
        if student_name in self.students:
            self.students.remove(student_name)
        else:
            raise ValueError(f"Student {student_name} is not enrolled")

    def count(self) -> int:
        return len(self.students)

    @staticmethod
    def is_valid_name(name: Any) -> bool:
        return isinstance(name, str) and bool(name.strip())



