# Determine if a number is a prime number or not

cor = {"limpa": '\033[m',
       "amarelo": '\033[33m',
       "verde": '\033[32m',
       "vermelho": '\033[31m',
       "azul": '\033[34m'}

number = int(input("Please type a number: "))

if number > 0:
    count = 0
    for k in range(1, number + 1, 1):

        if number % k == 0:
            count += 1
            print("{}{}{}".format(cor["amarelo"], k, cor["limpa"]), end=' ')

        else:
            print("{}{}{}".format(cor["vermelho"], k, cor["limpa"]), end=' ')

    print("\nThe number {} has {} divisors between 1 and {}".format(number, count, number))

    if count > 2:
        print("That is the reason why {} {}IS NOT{} a {}PRIME NUMBER{}!"
              .format(number, cor["vermelho"], cor["limpa"], cor["azul"], cor["limpa"]))
    else:
        print("That is the reason why {} {}IS{} a {}PRIME NUMBER{}!"
              .format(number, cor["verde"], cor["limpa"], cor["azul"], cor["limpa"]))

else:
    print("{}You need to type a positive number greater than 0!{}".format(cor["vermelho"], cor["limpa"]))