# Multiplication table version 3

while True:
    print('-' * 30)
    number = int(input('Please type a number to see its multiplication table: '))
    print('-' * 30)
    for n in range(1, 11):
        print(f'{number} x {n} = {number * n}')
    if number < 0:
        break
print('Program ended. Go back whenever you want! =D')