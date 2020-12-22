# Bigger and Smaller weight

bigger = 0 # Bigger Weight
smaller = 0 # Smaller Weight
for k in range(1, 6):
    n = int(input("Person No {} weight: ".format(k)))
    if k == 1:
        bigger = smaller = n
    elif n > bigger:
        bigger = n
    elif n < bigger:
        smaller = n
    else:
        pass

print("The biggest weight is {} Kg".format(bigger))
print("The smallest weight is {} Kg".format(smaller))
