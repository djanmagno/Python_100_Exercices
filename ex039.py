# Military Service
import datetime

birth_year = int(input("Please typer your birth year: "))
now = datetime.datetime.now().year
age = now - birth_year

if age < 18:
    print("Who borned in {} is {} years old in {}.\nIt still missing {} years for the military service.\n"
          "Your military conscription will be in {}."
          .format(birth_year, age, now, 18 - age, now + 18 - age))
elif age > 18:
    print("Who borned in {} is {} years old in {}.\nYou should make your military conscription {} years ago.\n"
          "Your military conscription was in {}."
          .format(birth_year, age, now, age - 18, now - age + 18))
else:
    print("Who borned in {} is {} years old in {}.\n"
          "You must go to your military conscription IMEDIATELY."
          .format(birth_year, age, now, age - 18, now - age + 18))