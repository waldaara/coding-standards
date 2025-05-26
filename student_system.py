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
        self.honor_roll = False
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
        Also updates pass/fail and honor roll status.
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
        self.honor_roll = average >= 90
        return self.letter_grade

    def remove_grade_by_value(self, value):
        """
        Remove the first occurrence of a grade by its value.
        If the value does not exist, prints a warning.
        """
        try:
            self.grades.remove(value)
            print(f"Grade {value} removed.")
        except ValueError:
            print(f"Grade value '{value}' not found. Cannot remove.")

    def remove_grade_by_index(self, index):
        """
        Remove a grade by its index in the list.
        If the index is invalid, prints a warning.
        """
        try:
            removed = self.grades.pop(index)
            print(f"Grade at index {index} ({removed}) removed.")
        except IndexError:
            print(f"Index {index} is out of bounds. Cannot remove grade.")

    def report(self):
        """Print a detailed report of the student's academic status."""
        average = self.calc_average()
        self.determine_letter_grade()

        print("\n📄 Student Report")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {self.letter_grade}")
        print(f"Status: {'Passed' if self.is_passed else 'Failed'}")
        print(f"Honor Roll: {'Yes' if self.honor_roll else 'No'}")

    def summary(self):
        """Generate and return a formatted summary string for the student."""
        average = self.calc_average()
        self.determine_letter_grade()

        return (
            f"📊 Summary for {self.name} (ID: {self.student_id})\n"
            f" - Grades Count: {len(self.grades)}\n"
            f" - Average Grade: {average:.2f}\n"
            f" - Letter Grade: {self.letter_grade}\n"
            f" - Pass Status: {'Passed' if self.is_passed else 'Failed'}\n"
            f" - Honor Roll: {'Yes' if self.honor_roll else 'No'}"
        )


def main():
    """Test function to demonstrate the Student system."""
    try:
        student_a = Student("001", "Alice")

        # Adding grades
        student_a.add_grade(95)
        student_a.add_grade(88)
        student_a.add_grade(76.5)
        student_a.add_grade("Ninety")  # Invalid
        student_a.add_grade(-5)        # Invalid

        # Removing grades
        student_a.remove_grade_by_index(2)
        student_a.remove_grade_by_value(88)
        student_a.remove_grade_by_value(100)  # Doesn't exist
        student_a.remove_grade_by_index(10)   # Out of bounds

        # Reports
        student_a.report()
        print("\n" + student_a.summary())

    except ValueError as err:
        print(f"Error creating student: {err}")


if __name__ == "__main__":
    main()
