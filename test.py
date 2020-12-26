group = [{'name': 'djan', 'goals': [1, 2], 'score': 3}, {'name': 'vivi', 'goals': [1, 1, 1], 'score': 3},
         {'name': 'be', 'goals': [1, 2, 4, 0], 'score': 7}, {'name': 'ka', 'goals': [1, 2, 3, 3, 0], 'score': 9},]

print('Code', end=' ')
print('Name', end='          ')
print('Goals', end='          ')
print('Total', end='')
print()
print('-' * 50)

for a, b in enumerate(group):
    print(a, end='    ')
    print(f'{b["name"]:<5}', end='         ')
    print(f'{b["goals"]}', end='          ')
    print(f'{b["score"]:>2}', end='')
    print()


