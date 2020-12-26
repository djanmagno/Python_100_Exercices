# Ordered list without repetition
lst = []
cor = {"limpa": '\033[m',
       "amarelo": '\033[33m',
       "vermelho": '\033[31m', }

for n in range(0, 5):
    value = int(input('Type a value: '))
    if n == 0 or value >= lst[-1]:
        lst.append(value)
        print(f'The number {cor["vermelho"]}{value}{cor["limpa"]} were added on the position '
              f'{cor["vermelho"]}{lst.index(value) + 1}{cor["limpa"]}.')
    else:
        position = 0
        while position < len(lst):
            if value <= lst[position]:
                lst.insert(position, value)
                print(f'The number {cor["vermelho"]}{value}{cor["limpa"]} were added on the position '
                      f'{cor["vermelho"]}{position + 1}{cor["limpa"]}.')
                break
            position += 1
print('-=' * 30)
print(f'The numbers typed in order are {cor["amarelo"]}{lst}{cor["limpa"]}.')