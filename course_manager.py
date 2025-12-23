# Online Course Management System
# Demonstrates OOP, inheritance, decorators, sorting, filtering, and more

class Course:
    def __init__(self, course_name: str, duration: str):
        self.course_name = course_name
        self.duration = duration

    def course_info(self):
        return f"Course: {self.course_name} | Duration: {self.duration}"


class StudentCourse(Course):
    platform_name = "LearnHub"

    def __init__(self, course_name, duration, student_name, progress=0):
        super().__init__(course_name, duration)
        self.student_name = student_name
        self._progress = 0
        self.progress = progress  # use setter validation

    # Polymorphism: override
    def course_info(self):
        return (
            f"Platform: {StudentCourse.platform_name} | "
            f"Student: {self.student_name} | "
            f"Course: {self.course_name} | "
            f"Progress: {self.progress}%"
        )

    # Property with validation
    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        if 0 <= value <= 100:
            self._progress = value
        else:
            raise ValueError("Progress must be between 0 and 100")

    # Class method
    @classmethod
    def change_platform_name(cls, new_name):
        cls.platform_name = new_name

    # Static method
    @staticmethod
    def is_completed(progress):
        return progress == 100


def main():
    # Create multiple student-course objects
    students = [
        StudentCourse("Python OOP", "6 weeks", "Alice", 100),
        StudentCourse("Python OOP", "6 weeks", "Bob", 70),
        StudentCourse("Python OOP", "6 weeks", "Charlie", 40),
        StudentCourse("Python OOP", "6 weeks", "Diana", 100),
    ]

    while True:
        print("\n--- Online Course Management Menu ---")
        print("1. View all students")
        print("2. View completed students")
        print("3. Sort students by progress")
        print("4. Check student enrollment")
        print("5. Change platform name")
        print("0. Exit")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                for student in students:
                    print(student.course_info())

            case "2":
                # List comprehension
                completed_students = [
                    s for s in students if StudentCourse.is_completed(s.progress)
                ]
                if completed_students:
                    for s in completed_students:
                        print(s.course_info())
                else:
                    print("No students have completed the course.")

            case "3":
                # Sorting with lambda
                sorted_students = sorted(
                    students, key=lambda s: s.progress, reverse=True
                )
                for s in sorted_students:
                    print(s.course_info())

            case "4":
                name = input("Enter student name to check: ")
                # Membership operator
                if name in [s.student_name for s in students]:
                    print(f"{name} is enrolled in the course.")
                else:
                    print(f"{name} is NOT enrolled in the course.")

            case "5":
                new_name = input("Enter new platform name: ")
                StudentCourse.change_platform_name(new_name)
                print("Platform name updated successfully.")

            case "0":
                print("Exiting program. Goodbye!")
                break

            case _:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
3