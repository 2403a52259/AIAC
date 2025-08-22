class Student:
    """Represents a student with name, roll number, and percentage marks."""
    def __init__(self, name: str, roll_number: str, marks: float) -> None:
        self.name: str = name
        self.roll_number: str = roll_number
        self.marks: float = float(marks)
    def _compute_grade(self) -> str:
        """Return the grade string based on percentage marks.
        Classification:
        - A+: 90–100
        - A:  75–89
        - B:  60–74
        - C:  50–59
        - F:  below 50
        """
        if 90 <= self.marks <= 100:
            return "A+"
        if 75 <= self.marks <= 89:
            return "A"
        if 60 <= self.marks <= 74:
            return "B"
        if 50 <= self.marks <= 59:
            return "C"
        return "F"

    def display_details(self) -> None:
        """Print the student's details and computed grade."""
        grade = self._compute_grade()
        print(f"Name       : {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks (%)  : {self.marks}")
        print(f"Grade      : {grade}")


if __name__ == "__main__":
    # Example usage (you can adjust the values or extend as needed)
    student = Student(name="vvr", roll_number="259", marks=89)
    student.display_details()
