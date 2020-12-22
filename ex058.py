# Guessing Game version 2

from random import randint

print("Hello, I am your computer.. Let's play a game!\n"
      "I have just chosen a number between 0 and 10\n"
      "Can you find out which number is this?")

computer_number = randint(0, 10)

person_number = int(input("What is your number? "))

count = 1

while person_number != computer_number:
    count += 1
    if person_number < computer_number:
        print("A little bit more... Try one more time!")
        person_number = int(input("What is your number? "))
    elif person_number > computer_number:
        print("A little bit less... Try one more time!")
        person_number = int(input("What is your number? "))
print("Congratulations you picket the correct number!!! On this game you have needed {} attempts to guess!"
      .format(count))
