import os
import csv
import pandas as pd


class ContactBook:
    def __init__(self):
        self.create_contact_book()

    @staticmethod
    def create_contact_book():
        if 'contact_book.csv' not in os.listdir(os.getcwd()):
            with open('contact_book.csv', 'w') as f:
                header = csv.DictWriter(f, fieldnames=["Name", "Contact number", "Email Id", "Address"])
                header.writeheader()

    @staticmethod
    def add_contact(name, contact_number, email_id, address) -> None:
        df = pd.DataFrame([[name, contact_number, email_id, address]])
        df.to_csv(r"C:\Users\DELL\PycharmProjects\TestProject\Beginner projects in Python\contact_book.csv", mode='a',
                  header=False, index=False)

    @staticmethod
    def edit_contact(name):
        pass

    def delete_contact(self, user_input):
        with open('contact_book.csv', 'rb+') as f:
            pass

    @staticmethod
    def search_contact(name) -> list:
        df = pd.read_csv(r"C:\Users\DELL\PycharmProjects\TestProject\Beginner projects in Python\contact_book.csv")
        arr = df.values
        for row in arr:
            if row[0] == name:
                return row

    def display_contact_book(self):
        pass

    @staticmethod
    def is_name_in_contact_book(name) -> bool:
        df = pd.read_csv(r"C:\Users\DELL\PycharmProjects\TestProject\Beginner projects in Python\contact_book.csv")
        return name in list(df.Name)


class CliHandler:
    def __init__(self):
        self._contact_book = ContactBook()

    def start(self):

        print(
            'This is your Contact book.\n'
            'If you want to add a contact press "1"\n'
            'If you want to edit a contact press "2"\n'
            'If you want to delete a contact press "3"\n'
            'If you want to search for contact press "4"\n'
            'If you want to display your contact list press "5"')
        while True:
            user_input = int(input('Enter your response:'))
            if user_input == 1:
                name = input('Name:')
                if self._contact_book.is_name_in_contact_book(name):
                    print("Name already exists in the contact book,please use different name.")
                    continue
                contact_number = input('Mobile number:')
                email_id = input('Email Id:')
                address = input('Address:')
                self._contact_book.add_contact(name, contact_number, email_id, address)
                print('You contact has been successfully created.')
                break

            elif user_input == 2:
                name = input('Name:')
                if self._contact_book.is_name_in_contact_book(name):
                    contact = self._contact_book.search_contact(name)
                    print(f"Name:{contact[0]}\n"
                          f"Contact Number:{contact[1]}\n"
                          f"Email Id:{contact[2]}\n"
                          f"Address:{contact[3]}")
                    pass
                    break
                print("Name does not exist")
                continue
            elif user_input == 3:
                name = input('Name:')
                if self._contact_book.is_name_in_contact_book(name):
                    pass
                    break
                print("Name does not exist")
                continue
            elif user_input == 4:
                name = input('Enter the name:').lower()
                if self._contact_book.is_name_in_contact_book(name):
                    contact = self._contact_book.search_contact(name)
                    print(f"Name:{contact[0]}\n"
                          f"Contact Number:{contact[1]}\n"
                          f"Email Id:{contact[2]}\n"
                          f"Address:{contact[3]}")
                    break
                print("Name does not exist")
                continue
            elif user_input == 5:
                break


if __name__ == '__main__':
    CliHandler().start()
