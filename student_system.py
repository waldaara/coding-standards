"""Student management system for handling student records, grades, and performance."""

class Student:
    """A class to represent a student with ID, name, grades, and performance data."""

    def __init__(self, student_id: str, name: str):
        """
        Initialize a student with ID and name.
        Raises ValueError if either field is empty.
        """
        if not student_id.strip():
            raise ValueError("Student ID cannot be empty.")
        if not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False
        self.letter_grade = "N/A"

    def add_grade(self, grade):
        """
        Add a validated grade (0–100) to the student's record.
        Ignores invalid inputs with a warning.
        """
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"Invalid grade '{grade}': Must be a number between 0 and 100.")

    def calc_average(self):
        """Calculate and return the average grade; returns 0.0 if no grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self):
        """
        Determine and store the letter grade based on average.
        Also updates pass/fail status.
        """
        average = self.calc_average()
        if average >= 90:
            self.letter_grade = "A"
        elif average >= 80:
            self.letter_grade = "B"
        elif average >= 70:
            self.letter_grade = "C"
        elif average >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

        self.is_passed = average >= 60
        return self.letter_grade

    def report(self):
        """Print a summary report for the student."""
        average = self.calc_average()
        self.determine_letter_grade()
        print("\n📄 Student Report")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {self.letter_grade}")
        print(f"Status: {'Passed' if self.is_passed else 'Failed'}")

def main():
    """Demonstrate the functionality with sample data."""
    try:
        student_a = Student("123", "Alice")
        student_a.add_grade(95)
        student_a.add_grade(88.5)
        student_a.add_grade(-10)     # Invalid
        student_a.add_grade("A+")    # Invalid
        student_a.add_grade(101)     # Invalid
        student_a.determine_letter_grade()
        student_a.report()
    except ValueError as err:
        print(f"Error creating student: {err}")

if __name__ == "__main__":
    main()
