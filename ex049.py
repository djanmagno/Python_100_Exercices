# Multiplication Table

n = int(input("Please choose a number: "))

print("-"*20)
for number in range(0,11):
    print("{} x {}".format(n, number))
print("-"*20)