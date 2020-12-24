# Fibonacci Sequence
print("-"*30)
print("FIBONACCI SEQUENCE")
print("-"*30)

terms = int(input("How many Fibonacci terms do you want to see? "))
count = 0
t1 = 0
t2 = 1
print("~" * 80)

while count < terms:
    next = t1 + t2
    terms -= 1
    print("{}".format(t1), end =" -> ")
    t1 = t2
    t2 = next

print("End")
print("~" * 80)