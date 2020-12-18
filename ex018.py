# Calculating the sin, cos and tan of an angle
from math import sin, cos, tan, radians

angle_degree = int(input("Please type the angle you want to calculate the sin, cos and tan: "))

angle_rad = radians(angle_degree)

print("Tha angle {} has as:\nSin = {}\nCos = {}\nTan = {}"
      .format(angle_rad, sin(angle_rad), cos(angle_rad), tan(angle_rad)))
