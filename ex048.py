# Sum of all odd numbers multiple of 3 between 1 and 500
s = 0
for number in range(1, 501):
    if (number % 2 != 0) and (number % 3 == 0):
        s = s + number
print("The sum of odd number multiple of 3 is {}!".format(s))

