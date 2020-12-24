# Registration and analyzing data from de group
age_count = gender_count = girl_count = 0

while True:
    print('-' * 30)
    print(' ' * 5 + 'Register a Person' + ' ' * 5)
    print('-' * 30)

    age = abs(int(input('Age: ')))
    if age >= 18:
        age_count += 1

    gender = input('Gender: [M/F] ').upper()
    if gender == 'M':
        gender_count += 1
    elif gender == 'F' and age < 20:
        girl_count += 1

    while gender not in 'MF':
        gender = input('Gender: [M/F] ').upper()
        if gender == 'M':
            gender_count += 1
        elif gender == 'F' and age < 20:
            girl_count += 1
    else:
        print('-' * 30)
        ask = input('Do you want to continue? [Y/N] ').upper()

    while ask not in 'YN':
        ask = input('Do you want to continue? [Y/N] ').upper()
    if ask == 'N':
        print('-' * 30)
        break
print('=' * 20 + ' PROGRAM FINISHED ' + '=' * 20 )

print(f'The number of people with more than 18 years old is {age_count}.')
print(f'The number of men on the registration is {gender_count}.')
print(f'We have {girl_count} woman with less than 20 years old.')
