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


def writing(txt, k):
    print(f'-' * (len(txt) + 2 * k))
    print(f"{' ' * k}{txt}{' ' * k}")
    print(f'-' * (len(txt) + 2 * k))


def summary(price, incr, decr):
    writing('VALUE SUMMARY', 14)
    print(f'Analyzed Price: ', end='  ')
    print(f'{coin(price):>24}')
    print(f'Double of the Price: ', end='  ')
    print(f'{double(price):>20}')
    print(f'Half of the Price: ', end='  ')
    print(f'{half(price):>21}')
    print(f'{incr}% of Increase: ', end='  ')
    print(f'{increase(price, incr):>24}')
    print(f'{decr}% of Increase: ', end='  ')
    print(f'{decrease(price, decr):>23}')
    print(f'-' * (len('VALUE SUMMARY') + 28))
