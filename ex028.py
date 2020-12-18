# Guessing Game

from random import randint

computer_number = randint(0, 5)
print("Computer has already chosen its number between 0 and 5.\nTry to find out this number...")
person_number = int(input("Please choose a number between 0 and 5: "))
if computer_number == person_number:
    print("Congratulation you pick the right number {}".format(computer_number))
else:
    print("Wrong answer! The computer number was %s and your number was %s. Try again!" % (computer_number, person_number))
print(computer_number)