# Binary, Octal and Hexadecimal code convertor

number = int(input("Please type an integer number: "))
print("Please choose an base to convert your integer number:\n[1] Binary\n[2] Octal\n[3] Hexadecimal")
option = int(input("Your option: "))

if option == 1:
    print("{} converted to BINARY is equal to {}".format(number, str(bin(number))[2:]))

elif option == 2:
    print("{} converted to OCTAL is equal to {}".format(number, str(oct(number))[2:]))

elif option == 3:
    print("{} converted to HEXADECIMAL is equal to {}".format(number, str(bin(hex))[2:]))

else:
    print("Invalid Option!!!")
