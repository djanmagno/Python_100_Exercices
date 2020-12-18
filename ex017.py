# Calculating the hypotenuse of a right triangle
from math import pow,sqrt

side1 = int(input("Please type the length of side 1 of the right triangle: "))
side2 = int(input("Please type the length of side 2 of the right triangle: "))

hypotenuse = int(sqrt((pow(side1, 2) + pow(side2, 2))))
print("The hypotenuse of th right triangle is {}.".format(hypotenuse))
