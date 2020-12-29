# Calculating area with functions

print('Measuring your land')
print('-' * 30)


def area(x, y):
    print(f'The area of a land with {x:.1f} x {y:.1f} is {(x * y):.1f} m2.')


width = float(input('WIDTH (m): '))
lenght = float(input('LENGTH (m): '))
area(width, lenght)
