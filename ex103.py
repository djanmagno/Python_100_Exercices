# File of a soccer player

print('-' * 30)
name = input('Player name: ')
goals = input('Scored Goals:')


def file(n='<Unknown>', g=''):
    if n != '' and g != '':
        print(f'The player {n} has scored {g} goals on the championship.')
    if n == '' and g != '':
        n = '<Unknown>'
        print(f'The player {n} has scored {g} goals on the championship.')
    if n != '' and g == '':
        g = 0
        print(f'The player {n} has scored {g} goals on the championship.')
    if n == '' and g == '':
        n = '<Unknown>'
        g = 0
        print(f'The player {n} has scored {g} goals on the championship.')


file(name, goals)
