# Over 18 Group
import datetime

now = datetime.datetime.now().year
count1 = 0
count2 = 0

for k in range(1, 8):
    n = int(input("Person No {}. Please type your birth year: ".format(k)))
    if now - n >= 18:
        count1 += 1

    elif now - n < 18:
        count2 += 1

print("So, we have {} over 18!".format(count1))
print("And we have {} under 18!".format(count2))
