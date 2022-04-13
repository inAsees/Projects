from contact_book import ContactBook


class CliHandler:
    def __init__(self):
        self._contact_book = ContactBook(
            r"C:\Users\DELL\PycharmProjects\TestProject\Beginner projects in Python\contact_book.csv")

    @staticmethod
    def _if_user_wants_to_edit_contact() -> bool:
        response = input("If YES press '1' or '2' if NO:\n")
        if response == "1":
            return True
        elif response == "2":
            return False

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
                name = input('Name: ')
                if not self._contact_book.is_name_in_contact_book(name):
                    print("Name does not exist")
                    continue
                contact = self._contact_book.search_contact(name)
                print("Below is your contact details.")
                print(f"Name:{contact[0]['name']}\n"
                      f"Contact Number:{contact[0]['contact_number']}\n"
                      f"Email Id:{contact[0]['email_id']}\n"
                      f"Address:{contact[0]['address']}")
                print("Would you like to edit Name?")
                if self._if_user_wants_to_edit_contact():
                    new_name = input("new name: ")
                else:
                    new_name = None
                print("Would you like to edit mobile number?\n")
                if self._if_user_wants_to_edit_contact():
                    new_contact_number = input("new mobile number: ")
                else:
                    new_contact_number = None
                print("Would you like to edit Email Id?\n")
                if self._if_user_wants_to_edit_contact():
                    new_email_id = input("new email id: ")
                else:
                    new_email_id = None
                print("Would you like to edit Address?\n")
                if self._if_user_wants_to_edit_contact():
                    new_address = input("new address: ")
                else:
                    new_address = None
                self._contact_book.edit_contact(name, new_name, new_contact_number, new_email_id, new_address)
                print("Contact updated successfully")
                break
            elif user_input == 3:
                name = input('Name:')
                if not self._contact_book.search_contact(name):
                    print("Name does not exist")
                    continue
                self._contact_book.delete_contact(name)
                print("Contact deleted successfully.")
                break
            elif user_input == 4:
                name = input('Enter the name:\n').lower()
                if not self._contact_book.is_name_in_contact_book(name):
                    print("Name does not exist")
                    continue
                contact = self._contact_book.search_contact(name)
                print(f"Name:{contact[0]['name']}\n"
                      f"Contact Number:{contact[0]['contact_number']}\n"
                      f"Email Id:{contact[0]['email_id']}\n"
                      f"Address:{contact[0]['address']}")
                break
            elif user_input == 5:
                contack_book = self._contact_book.display_contact_book()
                for row in contack_book:
                    print(f"Name: {row['name']}\n"
                          f"Contact number: {row['contact_number']}\n"
                          f"Email Id: {row['email_id']}\n"
                          f"Address: {row['address']}", end='\n\n')
                break
            else:
                print("Invalid input")
                continue


if __name__ == '__main__':
    CliHandler().start()