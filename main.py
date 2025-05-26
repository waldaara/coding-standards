"""This module defines a Student class for handling student data and grades."""

class Student:
    """A class to represent a student with grades and status."""

    def __init__(self, student_id, name):
        """Initialize a student with ID, name, empty grades, and default flags."""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        """Add a numeric grade to the student's record."""
        if isinstance(grade, (int, float)):
            self.grades.append(grade)
        else:
            print(f"Ignored invalid grade: {grade}")

    def calc_average(self):
        """Calculate and return the average grade."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def check_honor(self):
        """Determine if the student qualifies for honors."""
        average = self.calc_average()
        if average > 90:
            self.honor = True
        return self.honor

    def delete_grade(self, index):
        """Safely delete a grade by index."""
        try:
            del self.grades[index]
        except IndexError:
            print(f"Invalid index: {index}. Cannot delete grade.")

    def report(self):
        """Print a formatted report of the student's status."""
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average Grade: {self.calc_average():.2f}")
        print(f"Honor Roll: {'Yes' if self.honor else 'No'}")

def main():
    """Test function to demonstrate Student class usage."""
    student_a = Student("001", "Alice")
    student_a.add_grade(100)
    student_a.add_grade("Fifty")  # Will be ignored
    student_a.calc_average()
    student_a.check_honor()
    student_a.delete_grade(5)  # Invalid index
    student_a.report()

if __name__ == "__main__":
    main()
