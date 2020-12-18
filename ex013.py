# Salary Readjustment

s = float(input("What is your salary? R$ "))
r = float(input("What is the Readjustment of your salary? "))

print("The initial salary was R$ {} and the Readjustment is of {} %.\nThe new salary of the employee is R$ {}."
      .format(s, r / 100, round(s * (1 + r / 100), 2)))