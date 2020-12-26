# Creating a matrix with lists
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for a in range(0, 3):
    for b in range(0, 3):
        value = int(input(f'Please type the number for the position {[a,b]}: '))
        matrix[a][b] = value

for n in range(0, 3):
    if n == 1 or n == 2:
        print('')
    for m in range(0, 3):
        print(f'{[matrix[n][m]]}', end='')