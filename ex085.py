# List with an inside even list and odd list

main_list = list()
even_list = list()
odd_list = list()

main_list.append(even_list)
main_list.append(odd_list)


for n in range(0, 7):
    value = int(input(f'Please type the {n + 1} number: '))
    if value % 2 == 0:
        main_list[0].append(value)
    else:
        main_list[1].append(value)
print('=-=' * 30)
print(f'The even list is {sorted(main_list[0])}')
print(f'The odd list is {sorted(main_list[1])}')
