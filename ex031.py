# Flight ticket Price

distance = abs(float(input("Tell me the distance to your destination em Km: ")))

if distance <= 200:
    print("You will begin a flight of {} Km.\nThe ticket price will be R$ {:.2f}.".format(distance, distance*0.5))
else:
    print("You will begin a flight of {} Km.\nThe ticket price will be R$ {:.2f}.".format(distance, distance * 0.45))