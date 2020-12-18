# Grade calculator

grade1 = float(input("Please your first grade: "))
grade2 = float(input("Please your second grade: "))

average = (grade1 + grade2) / 2

if average < 5.0:
    print("Your average grade was {}, it is not enough to be approved.".format(average))
elif 5.0 <= average <= 6.9:
    print("Your average grade was {}, you need to do the exams again.".format(average))
else:
    print('Your average grade was {}, you are approved.'.format(average))
