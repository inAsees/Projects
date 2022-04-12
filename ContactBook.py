import os
from typing import List, Dict, Optional

import pandas as pd


class ContactBook:
    def __init__(self, resource_file_path: str):
        self._res_file_path = resource_file_path
        self._df = self.load_from_file()

    def load_from_file(self) -> pd.DataFrame:
        if os.path.exists(self._res_file_path):
            return pd.read_csv(self._res_file_path)

        return pd.DataFrame(columns=["name", "contact_number", "email_id", "address"])

    def add_contact(self, name: str, contact_number: int, email_id: str, address: str) -> None:
        row = {
            "name": name,
            "contact_number": contact_number,
            "email_id": email_id,
            "address": address
        }
        self._df = self._df.append(row, ignore_index=True)
        self._df.to_csv(self._res_file_path, index=False)

    def edit_contact(self, name: str, new_name: Optional[str], new_phone: Optional[int], new_email: Optional[str],
                     new_address: Optional[str]) -> None:
        idx = self._df.loc[self._df.name == name].index
        if len(idx) == 0:
            return

        idx = idx[0]
        if new_name is not None:
            self._df.loc[idx, "name"] = new_name
        if new_phone is not None:
            self._df.loc[idx, "contact_number"] = new_phone
        if new_email is not None:
            self._df.loc[idx, "email_id"] = new_email
        if new_address is not None:
            self._df.loc[idx, "address"] = new_address

        self._df.to_csv(self._res_file_path, index=False)

    def delete_contact(self, name: str) -> None:
        self._df.drop(self._df[self._df.name == name].index, inplace=True)
        self._df.to_csv(self._res_file_path, index=False)

    def search_contact(self, name: str) -> List[Dict]:
        res = []
        df = self._df[self._df.name == name]
        for _, row in df.iterrows():
            res.append(dict(row))
        return res

    def display_contact_book(self) -> List[Dict]:
        res = []
        for _, row in self._df.iterrows():
            res.append({"name": row["name"], "address": row["address"]})

        return res


class CliHandler:
    def __init__(self):
        self._contact_book = ContactBook(
            r"C:\Users\DELL\PycharmProjects\TestProject\Beginner projects in Python\contact_book.csv")

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
                if not self._contact_book.is_name_in_contact_book(name):
                    print("Name does not exist")
                    continue
                contact = self._contact_book.search_contact(name)
                print(f"Name:{contact[0]}\n"
                      f"Contact Number:{contact[1]}\n"
                      f"Email Id:{contact[2]}\n"
                      f"Address:{contact[3]}")
                name = input('Name:')
                contact_number = input('New Mobile number:')
                email_id = input('New Email Id:')
                address = input('New Address:')
                break
            elif user_input == 3:
                name = input('Name:')
                if not self._contact_book.is_name_in_contact_book(name):
                    print("Name does not exist")
                    continue
                self._contact_book.delete_contact(name)
                print("Contact deleted successfully.")
                break
            elif user_input == 4:
                name = input('Enter the name:').lower()
                if not self._contact_book.is_name_in_contact_book(name):
                    print("Name does not exist")
                    continue
                contact = self._contact_book.search_contact(name)
                print(f"Name:{contact[0]}\n"
                      f"Contact Number:{contact[1]}\n"
                      f"Email Id:{contact[2]}\n"
                      f"Address:{contact[3]}")
                break



            elif user_input == 5:
                pass
                break
            else:
                print("Invalid input")
                continue


if __name__ == '__main__':
    CliHandler().start()
