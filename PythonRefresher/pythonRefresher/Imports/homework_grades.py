"""
- modules get used all the time throughout programming
- it  helps with creating more files with unique purposes
- keeps code clean/maintainable
"""

import pythonRefresher.Imports.grade_average_service as grade_service
# import pythonRefresher.Imports.grade_average_service

homework_assignment_grades = {'homework_1': 85, 'homework_2': 100, 'homework_3': 81}

grade_service.calculate_homework(homework_assignment_grades)
