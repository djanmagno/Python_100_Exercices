# Dice Game
from random import randint
import time
from operator import itemgetter

ranking = dict()
sorted_ranking = list()

ranking['player_1'] = randint(1, 6)
ranking['player_2'] = randint(1, 6)
ranking['player_3'] = randint(1, 6)
ranking['player_4'] = randint(1, 6)

list_result = sorted(ranking.values(), reverse=True)

print('Drawing Numbers')

for k, v in ranking.items():
    print(f'The {k} played {v}.')
    time.sleep(1)
print('=-=' * 30)
"""
for e in list_result:
    for f in ranking.keys():
        if ranking[f] == e:
            sorted_ranking[f] = ranking[f]
"""
sorted_ranking = sorted(ranking.items(), key=itemgetter(1), reverse=True)

print('== Players Ranking ==')

"""
n = 0
for a, b in sorted_ranking.items():
    while n != 4:
        n += 1
        print(f'{n} place: {a} with {b}')
        time.sleep(1)
        break
"""
for m, n in enumerate(sorted_ranking):
    print(f'{m} place: {n[0]} with {n[1]} points.')
    time.sleep(1)
