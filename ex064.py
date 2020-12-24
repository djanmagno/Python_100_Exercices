# Count and Sum the numbers until we type 999 version 1

typed = int(input('Please type a number [999 in order to stop]: '))

sum = 0

count = 0

while typed != 999:
    count += 1
    sum += typed
    typed = int(input('Please type a number [999 in order to stop]: '))

print('You have typed {} numbers and their sum is {}.'.format(count, sum))
