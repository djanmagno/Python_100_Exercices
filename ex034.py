# Multiple raise on salary

salary = abs(float(input("Please type your salary in order to know the raise you will receive: ")))

if salary > 1250:
    print(f"Your salary now is R$ {salary}. Your salary will increase 10%. So your new salary will be R$ {salary * 1.1}.")
else:
    print(f"Your salary now is R$ {salary}. Your salary will increase 15%. So your new salary will be R$ {salary * 1.15}.")