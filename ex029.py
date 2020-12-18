# Speed Control

speed = int(input("Please tell me the speed of your car: "))

if speed > 80:
    print("TICKETED!!! You have exceeded the limit speed of 80 Km/h.\nYou must pay a fine of R$ {:.2f}"
          .format((speed - 80)*7))
print("Have a nice day and drive safely!!!")