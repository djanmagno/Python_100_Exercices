# Extracting data from a list
lst = []
count = 0
while True:
    value = int(input('Please type a number: '))
    count += 1
    ask = input('Do you want to continue? [Y/N] ').upper()
    lst.append(value)
    while ask not in 'YN':
        print('Please Y for Yes or N for No!')
        ask = input('Do you want to continue? [Y/N] ').upper()
    if ask == 'N':
        break
print('=-' * 30)
lst_reverse = sorted(lst, reverse=True)
print(f'Were typed {count} numbers.')
print(f'The reverse order for the list is {lst_reverse}.')
try:
    index = lst_reverse.index(5)
    print(f'The number 5 is on the list on the position {index + 1}.')
except ValueError:
    print(f'The number 5 is not on the list.')
print('=-' * 30)