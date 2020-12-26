# Python Dictionaries

student = dict()

student['name'] = input('Name: ')
student['average'] = int(input('Average: '))

print(f'The student name is {student["name"]}.')
print(f'The grade average of the student {student["name"]} is {student["average"]}.')
if student["average"] >= 7:
    print(f'The student {student["name"]} was approved on the exams.')
else:
    print(f'The student {student["name"]} was reproved on the exams.')
