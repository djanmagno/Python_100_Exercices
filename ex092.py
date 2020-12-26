# Worker Register with dictionary
import datetime

now = datetime.datetime.now().year

employee = dict()

employee['name'] = input('Name: ')
birth = int(input('Birth Year: '))
employee['age'] = now - birth
employee['ctps'] = int(input('Worker Register (Type 0 if you do not have it): '))
if employee['ctps'] == 0:
    print(employee)
    print('-=' * 30)
    for a, b in employee.items():
        print(f'- {a} has as value {b}')
else:
    employee['hire'] = int(input('Year of Hiring: '))
    employee['salary'] = round(float(input('Salary: R$ ')), 2)
    employee['retirement'] = employee['age'] + ((35 + employee["hire"]) - now)
    print('-=' * 30)
    print(employee)

    for a, b in employee.items():
        print(f'- {a} has as value {b}')
