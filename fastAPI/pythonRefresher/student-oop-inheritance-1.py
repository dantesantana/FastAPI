class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greetings(self):
        return f'Hello! I am {self.first_name} {self.last_name}.'


# Subclass
class CollegeStudent(Student):
    def __init__(self, first_name, last_name, major):
        # take first/last name from parent init
        super().__init__(first_name, last_name)
        self.major = major

    # parent functions can be overwritten
    def greetings(self):
        return f'{self.first_name} is a college student!'


class NonCollegeStudent(Student):
    def __init__(self, first_name, last_name, future_adult_job):
        super().__init__(first_name, last_name)
        self.future_adult_job = future_adult_job

    def grow_up(self):
        return f'When I grow up, I want to be a {self.future_adult_job}.'


student_1 = CollegeStudent('Eric', 'Roby', 'Computer Science')
student_2 = NonCollegeStudent('John', 'Miller', 'Doctor')

print(student_1.greetings(), student_1.major, student_2.greetings(), student_2.grow_up())
