# Bigger and smaller values using if conditions

value_1 = float(input("Please type the first number: "))
value_2 = float(input("Please type the second number: "))
value_3 = float(input("Please type the third number: "))

# Verifying the smaller number

smaller = value_1
if (value_2 < value_1) and (value_2 < value_3):
    smaller = value_2
elif (value_3 < value_1) and (value_3 < value_2):
    smaller = value_3

# Verifying the bigger value

bigger = value_1
if (value_2 > value_1) and (value_2 > value_3):
    bigger = value_2
elif (value_3 > value_1) and (value_3 > value_2):
    bigger = value_3

print(f"The biggest number is {bigger} and the smallest number is {smaller}!")
