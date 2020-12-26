# Analyzing a Tupple

v1 = int(input("Please type a number: "))
v2 = int(input("Please type other number: "))
v3 = int(input("Please type one more number: "))
v4 = int(input("Please type the last number: "))
tup = (v1, v2, v3, v4)
print(f"You have typed the values: {tup}")
print(f"The number 9 has appeared {tup.count(9)} times.")
if 3 in tup:
    print(f"The number 3 has appeared on the {tup.index(3) + 1}th position.")
else:
    print(f"The number 3 does not appear on the tupple.")

print(f"The even number are", end = ' ')
for n in tup:
    if n % 2 == 0:
        print(f"{n}", end = ' ')
    else:
        pass
