# Rounding any float number to an integer
from math import floor
float_number = float(input("Please type your float number: "))
print("The number %s has as integer part the number %s" % (float_number, floor(float_number)))