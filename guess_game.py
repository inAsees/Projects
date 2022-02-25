import random


def guessGame(upper_bound):
    print(f'Guess a number between 1 and {upper_bound}.You have got 3 attempts to guess!!')
    comp_choose = random.randint(1, upper_bound)
    attempts = 0
    while attempts < 3:
        attempts += 1
        try:
            user_guess = int(input('Enter the number :'))
        except Exception:
            print('Invalid input, try again\n')
            attempts -= 1
            continue
        if comp_choose == user_guess:
            print(f'Number {comp_choose} found in {attempts} attempt.')
            break

        elif user_guess < 1 or user_guess > upper_bound:
            print(f'Entered number is out of range,please guess a number between 1 and {upper_bound} again:')
        elif user_guess < comp_choose:
            print('number is SMALL , guess BIGGER number again!')
        else:
            print('number is BIG , guess SMALLER number again!')

    print(
        'You are out of total attempts!! Better luck next time.\nDo you want to play again!! For YES/NO press Y/N\n')
    play_again = input().upper()
    if play_again == 'Y':
        guessGame(12)


guessGame(12)
