import random


class RpsGame:
    def __init__(self):
        self.max_attempts = 5
        self.current_attempt = 0
        self.user_score = 0
        self.comp_score = 0

    def increment_current_attempt(self) -> None:
        self.current_attempt += 1

    def _increment_user_score(self) -> None:
        self.user_score += 1

    def _increment_comp_score(self) -> None:
        self.comp_score += 1

    def is_choice_r_p_or_s(self, user_choice) -> str:
        if user_choice == 1:
            return "Rock"
        elif user_choice == 2:
            return "Paper"
        else:
            return "Scissor"

    def _rps_logic(self, user_choice) -> int:
        comp_choice = random.randint(1, 3)

        if user_choice == comp_choice:
            return -1
        elif user_choice == 1:
            if comp_choice == 2:
                self._increment_comp_score()
                return 3
            else:
                self._increment_user_score()
                return 2
        elif user_choice == 2:
            if comp_choice == 3:
                self._increment_comp_score()
                return 5
            else:
                self._increment_user_score()
                return 4
        elif user_choice == 3:
            if comp_choice == 1:
                self._increment_comp_score()
                return 7
            else:
                self._increment_user_score()
                return 6

    def user_vs_comp(self, user_choice) -> bool or None:
        if self._rps_logic(user_choice) < 0:
            return None
        elif self._rps_logic(user_choice) % 2 != 0:
            return True
        else:
            return False

    def winner(self) -> bool:
        if self.user_score > self.comp_score:
            return True
        elif self.user_score < self.comp_score:
            return False

    def draw(self) -> bool:
        return self.user_score == self.comp_score


class CliHAndler:
    def __init__(self):
        self.rps_game = RpsGame()

    def start(self):
        print(
            f'This is Rock Paper Scissor game.\tThere are {self.rps_game.max_attempts} attempts.\nFor "Rock" press 1\nFor "Paper" press 2\nFor "Scissor" press 3')
        while self.rps_game.current_attempt < self.rps_game.max_attempts:
            try:
                user_choice = int(input('Enter: '))
            except ValueError:
                print('Invalid response.')
                continue
            if user_choice < 1 or user_choice > 3:
                print('Invalid response.')
                continue
            self.rps_game.increment_current_attempt()
            print(self.rps_game.is_choice_r_p_or_s(user_choice))
            if self.rps_game.user_vs_comp(user_choice) == None:
                print('MATCH DRAW')
                continue

            if self.rps_game.user_vs_comp(user_choice):
                print('You won the MATCH')
            else:
                print("You loose the MATCH")
        if self.rps_game.draw():
            print(self.rps_game.user_score,self.rps_game.comp_score)
            print('GAME DRAW')
        if self.rps_game.winner():
            print(self.rps_game.user_score, self.rps_game.comp_score)
            print("You won the GAME")
        else:
            print(self.rps_game.user_score, self.rps_game.comp_score)
            print("Comp won the GAME")


if __name__ == "__main__":
    CliHAndler().start()
