import random


class RollDice:
    def __init__(self, user_input):
        self._user_input = user_input

    def comp_choose(self) -> int:
        return random.randint(1, 6)

    def play_again(self) -> bool:
        return self._user_input == 1

    def quit_game(self) -> bool:
        return self._user_input == 2


class CliHandler:

    def start(self):
        print('Press 1 to roll the dice.\nPress 2 if you want to quit this game.')
        while True:
            try:
                user_input = int(input('Roll/Quit:'))
            except ValueError:
                print('Invalid input! Try again.')
                continue
            roll_dice_obj = RollDice(user_input)
            if roll_dice_obj.play_again():
                print(f'You got number: {roll_dice_obj.comp_choose()}')
            elif roll_dice_obj.quit_game():
                print('Game Ended')
                break
            else:
                print('Invalid input!\t Use only "1" or "2"!\tTry again.')


if __name__ == "__main__":
    CliHandler().start()
