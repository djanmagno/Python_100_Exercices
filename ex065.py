# Bigger, Smaller and average

number = int(input('Please type a number: '))
ask = input('Do you want to continue? [S/N] ').upper()
bigger = number
smaller = number
count = 1
soma = number

while ask == 'S':

    number = int(input('Please type a number: '))
    ask = input('Do you want to continue? [S/N] ').upper()
    count += 1
    soma += number

    if number > bigger:
        bigger = number
    elif number < smaller:
        smaller = number

print('You have typed {} numbers and their average is {}.'.format(count, (soma / count)))
print('The biggest number is {} and the smallest number is {}.'.format(bigger, smaller))
