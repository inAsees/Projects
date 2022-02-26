# progrem for dice_roll
#function cretae random numbers 1 to 6
import random


def roll_Dice():
    print('Press 1 to roll the dice.\nPress 2 if you want to quit this game.')
    while True:
        try:
            roll = int(input())
            if roll == 1:
                print('You got number', random.randint(1, 6))
            elif roll == 2:
                print('Game Ended')
                break
            else:
                print('Invalid input! Try again.')
        except Exception:
            print('Invalid input! Try again.')


roll_Dice()


