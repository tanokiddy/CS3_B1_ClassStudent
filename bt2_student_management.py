from typing import List
from typing import Literal

COURSE_TYPE = Literal['online', 'offline', 'hybrid']

class Course:
    def __init__(self, course_id: int, course_name: str, type: COURSE_TYPE, tuition: int):
        self.course_id = course_id
        self.course_name = course_name
        self.type = type
        self.tuition = tuition
    def course_info(self) -> object:
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "type": self.type,
            "tuition": self.tuition
        }
    def __str__(self) -> str:
        return f"course_id: {self.course_id}, course_name: {self.course_name}, type: {self.type}, tuition: {self.tuition}"

class Student:
    def __init__(self, student_id: int, student_name: str, dob: str):
        self.courses = []
        self.student_id = student_id
        self.student_name = student_name
        self.dob = dob
    def register_course(self, course: Course):
        self.courses.append(course)
    def get_registered_courses(self) -> List[Course]:
        return self.courses
    def __str__(self) -> str:
        return f"student_id: {self.student_id}, student_name: {self.student_name}, dob: {self.dob}"

# Add courses to the manager
course_1 = (Course(1, "CS1", "hybrid", 100))
course_2 = (Course(2, "CS2", "online", 200))
course_3 = (Course(3, "CS3", "online", 300))
course_4 = (Course(4, "CS4", "offline", 400))
course_5 = (Course(5, "CS5", "offline", 500))
    
# Add students to the manager
student_1 = (Student(1, "John", "1991/9/14"))
student_2 = (Student(2, "John", "1992/9/14"))
student_3 = (Student(3, "John", "1993/9/14"))
student_4 = (Student(4, "John", "1994/9/14"))
student_5 = (Student(5, "John", "1995/9/14"))

# student_1 register some courses
student_1.register_course(course_1)
student_1.register_course(course_3)
student_1.register_course(course_5)

# Get student_1's all registered courses
student_1_all_courses = student_1.get_registered_courses()
print(student_1_all_courses)

# Get info some courses
course_1_info = course_1.course_info()
course_2_info = course_2.course_info()
course_3_info = course_3.course_info()
print(course_1_info, course_2_info, course_3_info)
