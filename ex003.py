# Adding two values
number_1 = int(input("Please type your first number: "))
number_2 = int(input("Please type your second number: "))

s = lambda x, y: x + y

result = s(number_1, number_2)

print("This adding operation of %s and %s has a result %s" % (number_1, number_2, result))
