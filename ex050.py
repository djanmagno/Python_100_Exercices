# Summing even numbers

s = 0

for i in range(1,7):
    n = int(input("Please type the {} number: ".format(i)))
    if n % 2 == 0:
        s = s + n
print("The sum of all chosen even numbers is: {}".format(s))