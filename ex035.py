# Analyzing a triangle

l1 = float(input("Tell me the length of segment 1: "))
l2 = float(input("Tell me the length of segment 2: "))
l3 = float(input("Tell me the length of segment 3: "))

condition_1 = ((abs(l2-l3) < l1) and ((l2 + l3) > l1))
condition_2 = ((abs(l1-l3) < l2) and ((l1 + l3) > l2))
condition_3 = ((abs(l1-l2) < l3) and ((l1 + l2) > l3))

if condition_1 and condition_2 and condition_3:
    print("With the segments %s, %s, %s it is POSSIBLE to create a triangle!" % (l1, l2, l3))
else:
    print("With the segments %s, %s, %s it is NOT POSSIBLE to create a triangle!" % (l1, l2, l3))