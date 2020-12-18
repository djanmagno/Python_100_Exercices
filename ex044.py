# Payment Management

cor = {"limpa" : '\033[m',
       "vermelho" : '\033[31m'}

price = round(float(input("How much do you have to pay: R$ ")), 2)
print("Please choose an base to convert your integer number:"
      "\n[1] 1x in cash\n[2] 1x on credit card\n[3] 2x on credit card\n[4] 3x or more on credit card")
option = int(input("Your option: "))

if option == 1:
    print("Your buy of R$ {} will have a discount of 10% and will cost {}.".format(price, price*0.9))

elif option == 2:
    print("Your buy of R$ {} will have a discount of 5% and will cost {}.".format(price, price*0.95))

elif option == 3:
    print("Your buy of R$ {} will be splitted in 2x of R$ {}.".format(price, price/2))

elif option == 4:
    times = int(input("How many times: "))
    print("The buy will be splitted in {}x of R$ {} with interest."
          "The buy of R$ {} will cost R$ {} in the end".format(times, price*1.2 / times, price, price*1.2))
else:
    print("{}Invalid Option!!!{}".format(cor["vermelho"], cor["limpa"]))
