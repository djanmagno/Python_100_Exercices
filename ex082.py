# Splitting a list in even and odd numbers

lst = []
even_lst = []
odd_lst = []

while True:
    value = int(input('Please type a number: '))
    ask = input('Do you want to continue? [Y/N] ').upper()
    lst.append(value)
    while ask not in 'YN':
        print('Please Y for Yes or N for No!')
        ask = input('Do you want to continue? [Y/N] ').upper()
    if ask == 'N':
        break
print('=-='* 30)
print(f'The complete list is {lst}.')
for n in lst:
    if n % 2 == 0:
        even_lst.append(n)

    else:
        odd_lst.append(n)
print(f'The even list is {even_lst}.')
print(f'The odd list is {odd_lst}.')
print('=-=' * 30)