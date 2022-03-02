import random


class RollDice:

    def get_random(self):
        return random.randint(1, 6)


class CliHandler:

    def start(self):
        print('Press 1 to roll the dice.\nPress 2 if you want to quit this game.')
        while True:
            try:
                user_input = int(input('Roll/Quit:'))
            except ValueError:
                print('Invalid input! Try again.')
                continue
            roll_dice = RollDice()
            if user_input == 1:
                print(f'You got number: {roll_dice.get_random()}')
            elif user_input == 2:
                print('Game Ended')
                break
            else:
                print('Invalid input!\t Use only "1" or "2"!\tTry again.')


if __name__ == "__main__":
    CliHandler().start()


