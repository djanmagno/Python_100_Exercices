# Even or Odd Game
from random import randint
print('-=' * 30)
print("LET'S PLAY EVEN OR ODD GAME")
print('-=' * 30)

h_score = count = 0

while True:
    count += 1
    computer = randint(0, 99)
    human = abs(int(input('Please type a number: ')))
    ask = input('Even or Odd [E/O]: ').upper()
    result = computer + human

    if ask == 'E' and result % 2 == 0:
        print('-' * 30)
        print(f'You have played {human} and computer played {computer}. Total result was {result} it is EVEN!')
        print('-' * 30)
        h_score += 1
        print('Human won!')
        print("Let's play again...")
        print('-=' * 30)
    elif ask == 'O' and result % 2 != 0:
        print('-' * 30)
        print(f'You have played {human} and computer played {computer}. Total result was {result} it is ODD!')
        print('-' * 30)
        h_score += 1
        print('Human won!')
        print("Let's play again...")
        print('-=' * 30)
    elif ask == 'E' and result % 2 != 0:
        print('-' * 30)
        print(f'You have played {human} and computer played {computer}. Total result was {result} it is ODD!')
        print('-' * 30)
        print('You Lose!')
        print('-=' * 30)
        break
    elif ask == 'O' and result % 2 == 0:
        print('-' * 30)
        print(f'You have played {human} and computer played {computer}. Total result was {result} it is EVEN!')
        print('-' * 30)
        print('You Lose!')
        print('-=' * 30)
        break

print(f"Game Over!You have won {h_score} times!")