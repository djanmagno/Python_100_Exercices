# Loan approval

cor = {"limpa" : '\033[m',
       "verde" : '\033[32m'}

house_value = abs(float(input("What is the price of the house? R$ {}{}".format(cor["verde"], cor["limpa"]))))
salary = abs(float(input("What is your salary? R$ {}{}".format(cor["verde"], cor["limpa"]))))
years = abs(float(input("How many years do you want to pay the loan? {}{}".format(cor["verde"], cor["limpa"]))))

loan_payment = house_value/(years*12)

print("In order to pay a house which costs R$ {:.2f} in {:.0f} years, you need to pay monthly R$ {:.2f}."
      .format(house_value, years, loan_payment))

if (loan_payment/salary) < 0.3:
    print("You are allowed to take the loan!!!")
elif (loan_payment/salary) > 0.3:
    print("You are not allowed to take the loan!!!")