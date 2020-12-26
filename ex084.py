# Analyzing composed lists

ask = 'Y'
lst = list()
data = list()
count = 0
bigger = smaller = 0
while True:
    count += 1
    name = input('Name: ')
    weight = int(input('Weight: '))

    ask = input('Do you want to continue? [Y/N] ').upper()
    while ask not in 'YN':
        ask = input('Do you want to continue? [Y/N] ').upper()
    if ask == 'Y':
        data.append(name)
        data.append(weight)
        lst.append(data[:])
        data.clear()

    else:
        data.append(name)
        data.append(weight)
        lst.append(data[:])
        data.clear()
        break
print('=-=' * 30)
print(lst)
print(f'In total {len(lst)} people were registered.')

bigger = 0

for e in range(0, len(lst)):

    if e == 0:
        bigger = smaller = lst[e][1]
    else:
        if lst[e][1] <= smaller:
            smaller = lst[e][1]

        if lst[e][1] >= bigger:
            bigger = lst[e][1]

print(f'The biggest weight was {bigger:.1f} Kg. For ', end='')
for b in lst:
    if b[1] == bigger:
        print(f'{b[0]}', end=' ')
print(f'\nThe smallest weight was {smaller:.1f} Kg. ', end='')
for s in lst:
    if s[1] == smaller:
        print(f'{s[0]}', end=' ')


