import random


class PasswordGenerator:
    def __init__(self):
        self._minimum_length = 4

    def generate_password(self, password_length: int) -> str:
        if password_length != 0:
            pass
        else:
            password_length = random.randint(self._minimum_length, 12)
            pass

    def get_minmum_length(self)->int:
        return self._minimum_length


class CliHandler:

    def start(self):
        password_gen = PasswordGenerator()
        password_usage = input("Password Generator Application.\n"
                               "Where are you going to use this password? "
                               "Example:Facebook,Instagram etc.\n")
        while True:
            user_input = input(
                f"Do you want to provide maximum length for the password?\n"
                f"Make sure to provide minimum length of {password_gen.get_minmum_length()} characters.\n"
                "If YES press '1'.\n"
                "If NO press '2'.\n")
            if user_input == "1":
                while True:
                    try:
                        password_length = int(input("Please provide the maximum length of the password:"))
                    except ValueError as e:
                        print("Invalid input")
                        continue

                    if password_length < password_gen.get_minmum_length():
                        print(f"This is less than {password_gen.get_minmum_length()},try again.")
                        continue
                    password_gen.generate_password(password_length)
                    break
                break

            elif user_input == "2":
                password_gen.generate_password(password_length=0)
                break
            else:
                print("Invalid input")
                continue


if __name__ == "__main__":
    CliHandler().start()
