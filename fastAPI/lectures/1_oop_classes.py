# OOP

class Student:
    pass

    # class variables
    number_of_students = 0
    school = 'Online School'

    # initial class setup
    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

        Student.number_of_students += 1

    # class functions
    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a '\
            f'{self.major} major!'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a '\
            f'{self.major} student going to {self.school}'

    # change the school variable by using a class method
    # (changes variable for all instances)
    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls, student_str):
        first_name, last_name, major = student_str.split('.')
        return cls(first_name, last_name, major)


print(f'Student count: {Student.number_of_students}')
student_1 = Student('Eric', 'Roby', 'Computer Science')
student_2 = Student('John', 'Miller', 'Math')
print(f'Student count: {Student.number_of_students}')

print(
    student_1.first_name,
    student_1.last_name,
    student_1.major,
    student_2.first_name,
    student_2.last_name,
    student_2.major,
    student_1.fullname_with_major(),
    Student.fullname_with_major(student_2),
    student_1.school,
    student_2.fullname_major_school(),
    sep='\n'
)

print(student_1.school, student_2.school)
Student.set_online_school('Google Hangouts')
print(student_1.school, student_2.school)

student_3 = Student.split_students('Adil.Yutzy.English')
print(student_3.fullname_major_school())