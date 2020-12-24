# Using break in infinite while loop

count = soma = 0

while True:
    number = int(input('Please type a number [999 to stop]: '))
    if number == 999:
        break
    count += 1
    soma += number

print(f'The sum of {count} values is {soma}.')