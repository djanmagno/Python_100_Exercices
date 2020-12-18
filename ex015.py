# Price of a rent Car

km = float(input("How many km have you drive? "))
days = float(input("How many days have you rent the car? "))

price = round(60*days + 0.15*km, 2)

print("You have to pay R$ {}".format(price))