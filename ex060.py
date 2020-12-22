# Factorial of a number
number = int(input("Type a number in order to calculate its factorial: "))

result = 1

count = number

print("Calculating {}! = ".format(number), end="")

while count > 0:
    print("{}".format(count), end="")
    print(" x " if count > 1 else " = ", end="")
    result *= count
    count -= 1

print(result)

