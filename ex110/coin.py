# Functions to use on exercise 107

def coin(price=0, coin='R$'):
    return f'{coin} {price:>.2f}'.replace('.', ',')


def increase(price=0, interest=0, form=True):
    if form:
        res = price * (1 + interest/100)
        return coin(res)
    else:
        res = price * (1 + interest/100)
        return round(res, 2)


def decrease(price=0, interest=0, form = True):
    if form:
        res = price * (1 - interest/100)
        return coin(res)
    else:
        res = price * (1 - interest/100)
        return round(res, 2)


def double(price, form= True):
    if form:
        res = price * 2
        return coin(res)
    else:
        res = price * 2
        return res


def half(price, form = True):
    if form:
        res = price / 2
        return coin(res)
    else:
        res = price / 2
        return res

