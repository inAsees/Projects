import random
import string
import os
import csv
from typing import Dict, Optional


class PasswordGenerator:
    def __init__(self, parent_directory: str, resource_directory_path: str, resource_file_path: str):
        self._parent_directory = parent_directory
        self._resource_directory_path = resource_directory_path
        self._resource_file_path = resource_file_path
        self._create_directory_if_not_exists()
        self._dic = self._load_from_file()
        self._minimum_length = 4

    def is_password_already_exits(self, password_usage: str) -> bool:
        return password_usage in self._dic:
      

    def generate_password(self, password_usage: str, password_length: Optional[int]) -> str:
        password = ""
        if password_length is None:
            password_length = 12
        password = random.sample(string.ascii_letters + string.punctuation + string.digits, k=password_length)
        self._dic[password_usage] = "".join(password)
        return "".join(password)

    def save(self) -> None:
        with open(self._resource_file_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["domain", "password"])
            writer.writeheader()
            for domain in self._dic:
                writer.writerow({"domain": domain, "password": self._dic[domain]})

    def get_minimum_length(self) -> int:
        return self._minimum_length

    def _load_from_file(self) -> Dict:
        dic = {}

        if not os.path.exists(self._resource_file_path):
            return dic

        with open(self._resource_file_path, "r") as f:
            reader = csv.DictReader(f)
            for rows in reader:
                dic[rows["domain"]] = rows["password"]

        return dic

    def _create_directory_if_not_exists(self) -> None:
        if "my_passwords_repository" not in os.listdir(self._parent_directory):
            os.mkdir(self._resource_directory_path)

class CliHandler:
    def start(self):
        password_gen = PasswordGenerator(r'C:\Users\DELL\Desktop\test_files',
                                         r"C:\Users\DELL\Desktop\test_files\my_passwords_repository",
                                         r"C:\Users\DELL\Desktop\test_files\my_passwords_repository\passwords_list.csv"
                                         )
        password_usage = input("Password Generator Application.\n"
                               "Where are you going to use this password? "
                               "Example:Facebook,Instagram etc.\n")
        if password_gen.is_password_already_exits(password_usage):
            print(f"{password_usage} password already exists.\n"
                  f"Do you want to replace it?\n"
                  f"If YES press '1' or '2' if NO.\n")
            while True:
                user_input = input("Enter:")
                if user_input == "2":
                    print("App closed.")
                    quit()
                elif user_input == "1":
                    break
                else:
                    print("Invalid input")
                    continue
        while True:
            user_input = input(
                f"Do you want to provide maximum length for the password?\n"
                f"Make sure to provide minimum length of {password_gen.get_minimum_length()} characters.\n"
                "If YES press '1'.\n"
                "If NO press '2'.\n")
            if user_input == "1":
                while True:
                    try:
                        password_length = int(input("Please provide the maximum length of the password:"))
                    except ValueError as e:
                        print("Invalid input")
                        continue

                    if password_length < password_gen.get_minimum_length():
                        print(f"This is less than {password_gen.get_minimum_length()},try again.")
                        continue
                    print(f"Password is: {password_gen.generate_password(password_usage, password_length)}")
                    break
                break

            elif user_input == "2":
                print(f"Password is: {password_gen.generate_password(password_usage, password_length=None)}")
                break
            else:
                print("Invalid input")
                continue
        print("Do you want to save the password?\n"
              "If YES press 1\n"
              "If NO press 2\n")
        while True:
            user_input = input()
            if user_input == "1":
                password_gen.save()
                print("Password saved successfully")
                break
            elif user_input == "2":
                print("Password not saved.")
                break
            else:
                print("Invalid input")
                continue


if __name__ == "__main__":
    CliHandler().start()
