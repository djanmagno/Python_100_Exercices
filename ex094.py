# Unifying dictionary and lists

group = list()
person = dict()

ask = 'Y'
soma = 0
while ask == 'Y':
    person['name'] = input('Name: ')
    person['gender'] = input('Gender: [M/F] ').upper()
    while person['gender'] not in 'MF':
        print('Please type M for male or F for female!')
        person['gender'] = input('Gender: [M/F] ').upper()
    person['age'] = int(input('Age: '))
    soma += person['age']
    group.append(person.copy())
    ask = input('Do you want to continue? [Y/N] ').upper()
    while ask not in 'YN':
        print('Please type Y for yes or N for no!')
        ask = input('Do you want to continue? [Y/N] ').upper()
print('-=' * 30)
print(f'  - There are {len(group)} people on the group.')
print(f'  - There average age of the group is {soma/len(group):.2f} years old.')
print(f'  - The girls on the group are: ', end='')
for k in group:
    if k['gender'] == 'F':
        print(f'{k["name"]}', end=' ')
    else:
        pass
print()
print('  - The list of people who is over the average age: ')
for n in group:
    if n['age'] >= soma/len(group):
        print(f'     Name: {n["name"]}', end='; ')
        print(f' Gender: {n["gender"]}', end='; ')
        print(f' Age: {n["age"]}', end=';')
        print()
    else:
        pass
print('<< PROGRAM FINISHED >>')
