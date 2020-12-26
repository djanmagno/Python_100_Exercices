# Registering a Football Player version 2

player = dict()
goals = list()
strikers = list()
score = 0
ask = 'Y'

while True:

    player['name'] = input('Player Name: ')
    games = int(input(f'How many games has {player["name"]} played this season? '))
    for g in range(0, games):
        gol = int(input(f'How many goals has {player["name"]} scored on game {g + 1}? '))
        score += gol
        goals.append(gol)
    player['goals'] = goals[:]
    player['score'] = score
    score = 0
    strikers.append(player.copy())
    goals.clear()

    ask = input('Do you want to continue? [Y/N] ').upper()
    print('-=' * 50)
    while ask not in 'YN':
        print('Please type Y for yes or N for no!')
        ask = input('Do you want to continue? [Y/N] ').upper()
    if ask == 'N':
        break

print(strikers)
print('-=' * 50)

print('Code', end=' ')
print('Name', end='          ')
print('Goals', end='          ')
print('Total', end='')
print()
print('-' * 50)

for a, b in enumerate(strikers):
    print(f'{a:<4}', end=' ')
    for d in b.values():
        print(f'{str(d):<12}', end='')
    print()
print('-' * 50)

while True:
    number = int(input('From which players do you want to see the data? (Code) '))
    if number == 999:
        break
    if number >= len(strikers):
        print(f'WARNING! This number {number} does not exist!')
    else:
        print(f'-- SHOW DATA FROM PLAYER {strikers[number]["name"]}: ')
        for a in range(0, len(strikers[number]["goals"])):
            print(f'   On the game {a + 1} he scored {strikers[number]["goals"][a]} goals.')
        print('-' * 50)

print(f' << PROGRAM FINISHED >> ')
