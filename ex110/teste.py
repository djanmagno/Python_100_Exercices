# Exercices modules

from ex109 import coin

value = float(input('Please type a value: R$ '))
print(f'The half of the value {coin.coin(value)} is {coin.half(value, False)}.')
print(f'The double of the value {coin.coin(value)} is {coin.double(value)}.')
print(f'Increasing in 10% the value {coin.coin(value)} we have {coin.increase(value, 10)}.')
print(f'Decreasing in 13% the value {coin.coin(value)} we have {coin.decrease(value, 13, False)}.')
