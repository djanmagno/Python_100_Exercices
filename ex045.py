# Jokenpo

import time
from random import randint

cor = {"limpa": '\033[m',
       "vermelho": '\033[31m',
       "amarelo": '\033[33m',
       "verde": '\033[32m',}

dici = {"0": "STONE", "1": "PAPER", "2": "SCISSOR"}

print("Your options:\n"
      "[0] STONE\n[1] PAPER\n[2] SCISSOR")

human = input("Which is your play? ")
time.sleep(1)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")
time.sleep(1)

computer = str(randint(0, 2))

time.sleep(1)
# Case 1 - DRAW
if human == computer:
    print("-=" * 18)
    print("Human and Computer played {}!".format(dici[human]))
    print("-=" * 18)
    print("{}Draw!!!{}".format(cor["amarelo"], cor["limpa"]))
# Case - 2 Human WIN
if (human == "0" and computer == "2") or (human == "1" and computer == "0") or (human == "2" and computer == "1"):
    print("-=" * 18)
    print("Human played {}!".format(dici[human]))
    print("Computer played {}!".format(dici[computer]))
    print("-=" * 18)
    print("{}Human win!{}".format(cor["verde"], cor["limpa"]))
# Case - 3 Computer WIN
if (human == "0" and computer == "1") or (human == "1" and computer == "2") or (human == "2" and computer == "0"):
    print("-=" * 18)
    print("Human played {}!".format(dici[human]))
    print("Computer played {}!".format(dici[computer]))
    print("-=" * 18)
    print("{}Computer win!{}".format(cor["vermelho"], cor["limpa"]))
