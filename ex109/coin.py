# Functions to use on exercise 107

def increase(price=0, interest=0):
    res = price * (1 + interest/100)
    return res


def decrease(price=0, interest=0):
    res = price * (1 - interest/100)
    return res


def double(price):
    res = price * 2
    return res


def half(price):
    res = price / 2
    return res


def coin(price = 0, coin = 'R$'):
    return f'{coin} {price:>.2f}'.replace('.', ',')