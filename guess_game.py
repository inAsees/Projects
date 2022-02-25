import random


def guessGame(num):
    print(f'Guess a number between 1 and {num}.You have got 3 attempts to guess!!')
    user_guess = int(input('Enter the number :'))
    comp_choose = random.randint(1, num)
    attempts = 1
    while user_guess != comp_choose and attempts < 3:
        if user_guess < 1 or user_guess > num:

            try:
                user_guess = int(
                    input(f'Entered number is out of range,please guess a number between 1 and {num} again:\n'))
            except Exception:
                user_guess = int(
                    input(f'Invalid number!! Try again:\n'))
            attempts += 1
        elif user_guess < comp_choose:

            try:
                user_guess = int(input('number is SMALL , guess BIGGER number again!\nTry again:'))
            except Exception:
                user_guess = int(input(f'Invalid number!! Try again:\n'))
            attempts += 1
        else:

            try:
                user_guess = int(input('number is BIG , guess SMALLER number again!\nTry again:'))
            except Exception:
                user_guess = int(input(f'Invalid number!!\nTry again:'))
            attempts += 1
        if attempts == 1:
            print(f'Number {comp_choose} found in {attempts} attempt.')
        elif attempts == 3:
            print(
                'You are out of total attempts!! Better luck next time.\n Do you want to play again!! For YES/NO press Y/N\n')
            play_again = input().upper()
            if play_again == 'Y':
                guessGame(20)

        else:
            print(f'Number {comp_choose} found in {attempts} attempts.')


guessGame(20)
