import random


class GuessGame:
    def __init__(self, upper_bound: int, max_attempts: int):
        self._upper_bound = upper_bound
        self._max_attempts = max_attempts
        self._random_number = random.randint(1, upper_bound)
        self._current_attempts = 0

    def get_upper_bound(self):
        return self._upper_bound

    def get_max_attempts(self):
        return self._max_attempts

    def get_current_attempts(self):
        return self._current_attempts

    def get_random_number(self):
        return self._random_number

    def get_attempts_left(self):
        return self._max_attempts - self._current_attempts

    def is_user_input_not_in_range(self, user_input: int) -> bool:
        return user_input < 1 or user_input > self._upper_bound

    def is_user_input_smaller(self, user_input: int) -> bool:
        return user_input < self._random_number

    def increment_attempts(self):
        self._current_attempts += 1

    def is_user_guess_equal_random(self, user_input: int) -> bool:
        return self._random_number == user_input

    def is_current_attempts_equal_max_attempts(self) -> bool:
        return self._current_attempts == self._max_attempts

    def is_last_attempt(self) -> bool:
        return self._current_attempts == self._max_attempts


class CliHandler:
    def __init__(self, upper_bound: int, max_attempts: int):
        self._game = GuessGame(upper_bound, max_attempts)

    def start(self):
        print('Guess a number between 1 and {}.You have got {} attempts to guess!!'.format(self._game.get_upper_bound(),
                                                                                           self._game.get_max_attempts()))
        while self._game.get_current_attempts() < self._game.get_max_attempts():
            try:
                user_guess = int(input('Enter the number :'))
            except ValueError:
                print('Invalid input, try again\n')
                continue
            self._game.increment_attempts()
            if self._game.is_user_guess_equal_random(user_guess):
                print('Number {} found in {} attempt.'.format(self._game.get_random_number(),
                                                              self._game.get_current_attempts()))
                break

            elif self._game.is_user_input_not_in_range(user_guess):
                print(
                    'Entered number is out of range,please guess a number between 1 and {} again.\t You have {} attempts remaining.'.format(
                        self._game.get_upper_bound(), self._game.get_attempts_left()))
            elif self._game.is_user_input_smaller(user_guess):
                if self._game.is_last_attempt():
                    print(
                        f'Wrong answer!!\tYou are out of attempts.')
                    break
                print('number is SMALL , guess BIGGER number again!\t You have {} attempts remaining.'.format(
                    self._game.get_attempts_left()))

            else:

                if self._game.is_last_attempt():
                    print(
                        f'Wrong answer!\tYou are out of attempts.')
                    break
                print('number is big , guess SMALLER number again!\t You have {} attempts remaining.'.format(
                    self._game.get_attempts_left()))


if __name__ == "__main__":
    CliHandler(20, 3).start()
