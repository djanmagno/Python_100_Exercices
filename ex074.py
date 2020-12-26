# Bigger and smaller value in a tupple

from random import randint
v0 = randint(1,10)
v1 = randint(1,10)
v2 = randint(1,10)
v3 = randint(1,10)
v4 = randint(1,10)
tup = (v0, v1, v2, v3, v4)
print("The values are: ", end='')
for n in tup:
    print(f"{n} ", end='')

print(f"\nThe biggets value is {max(tup)}!")
print(f"The smallest value is {min(tup)}!")