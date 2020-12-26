# Unique value  in a list
ask = 'Y'
lst = []
while ask == 'Y':
    value = int(input('Please type a value: '))
    if value not in lst:
        lst.append(value)
        print('Value added with success!')
        ask = input('Do you want to continue? [Y/N] ').upper()
    else:
        print('This value is already on the list!')
        ask = input('Do you want to continue? [Y/N] ').upper()
print('=-' * 50)
print(f'You have typed the following values {sorted(lst)}')