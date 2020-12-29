# Counting Function

#(1, 11, 1)
def asc_counter(a, b, c):
    print('=-' * 31)
    print(f'Counting from {a} to {b} {c} by {c}')
    for i in range(a, (b + 1), c):
        print(i, end=' ')
    print('END!')
    print('=-' * 31)


def des_counter(a, b, c):
    counting = b
    print(f'Counting from {b} to {a} {c} by {c}')
    for j in range(a, (b + c), c):
        print(counting, end=' ')
        counting -= c
    print('END!')
    print('=-' * 31)


asc_counter(1, 10, 1)
des_counter(0, 10, 2)

print('Now it is your turn to personalize the counting!')
start = int(input('Start: '))
end = int(input('End: '))
interval = abs(int(input('Interval: ')))
print('=-' * 31)

if interval != 0:
    if start < end:
        asc_counter(start, end, interval)
    elif start > end:
        des_counter(end, start, interval)
else:
    interval = 1
    if start < end:
        asc_counter(start, end, interval)
    elif start > end:
        des_counter(end, start, interval)