# Verifying the first letters of a text

city = input("What is your place of birth? ")

city = city.split()

city_v1 = city[0].lower().strip()

print("Does it have 'Santo' and its first name? %s" % ("santo" in city_v1))
