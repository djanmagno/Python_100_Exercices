# IMC Calculator

weight = abs(float(input("Please tell me your weight in Kg: ")))
height = abs(float(input("Please tell me your height in m: ")))

imc = round((weight / height ** 2) * (10 ** 4), 2)

if imc < 18.5:
    print(f"Your IMC is {imc}.\nYou are UNDERWEIGHT.")
elif 18.5 <= imc <= 25:
    print(f"Your IMC is {imc}.\nYou are NORMAL.")
elif 25 < imc <= 30:
    print(f"Your IMC is {imc}.\nYou are OVERWEIGHT.")
elif 30 < imc <= 40:
    print(f"Your IMC is {imc}.\nYou are OBESE.")
elif imc > 40:
    print(f"Your IMC is {imc}.\nYou are EXTREMELY OBESE.")