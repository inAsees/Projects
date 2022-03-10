import random


class RpsGame:
    def __init__(self, max_attempts):
        self._current_attempt = 0
        self._max_attempts = max_attempts
        self._comp_choice = None
        self.user_score = 0
        self.comp_score = 0

    def increment_user_score(self):
        self.user_score += 1

    def increment_comp_score(self):
        self.comp_score += 1

    def is_attempts_left(self) -> bool:
        return self._current_attempt < self._max_attempts

    def make_choice(self):
        self._current_attempt += 1
        self._comp_choice = random.choice(["1", "2", "3"])

    def get_comp_choice(self) -> str:
        return self._comp_choice

    def get_result(self, user_input: str) -> str:
        results_mapping = {
            "1": {
                "1": "DRAW",
                "2": "LOSE",
                "3": "WON",
            },
            "2": {
                "1": "WON",
                "2": ["DRAW"],
                "3": "LOSE",
            },
            "3": {
                "1": "LOSE",
                "2": "WON",
                "3": "DRAW"
            }
        }
        if results_mapping[user_input][self._comp_choice] == "WON":
            self.increment_user_score()
        elif results_mapping[user_input][self._comp_choice] == "LOSE":
            self.increment_comp_score()
        return results_mapping[user_input][self._comp_choice]

    def is_user_winner(self) -> str:
        if self.user_score > self.comp_score:
            return "WON"
        elif self.user_score < self.comp_score:
            return "LOSE"
        else:
            return "DRAW"


class CliHandler:
    def __init__(self, max_attempts: int):
        self._max_attempts = max_attempts
        self._rps_game = RpsGame(max_attempts)

    def start(self):
        print(f'This is Rock Paper Scissor game.\tThere are {self._max_attempts} attempts.\n'
              f'For "Rock" press 1\n'
              f'For "Paper" press 2\n'
              f'For "Scissor" press 3')

        while self._rps_game.is_attempts_left():
            user_choice = input('enter:')
            if user_choice == "1":
                self._rps_game.make_choice()
                self._print_results("Rock", self._rps_game.get_comp_choice(), self._rps_game.get_result(user_choice))

            elif user_choice == "2":
                self._rps_game.make_choice()
                self._print_results("Paper", self._rps_game.get_comp_choice(), self._rps_game.get_result(user_choice))

            elif user_choice == "3":
                self._rps_game.make_choice()
                self._print_results("Scissors", self._rps_game.get_comp_choice(),
                                    self._rps_game.get_result(user_choice))

            else:
                print('Invalid input')
                continue

        print(f"Final result of the game:\n"
              f"You {self._rps_game.is_user_winner()} the game.")

    def _print_results(self, user_choice: str, comp_choice_code: str, result: str):
        choice_mapping = {
            "1": "Rock",
            "2": "Paper",
            "3": "Scissors"
        }
        print(f'Your choice is: {user_choice}')
        print(f'Computer choice is {choice_mapping[comp_choice_code]}')
        print(f'You: {result}')


if __name__ == "__main__":
    CliHandler(5).start()
