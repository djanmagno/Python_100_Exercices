# Lottery suggestions

from random import randint
import time
print('-' * 50)
title = 'MEGA-SENA LOTTERY'
print(title.center(50))
print('-' * 50)
qnt = int(input('How many games do you want to play? '))
print(f'-=-=-=-=-=-=-=-= Raffling {qnt} Games -=-=-=-=-=-=-=-=')
game = list()

for n in range(0, qnt):

    for a in range(0, 7):
        if a % 7 == 0:
            game.clear()
        else:
            value = randint(0, 60)
            if value in game:
                value = randint(0, 60)
                game.append(value)
            else:
                game.append(value)

    print(f'Game {n + 1}: {game}')

    time.sleep(1)
luck = ' < GOOD LUCK! > '
print(luck.center(50, '*'))
