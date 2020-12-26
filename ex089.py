# Students grade with composed lists
classroom = list()
student = []
grade = []

while True:
    name = input('Name: ')
    grade1 = float(input('Grade 1: '))
    grade2 = float(input('Grade 2: '))
    student.append(name)
    grade.append(grade1)
    grade.append(grade2)
    student.append(grade[:])
    classroom.append(student[:])
    grade.clear()
    student.clear()
    ask = input('Do you want to continue? ').upper()
    while ask not in 'YN':
        ask = input('Do you want to continue? ').upper()
    if ask == 'N':
        break
print('=-=' * 30)
space = ' ' * 10
print('No', end=' ')
print('NAME', end=space)
print('AVERAGE')
print('-' * 25, end=' ')

for n in range(0, len(classroom)):
    print('')
    print(f'{n}', end=' ')
    print(f'{classroom[n][0]:<5}', end=' ')
    print(f'{sum(classroom[n][1])/len(classroom[n][1]):>40.1f}', end=' ')

print('')
while True:
    print('-' * 30)
    ask_2 = int(input('Which of the student do you want to check the grades? '))
    if ask_2 != 999:
        print(f'The grades for {classroom[ask_2][0]} are: {classroom[ask_2][1]}')
    else:
        print('FINISHING...')
        break
print('<<< THANK YOU FOR YOUR TIME >>>')


