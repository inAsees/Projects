import random
import string
import os
import csv


class PasswordGenerator:
    def __init__(self):
        self._minimum_length = 4

    def generate_password(self, password_usage: str, password_length: int) -> str:
        password = ""
        if password_length != 0:
            for i in range(password_length):
                password += random.choice(string.ascii_letters + string.punctuation + string.digits)

        else:
            password_length = random.randint(self._minimum_length, 12)
            for i in range(password_length):
                password += random.choice(string.ascii_letters + string.punctuation + string.digits)

        self._save_password_in_file(password_usage, password)
        return password

    def create_directory(self) -> None:
        if "my_passwords_repository" not in os.listdir(r'C:\Users\DELL\Desktop'):
            os.mkdir(r"C:\Users\DELL\Desktop\my_passwords_repository")
            with open(r"C:\Users\DELL\Desktop\my_passwords_repository\passwords_list.csv",
                      "w") as f:
                writer = csv.writer(f)
                writer.writerow(["Domain Name", "Password"])

    def get_minimum_length(self) -> int:
        return self._minimum_length

    def _save_password_in_file(self, password_usage: str, password: str) -> None:
        with open(rf"C:\Users\DELL\Desktop\my_passwords_repository\passwords_list.csv",
                  "a") as f:
            writer = csv.writer(f)
            writer.writerow([password_usage, password])


class CliHandler:

    def __init__(self):
        self._password_gen = PasswordGenerator()
        self._create_directory = self._password_gen.create_directory()

    def start(self):
        password_usage = input("Password Generator Application.\n"
                               "Where are you going to use this password? "
                               "Example:Facebook,Instagram etc.\n")
        while True:
            user_input = input(
                f"Do you want to provide maximum length for the password?\n"
                f"Make sure to provide minimum length of {self._password_gen.get_minimum_length()} characters.\n"
                "If YES press '1'.\n"
                "If NO press '2'.\n")
            if user_input == "1":
                while True:
                    try:
                        password_length = int(input("Please provide the maximum length of the password:"))
                    except ValueError as e:
                        print("Invalid input")
                        continue

                    if password_length < self._password_gen.get_minimum_length():
                        print(f"This is less than {self._password_gen.get_minimum_length()},try again.")
                        continue
                    print(f"Password is: {self._password_gen.generate_password(password_usage, password_length)}")
                    break
                break

            elif user_input == "2":
                print(f"Password is: {self._password_gen.generate_password(password_usage, password_length=0)}")
                break
            else:
                print("Invalid input")
                continue

        pass


if __name__ == "__main__":
    CliHandler().start()
