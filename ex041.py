# Year classification for athletes
import datetime

birth_year = abs(int(input("Please type your birth year: ")))

now = datetime.datetime.now().year

age = abs(now - birth_year)

if age <= 9:
    print("You have {} years old.\nYour category is CHILDREN CATEGORY.".format(age))
elif 10 <= age <= 14:
    print("You have {} years old.\nYour category is JUNIOR CATEGORY.".format(age))
elif 15 <= age <= 19:
    print("You have {} years old.\nYour category is YOUTH CATEGORY.".format(age))
elif age == 20:
    print("You have {} years old.\nYour category is SENIOR CATEGORY.".format(age))
else:
    print(f"You have {age} years old.\nYour category is MASTER CATEGORY.")
