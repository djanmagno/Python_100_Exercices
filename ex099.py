# Function to find out the biggest number
import time


def bigger(*numbers):
    if len(numbers) != 0:
        print('=-' * 30)
        print('Analyzing the input values...')
        for n in numbers:
            print(n, end=' ', flush=True)
            time.sleep(0.4)

        print(f'In total {len(numbers)} numbers were informed.')
        print(f'The biggest number informed was {max(numbers)}.')
        print('=-' * 30)
    else:
        print('Analyzing the input values...')
        print('=-' * 30)
        print('Were informed in total 0 values.')
        print('The biggest value was 0.')
        print('=-' * 30)
    time.sleep(1)


bigger(2,9,4,5,7,1)
bigger(4,7,0)
bigger(1,2)
bigger(6)
bigger()