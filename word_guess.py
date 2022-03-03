import random


class WordGuess:
    def __init__(self, max_attempts: int):
        self._current_attempt = 0
        self._correct_attempt = 0
        self._wrong_attempt = 0
        self._max_attempts = max_attempts

    def get_random_word(self) -> str:
        return random.choice(['hang', 'dare', 'truth', 'sky', 'peace', 'hello'])

    def get_current_attempt(self) -> int:
        return self._current_attempt

    def get_correct_attempt(self) -> int:
        return self._correct_attempt

    def get_max_attempts(self) -> int:
        return self._max_attempts

    def increment_current_attempt(self) -> None:
        self._current_attempt += 1

    def increment_correct_attempt(self) -> None:
        self._correct_attempt += 1

    def increment_wrong_attempt(self) -> None:
        self._wrong_attempt += 1

    def get_attempts_left(self) -> int:
        return self._max_attempts - self._current_attempt

    def is_word_guessed_before_max_attempts_exhausts(self) -> bool:
        return self._correct_attempt == len(self.get_random_word())

    def guess_word_instead_of_letters(self) -> bool:
        return self._correct_attempt >= self._max_attempts // 2

    def is_user_guess_equals_random_word(self, word_input: str) -> bool:
        return word_input == self.get_random_word()

    def is_user_guess_present_in_random_word(self, letter_input) -> bool:
        return letter_input in self.get_random_word()

    def is_letter_input_alphabet(self, letter_input) -> bool:
        return letter_input.isalpha()

    def make_list_of_random_word(self) -> list:
        return [letter for letter in self.get_random_word()]

    def pop_letter_index_for_multiple_occurence_of_letter(self, letter_index: int) -> None:
        self.make_list_of_random_word().pop(letter_index)

    def insert_at_letter_index_for_multiple_occurence_of_letter(self, letter_index: int) -> None:
        self.make_list_of_random_word().insert(letter_index, '_')

    def get_index_of_letter_in_list_of_random_word(self, letter_input: str) -> int:
        return self.make_list_of_random_word().index(letter_input)

    def hint_no_1(self) -> bool:
        return self._wrong_attempt == 2

    def hint_no_2(self) -> bool:
        return self._correct_attempt == 0 and self._wrong_attempt == self._max_attempts // 2


class WordGuess2:
    def __init__(self, max_attempts: int):
        self._max_attempts = max_attempts
        self._curr_attempt = 0
        self._random_word = random.choice(['hang', 'dare', 'truth', 'buffalo', 'peace', 'hello'])
        self._guess_characters = ["" for i in range(len(self._random_word))]

    def get_random_word(self) -> str:
        return self._random_word

    def register_user_input(self, char: str):
        for i in range(len(self._random_word)):
            if char == self._random_word[i]:
                self._guess_characters[i] = char

        self._curr_attempt += 1

    def is_attempts_left(self):
        return self._curr_attempt < self._max_attempts

    def is_word_guessed(self) -> bool:
        return self._random_word == "".join(self._guess_characters)


class CliHandler:
    def __init__(self, max_attempts):
        self._word_guess = WordGuess(max_attempts)

    def start(self):
        print(
            f'This is the Word guess game. You have only {self._word_guess.get_max_attempts()} guesses in total. Best of luck.')
        while self._word_guess.get_current_attempt() < self._word_guess.get_max_attempts():
            if self._word_guess.is_word_guessed_before_max_attempts_exhausts():
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
                    if self._word_guess.is_user_guess_equals_random_word(word_input):
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

            letter_input = input('Enter the letter:').lower()
            if not self._word_guess.is_letter_input_alphabet(letter_input):
                print('Invalid input!!\nPlease enter letter only!')
                continue
            self._word_guess.increment_current_attempt()
            if self._word_guess.is_user_guess_present_in_random_word(letter_input):
                letter_index = self._word_guess.get_index_of_letter_in_list_of_random_word(letter_input)
                print(
                    f'You guessed the correct letter.Letter position is {letter_index + 1} in the word.\t'
                    f'{self._word_guess.get_attempts_left()} attempt remaining!')
                self._word_guess.pop_letter_index_for_multiple_occurence_of_letter(letter_index)
                self._word_guess.insert_at_letter_index_for_multiple_occurence_of_letter(letter_index)
                print(self._word_guess.make_list_of_random_word())
                self._word_guess.increment_correct_attempt()
            else:
                print(
                    f'Wrong guess! {self._word_guess.get_attempts_left()} attempt remaining!\nTry again.')
                self._word_guess.increment_wrong_attempt()
            if self._word_guess.hint_no_1():
                print(f'\tHint for you. (Word has {len(self._word_guess.get_random_word())} letters.)')
            elif self._word_guess.hint_no_2():
                print(
                    f'Smart Hint -> (Word starts with {self._word_guess.get_random_word()[0]} and ends with {self._word_guess.get_random_word()[len(self._word_guess.get_random_word()) - 1]})')
        if self._word_guess.get_correct_attempt() == len(self._word_guess.get_random_word()):
            print(
                f'You guessed the correct word {self._word_guess.get_random_word()} in {self._word_guess.get_current_attempt()} attempt.')
        else:
            print(
                'You failed to guess the correct word!!')


if __name__ == "__main__":
    CliHandler(7).start()
