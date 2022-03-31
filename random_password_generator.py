import random


class PasswordGenerator:
    def __init__(self):
        self._words_repository = []

    def update_words_repository(self, word_input: str) -> None:
        self._words_repository.append(word_input)

    def save_words_repository_in_file(self, password_usage: str) -> None:
        with open(f"password_hint_for_{password_usage}.txt", 'w') as f:
            f.write(f"Words used to create the password are: {self._get_words_repository()}")

    def generate_password(self) -> str:
        lst = []
        for word in self._get_words_repository():
            for char in word:
                lst.append(char)
        password = random.sample(lst, k=len(lst))
        return "".join(password)

    def _get_words_repository(self) -> list[str]:
        return self._words_repository


class CliHandler:

    def start(self):
        password_gen = PasswordGenerator()
        password_usage = input("Password generator app.Where are you going to use this password?\n")
        print("Your provided words will be used to create a password."
              "How many words would you like to provide?")
        words_count = int(input("enter:"))
        for _ in range(words_count):
            word_input = input("enter your word:")
            password_gen.update_words_repository(word_input)
        print(f"Generated password is : {password_gen.generate_password()}")
        password_gen.save_words_repository_in_file(password_usage)


if __name__ == "__main__":
    CliHandler().start()
