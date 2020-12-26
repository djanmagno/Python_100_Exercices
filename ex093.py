# Registering a Football Player

player = dict()

player['name'] = input('Player Name: ')
games = int(input(f'How many games has {player["name"]} played this season? '))
goals = list()
score = 0

for n in range(0, games):
    gol = int(input(f'How many goals has {player["name"]} scoreed on game {n + 1}? '))
    score += gol
    goals.append(gol)

print('-=' * 30)

player['goals'] = goals
player['score'] = score
print(player)

print('-=' * 30)

for a, b in player.items():
    print(f'The field {a} has value {b}.')

print('-=' * 30)
print(f'The player {player["name"]} has played {games} matches this season.')
for i, j in enumerate(player["goals"]):
    print(f'  => On game {i + 1}, he scored {j} goals.')
print(f'{player["name"]} scored {player["score"]} goals in total.')