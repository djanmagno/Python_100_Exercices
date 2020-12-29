# Function to Raffle and sum numbers

from random import randint
from time import sleep

lst = list()


def raffle():
    print('Raffling 5 values of the list: ', end=' ')
    for c in range(0, 5):
        n = randint(0, 10)
        lst.append(n)
        print(n, end=' ', flush=True)
        sleep(0.4)
    print('END!')


def soma(lista):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'Summing the even numbers of the list {lista}, we have {soma} as sum of the even numbers.')


raffle()
soma(lst)
