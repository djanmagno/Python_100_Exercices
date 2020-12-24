# Arithmetic progression version 2

print("Arithmetic Progression Calculator")
print("-="*20)

first = abs(int(input("First term: ")))
common_difference = abs(int(input("Reason of the AP: ")))
term = first
count = 1

while count <= 10:

    print("{}".format(term), end=" -> ")
    term += common_difference
    count += 1

print("Pause")



