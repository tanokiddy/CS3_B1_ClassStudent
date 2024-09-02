class Student:
    def __init__(self, student_id, student_name, math_grade, literature_grade, chemistry_grade):
        self.student_id = student_id
        self.student_name = student_name
        self.math_grade = math_grade
        self.literature_grade = literature_grade
        self.chemistry_grade = chemistry_grade

    def average_grade(self):
        return (self.math_grade + self.literature_grade + self.chemistry_grade) / 3

    def __str__(self):
        return (f"Student id: {self.student_id}, Student name: {self.student_name}, Math grade: {self.math_grade}, Literature grade: {self.literature_grade}, Chemistry grade: {self.chemistry_grade}")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_students_with_avg_grade_above(self, grade):
        print(f"List students with average grade above {grade}:")
        for student in self.students:
            if student.average_grade() > grade:
                print(f"{student}, Average grade: {student.average_grade():.1f}")
        print()

    def print_students_with_chemistry_grade_below(self, grade):
        print(f"List students with chemistry grade below {grade}:")
        for student in self.students:
            if student.chemistry_grade < grade:
                print(student)


# Initialize the StudentManager
manager = StudentManager()

# Add students to the manager
manager.add_student(Student("S1", "Nguyen Van A", 7.5, 6.0, 4.5))
manager.add_student(Student("S2", "Tran Thi B", 8.0, 7.5, 6.0))
manager.add_student(Student("S3", "Le Van C", 5.5, 5.0, 4.0))
manager.add_student(Student("S4", "Hoang Thi D", 6.0, 5.5, 8.0))
manager.add_student(Student("S5", "Pham Van E", 4.0, 4.5, 3.5))

# Print students with average grade above 5
manager.print_students_with_avg_grade_above(5)

# Print students with Chemistry grade below 5
manager.print_students_with_chemistry_grade_below(5)

