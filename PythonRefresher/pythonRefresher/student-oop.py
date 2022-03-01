"""
Object Oriented Programming
"""


class Student:
    number_of_students = 0
    school = 'Online School'

    # instance variables
    # self stands for the instance variable after it passes itself in
    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        # increment student number whenever a new student is initialized!
        Student.number_of_students += 1

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a {self.major} major!'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a ' \
               f'{self.major} student going to {self.school}'

    # Class methods run on all instances of a given class which currently exist
    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls, student_str):
        first_name, last_name, major = student_str.split('.')
        # return initialized instance
        return cls(first_name, last_name, major)


# No students created yet
print(f'Number of students: {Student.number_of_students}')

student_1 = Student('Eric', 'Roby', 'Computer Science')
student_2 = Student(first_name='John', last_name='Miller', major='Math')
new_student = 'Adil.Yutzy.English'
student_3 = Student.split_students(new_student)
print(student_3.fullname_major_school())

# 2 students created!
print(f'Number of students: {Student.number_of_students}')

print(student_1.first_name, student_1.school, student_2.first_name, student_2.school)
print(student_1.fullname_with_major())
print(Student.fullname_with_major(student_2))
print(Student.fullname_major_school(student_1))

print(student_1.school, student_2.school)
Student.set_online_school('I use Google Hangouts for class!')
print(student_1.school, student_2.school)
