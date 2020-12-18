# Leap Year
import datetime

year = int(input("Which year do you want to analyze? In order to analyze the current year please type 0: "))
now = datetime.datetime.now().year


def leap(y):
    if ((y % 4) == 0) and ((y % 100) != 0):
        print("%s IS a LEAP YEAR!" % (y))
    elif ((y % 4) == 0) and ((y % 100) == 0) and ((y % 400) == 0):
        print("%s IS a LEAP YEAR1" % (y))
    else:
        print("%s IS NOT a LEAP YEAR!" % (y))


if year == 0:
    leap(now)
else:
    leap(year)
