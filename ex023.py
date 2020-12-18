# Splitting number digits
import math

number = int(input("Please choose a number between 0 and 9999: "))
print("Analyzing the number {}".format(number))
print("Ten-thousands unit: {}".format(math.floor((number%10000)/1000)))
print("Thousands unit: {}".format(math.floor((number % 1000) / 100)))
print("Tenths unit: {}".format(math.floor((number % 100) / 10)))
print("Unit: {}".format(number % 10))
