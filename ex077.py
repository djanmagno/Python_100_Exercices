# Vowels of words in a tupple

cor = {"limpa": '\033[m',
       "amarelo": '\033[33m',
       "vermelho": '\033[31m', }

tup = ('aprender', 'programas', 'linguagem', 'python',
       'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
       'mercado', 'programador', 'futuro')

lenght = len(tup)

for k in range(0, lenght):
    print(f'\nOn the word {cor["vermelho"]}{tup[k].upper()}{cor["limpa"]} we have the following vowels ', end='')
    for j in (tup[k]):
        if j in 'aeiou':
            print(f'{cor["amarelo"]}{j}{cor["limpa"]}', end=' ')

        else:
            pass
