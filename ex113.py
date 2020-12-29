# Validanting a input

def readint(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('\033[0;31mERROR!Please type a number!\033[m')
        if ok:
            break
    return value


n = readint('Please type a number: ')
print(f'You have typed the number {n}.')

