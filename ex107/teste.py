# Exercices modules

import coin

value = float(input('Please type a value: R$ '))
print(f'The half of the value R$ {value} is {coin.half(value)}.')
print(f'The double of the value R$ {value} is {coin.double(value)}.')
print(f'Increasing in 10% the value R$ {value}we have {coin.increase(value, 10)}.')
print(f'Decreasing in 13% the value R$ {value} we have {coin.decrease(value, 13)}.')
