# Arithmetic progression version 2

print("Arithmetic Progression Calculator")
print("-="*20)

first = abs(int(input("First term: ")))
common_difference = abs(int(input("Reason of the AP: ")))
term = first
count = 1
total = 0
more = 10

while more != 0:
    total += more
    while count <= total:
        print("{}".format(term), end=" -> ")
        term += common_difference
        count += 1
    print("Pause")
    more = abs(int(input("How many more terms do you want to check: ")))
print("You have made {} operations".format(total))


