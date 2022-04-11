import os
import pandas as pd


class ContactBook:
    def __init__(self):
        self.create_contact_book_if_not_exists()
        self._df = self.load_from_file()

    @staticmethod
    def create_contact_book_if_not_exists() -> None:
        if 'contact_book.csv' not in os.listdir(os.getcwd()):
            df = pd.DataFrame(columns=["Name", "Contact_number", "Email_Id", "Address"])
            df.to_csv(r"C:\Users\DELL\PycharmProjects\TestProject\Beginner projects in Python\contact_book.csv",
                      index=False)

    @staticmethod
    def load_from_file() -> pd.DataFrame:
        df = pd.read_csv(r"C:\Users\DELL\PycharmProjects\TestProject\Beginner projects in Python\contact_book.csv")
        return df

    def is_name_in_contact_book(self, name) -> bool:
        return name in list(self._df.Name)

    def add_contact(self, name, contact_number, email_id, address) -> None:
        df = {
            "Name": name,
            "Contact_number": contact_number,
            "Email_Id": email_id,
            "Address": address
        }
        new_df = self._df.append(df, ignore_index=True)
        new_df.to_csv(r"C:\Users\DELL\PycharmProjects\TestProject\Beginner projects in Python\contact_book.csv",
                      index=False)

    def edit_contact(self, name) -> None:
        pass

    def delete_contact(self, name) -> None:
        df = self._df.loc[self._df["Name"] != name]
        df.to_csv(r"C:\Users\DELL\PycharmProjects\TestProject\Beginner projects in Python\contact_book.csv",
                  index=False)

    def search_contact(self, name):
        for row in list(self._df.values):
            if row[0] == name:
                return row

    @staticmethod
    def display_contact_book() -> None:
        pass


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
