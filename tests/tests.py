import unittest
from src.course import Course


class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course = Course("Python Programming", max_students=2)

    def test_initial_state(self):
        self.assertEqual(self.course.name, "Python Programming")
        self.assertEqual(self.course.max_students, 2)
        self.assertEqual(self.course.students, [])
        self.assertEqual(self.course.count(), 0)

    def test_enroll_student(self):
        self.course.enroll("Alice")
        self.assertIn("Alice", self.course.students)
        self.assertEqual(self.course.count(), 1)

    def test_enroll_multiple_students(self):
        self.course.enroll("Alice")
        self.course.enroll("Bob")
        self.assertEqual(self.course.count(), 2)
        self.assertListEqual(self.course.students, ["Alice", "Bob"])

    def test_enroll_over_capacity(self):
        self.course.enroll("Alice")
        self.course.enroll("Bob")

        with self.assertRaises(ValueError) as context:
            self.course.enroll("Charlie")

        self.assertEqual(str(context.exception), "No places left")
        self.assertEqual(self.course.count(), 2)

    def test_drop_existing_student(self):
        self.course.enroll("Alice")
        self.course.enroll("Bob")

        self.course.drop("Alice")
        self.assertNotIn("Alice", self.course.students)
        self.assertIn("Bob", self.course.students)
        self.assertEqual(self.course.count(), 1)

    def test_drop_nonexistent_student(self):
        self.course.enroll("Alice")

        with self.assertRaises(ValueError) as context:
            self.course.drop("Bob")

        self.assertIn("Bob", str(context.exception))
        self.assertEqual(self.course.count(), 1)

    def test_drop_and_re_enroll(self):
        self.course.enroll("Alice")
        self.course.enroll("Bob")

        self.course.drop("Alice")

        self.course.enroll("Charlie")
        self.assertListEqual(self.course.students, ["Bob", "Charlie"])

    def test_is_valid_name(self):
        self.assertTrue(Course.is_valid_name("Alice"))
        self.assertTrue(Course.is_valid_name("Bob"))
        self.assertTrue(Course.is_valid_name("Alice Smith"))

        self.assertFalse(Course.is_valid_name(""))
        self.assertFalse(Course.is_valid_name("   "))
        self.assertFalse(Course.is_valid_name("\t\n"))

        self.assertFalse(Course.is_valid_name(None))
        self.assertFalse(Course.is_valid_name(123))

    def test_count_method(self):
        self.assertEqual(self.course.count(), 0)

        self.course.enroll("Alice")
        self.assertEqual(self.course.count(), 1)

        self.course.enroll("Bob")
        self.assertEqual(self.course.count(), 2)

        self.course.drop("Alice")
        self.assertEqual(self.course.count(), 1)

    def test_enroll_after_drop(self):
        self.course.enroll("Alice")
        self.course.enroll("Bob")

        with self.assertRaises(ValueError):
            self.course.enroll("Charlie")

            self.course.drop("Alice")

            self.course.enroll("Charlie")
            self.assertEqual(self.course.count(), 2)
            self.assertListEqual(self.course.students, ["Bob", "Charlie"])

    def test_edge_cases_names(self):
        self.course.enroll("Alice Smith")
        self.course.enroll("Bob Johnson")

        self.assertIn("Alice Smith", self.course.students)
        self.course.drop("Alice Smith")
        self.assertNotIn("Alice Smith", self.course.students)

    def test_multiple_instances(self):
        course1 = Course("Python", max_students=1)
        course2 = Course("Java", max_students=3)

        course1.enroll("Alice")
        with self.assertRaises(ValueError):
            course1.enroll("Bob")

        course2.enroll("Bob")
        course2.enroll("Charlie")
        course2.enroll("David")

        self.assertEqual(course1.count(), 1)
        self.assertEqual(course2.count(), 3)

class TestDecoratorEdgeCases(unittest.TestCase):
    def test_decorator_on_empty_course(self):
        course = Course("Math", max_students=0)

        with self.assertRaises(ValueError) as context:
            course.enroll("Alice")

        self.assertEqual(str(context.exception), "No places left")

    def test_decorator_with_negative_capacity(self):
        course = Course("Math", max_students=-1)

        with self.assertRaises(ValueError):
            course.enroll("Alice")
            course.enroll("Bob")
            self.assertEqual(course.count(), 2)

    def test_decorator_preserves_original_method(self):
        course = Course("Test", max_students=1)
        course.enroll("Alice")
        self.assertEqual(course.students, ["Alice"])

if __name__ == "main":
    unittest.main(verbosity=2)