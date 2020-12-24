# ATM

print('=' * 50)
print(' ' * 18 + "DJAN's ATM" + ' ' * 10)
print('=' * 50)

value = abs(int(input('The amount to withdraw: R$ ')))

r50 = r20 = r10 = r1 = 0
rest = 0

while True:
    if (value % 50) == 0:
        r50 = int(value/50)
        print(f'numero de cedulas de R$ 50 é {r50}')
        break
    else:
        r50 = int(value / 50)
        print(f'numero de cedulas de R$ 50 é {r50}')
        rest = (value % 50)
    if (rest % 20) == 0:
        r20 = rest/20
        print(f'numero de cedulas de R$ 20 é {r20}')
        break
    else:
        r20 = int(rest / 20)
        rest = (rest % 20)
        print(f'numero de cedulas de R$ 20 é {r20}')
    if (rest % 10) == 0:
        r10 = int(rest / 10)
        print(f'numero de cedulas de R$ 10 é {r10}')
        break
    else:
        r10 = int(rest / 10)
        rest = (rest % 10)
        print(f'numero de cedulas de R$ 10 é {r10}')
        r1 = int(rest/1)
        print(f'numero de cedulas de R$ 1 é {r1}')
        break
print('Finish')