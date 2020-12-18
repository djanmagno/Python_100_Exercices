# Analyzing a triangle version 2

l1 = float(input("Tell me the length of segment 1: "))
l2 = float(input("Tell me the length of segment 2: "))
l3 = float(input("Tell me the length of segment 3: "))

if l1 == l2 and l2 == l3:
    print("With three equal segments you have an EQUILATERAL triangle!")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Two of the segments are equal, so you have an ISOSCELES triangle!")
else:
    print("With three different segments you have an SCALENE triangle!")