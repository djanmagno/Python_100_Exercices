# Number in Full
cor = {"limpa": '\033[m',
       "amarelo": '\033[33m',
       "vermelho": '\033[31m', }

full = ("Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
        "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty")
while True:
    number = int(input("Please type a number between 0 and 20: "))

    if number in range(0, 21):
        print("You have typed the number {}{}{}.".format(cor["amarelo"], full[number], cor["limpa"]))
        break
    else:
        pass