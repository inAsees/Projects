import random


class WordGuess:
    def __init__(self):
        self._current_attempt = 0
        self._wrong_attempt = 0
        self._random_word = random.choice(['hello'])
        self._max_attempts = len(self._random_word)
        self._guess_characters = ["" for i in range(len(self._random_word))]

    def get_random_word(self) -> str:
        return self._random_word

    def get_current_attempt(self) -> int:
        return self._current_attempt

    def get_attempts_left(self) -> int:
        return self._max_attempts - self._current_attempt

    def get_char_input_position(self, char_input):
        position = []
        for i in range(len(self._random_word)):
            if char_input == self._random_word[i]:
                self._guess_characters[i] = char_input
                position.append(i + 1)
        if len(position) == 1:
            return position[0]
        else:
            pass

    def increment_current_attempt(self) -> None:
        self._current_attempt += 1

    def increment_wrong_attempt(self) -> None:
        self._wrong_attempt += 1

    def is_word_guessed_before_max_attempts_exhausts(self) -> bool:
        return "".join(self._guess_characters) == self._random_word

    def guess_word_instead_of_letters(self) -> bool:
        return len("".join(self._guess_characters)) >= 2

    def is_char_input_repeated(self, char_input):
        return char_input in self._guess_characters and char_input in self._random_word

    def is_char_input_equals_random_word(self, word_input: str) -> bool:
        return self._random_word == word_input

    def is_char_input_present_in_random_word(self, char_input: str) -> bool:
        return char_input in self._random_word

    def is_char_input_alphabet(self, char_input: str) -> int:
        return char_input.isalpha()

    def hint_no_1(self) -> bool:
        return self._wrong_attempt == 2


class CliHandler:
    def __init__(self):
        self._word_guess = WordGuess()

    def start(self):
        print(
            f'This is the Word guess game. You have only {self._word_guess._max_attempts} guesses in total. Best of luck.')
        while self._word_guess.get_current_attempt() < self._word_guess._max_attempts:
            if self._word_guess.is_word_guessed_before_max_attempts_exhausts():
                print(
                    f'You guessed the correct word {self._word_guess.get_random_word()} in {self._word_guess.get_current_attempt()} attempt.')
                break
            if self._word_guess.guess_word_instead_of_letters():
                print(
                    'Do you want to guess the word instead of letters? '
                    'Press "1" for yes and "0" for continuing with letters instead.')
                try:
                    user_input = int(input('Enter your response:'))
                except ValueError:
                    print('Invalid input! Try again')
                    continue
                if user_input == 1:
                    word_input = input('Enter the word:').lower()
                    self._word_guess.increment_current_attempt()
                    if self._word_guess.is_char_input_equals_random_word(word_input):
                        print(f'You guessed the correct word in {self._word_guess._current_attempt} attempt.')
                        quit()
                    else:

                        print(
                            f'Wrong guess. {self._word_guess.get_attempts_left()} attempt remaining.\nTry again.')
                        self._word_guess.increment_wrong_attempt()
                        continue
                elif user_input == 0:
                    pass
                else:
                    print('Invalid input. Try again!')
                    continue

            char_input = input('Enter the letter:').lower()
            if not self._word_guess.is_char_input_alphabet(char_input):
                print('Invalid input!!\nPlease enter letter only!')
            elif self._word_guess.is_char_input_repeated(char_input):
                print(f'This letter is already entered,enter different letter again.')
                continue
            self._word_guess.increment_current_attempt()
            if self._word_guess.is_char_input_present_in_random_word(char_input):
                char_position = self._word_guess.get_char_input_position(char_input)
                print(
                    f'You guessed the correct letter.Letter position is {char_position} in the word.\t'
                    f'{self._word_guess.get_attempts_left()} attempt remaining!')

            else:
                print(
                    f'Wrong guess! {self._word_guess.get_attempts_left()} attempt remaining!\nTry again.')
                self._word_guess.increment_wrong_attempt()
            if self._word_guess.hint_no_1():
                print(f'\tHint for you. (Word has {len(self._word_guess.get_random_word())} letters.)')
        print('You failed to guess the correct word!!')

if __name__ == "__main__":
    CliHandler().start()
