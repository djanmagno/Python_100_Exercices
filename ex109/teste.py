# Exercices modules

from ex108 import coin

value = float(input('Please type a value: R$ '))
print(f'The half of the value {coin.coin(value)} is {coin.coin(coin.half(value))}.')
print(f'The double of the value {coin.coin(value)} is {coin.coin(coin.half(value))}.')
print(f'Increasing in 10% the value {coin.coin(value)} we have {coin.coin(coin.increase(value, 10))}.')
print(f'Decreasing in 13% the value {coin.coin(value)} we have {coin.coin(coin.decrease(value, 13))}.')
