cor = {"limpa": '\033[m',
       "verde": '\033[0;42m',
       "azul": '\033[0;44m',
       "branco": '\033[7;40m',
       "vermelho": '\033[0;41m'}


def writing(txt, k, color):
    print(f'{cor[color]}-' * (len(txt) + 2 * k))
    print(f"{' ' * k}{txt}{' ' * k}")
    print(f'{cor[color]}-' * (len(txt) + 2 * k))


while True:

    writing('PyHELP - Helping System', 3, 'verde')

    ask = input('\033[mFunction or Library > \033[m').lower()

    if ask == 'end':
        break
    else:
        writing('Accessing the Manual of command', 3, 'azul')

        print(f'{cor["branco"]}')
        help(ask)
        
print(cor['vermelho'])
writing('SEE YOU SOON!', 3, 'vermelho')


