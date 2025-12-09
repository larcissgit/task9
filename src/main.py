from src.course import Course
from src.constants import SAMPLE_CONSTANT


def main() -> None:
    try:
        c = Course("Python", max_students=2)
        c.enroll("Alice")
        c.enroll("Bob")
        c.enroll("Charlie")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
