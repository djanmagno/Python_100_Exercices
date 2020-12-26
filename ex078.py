# Bigger and Smaller value on a list
lst = []

for i in range(0, 5):
    value = input(f'Please type a value for the {i + 1} position: ')
    lst.append(value)
print('=-' * 30)
print(f'You have typed the following values {lst}')

print(f'The smallest value of the list is {min(lst)} on the position ', end='')
for k, l in enumerate(lst):
    if l == min(lst):
        print(f' {k}...', end='')


print(f'\nThe biggest value of the list is {max(lst)} on the position ', end='')
for m, n in enumerate(lst):
    if n == max(lst):
        print(f' {m}...', end='')


