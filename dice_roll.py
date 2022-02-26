import random


def roll_Dice():
    print('Press R to roll the dice.\nPress Q if you want to quit this game.')
    while True:
        roll = input().upper()
        if roll == 'R':
            print('You got number', random.randint(1, 6))
        elif roll == 'Q':
            print('Game Ended')
            break


roll_Dice()
