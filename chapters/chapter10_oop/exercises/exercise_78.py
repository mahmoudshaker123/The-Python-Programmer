# Exercise 78 - Simple University System
# Given the following
from __future__ import annotations


class Course:
    def __init__(self, course_name: str, course_code: str):
        self.course_name = course_name
        self.course_code = course_code
        self.professor = None
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def assign_professor(self, professor: Professor):
        self.professor = professor

    def list_students(self):
        return [student.name for student in self.students]


class Person:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class Student(Person):
    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.student_id = student_id
        self.enrolled_courses: list[Course] = []

    def enroll(self, course: Course):
        self.enrolled_courses.append(course)
        course.add_student(self)

    def list_courses(self):
        return [course.course_name for course in self.enrolled_courses]


class Professor(Person):
    def __init__(self, name: str, email: str, professor_id: str):
        super().__init__(name, email)
        self.professor_id = professor_id
        self.taught_courses: list[Course] = []

    def assign_course(self, course: Course):
        self.taught_courses.append(course)
        course.assign_professor(self)

    def list_courses(self):
        return [course.course_name for course in self.taught_courses]
