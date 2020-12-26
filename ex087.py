# Analyzing the data of the matrix

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

sum_even = sum_third = bigger = 0


for a in range(0, 3):
    for b in range(0, 3):
        value = int(input(f'Please type the number for the position {[a,b]}: '))
        matrix[a][b] = value
print('=-=' * 30)
for n in range(0, 3):
    if n == 1 or n == 2:
        print('')
    for m in range(0, 3):
        print(f'{[matrix[n][m]]} ', end='')
        if matrix[n][m] % 2 == 0:
            sum_even += matrix[n][m]

        if m == 2:
            sum_third += matrix[n][m]

        elif m == 1:
            if matrix[n][m] > bigger:
                bigger = matrix[n][m]

print('')
print("=-=" * 30)
print(f'The sum of even numbers on the matrix is {sum_even}.')
print(f'The sum of the numbers on the third column is {sum_third}.')
print(f'The biggets number on the second column is {bigger}.')

