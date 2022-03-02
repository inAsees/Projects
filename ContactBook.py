import pickle
import os

class ContactBook:
    def __init__(self):
        pass

    def create_contact_book(self):
        contact_book = []
        file_obj = open('contact_book.pkl', 'wb')
        contacts = pickle.dump(contact_book, file_obj)
        file_obj.close()

    def add_contact(self):
        file_obj = open('contact_book.pkl', 'wb')
        contacts = pickle.load(file_obj)

    def edit_contact(self):
        file_obj = open('contact_book.pkl', 'rb')
        contacts = pickle.load(file_obj)

    def delete_contact(self):
        file_obj = open('contact_book.pkl', 'rb')
        contacts = pickle.load(file_obj)

    def search_contact(self):
        file_obj = open('contact_book.pkl', 'rb')
        contacts = pickle.load(file_obj)
        name_search = input('Enter the name:').lower()
        found = False
        for index in range(len(contacts)):
            if name_search == contacts[index][0].lower():
                found = True
                print(
                    f'\tName = {contacts[index][0]}\n\tContact number = {contacts[index][1]}\n\tEmail: {contacts[index][2]}\n\tAddress = {contacts[index][3]}')
        if found == False:
            print('Contact name not found.')
        file_obj.close()

    def display_contact_book(self):
        file_obj = open('contact_book.pkl', 'rb')
        contacts = pickle.load(file_obj)
        for index in range(len(contacts)):
            print(
                f'Contact no:{index + 1}\n\tContactName = {contacts[index][0]}\n\tContact number = {contacts[index][1]}\n\tEmail: {contacts[index][2]}\n\tAddress = {contacts[index][3]}')

        file_obj.close()

    def is_valid_email(self):
        pass

class CliHandler:
    def __init__(self):
        self._contact_book_obj = ContactBook()

    def start(self):
        if not 'contact_book.pkl' in os.getcwd():
            self._contact_book_obj.create_contact_book()

        while True:
            print(
                'This is your Contact book.\nIf you want to add a contact press "1"\n'
                'If you want to edit a contact press "2"\nIf you want to delete a contact press "3"\n'
                'If you want to search for contact press "4"\nIf you want to display your contact list press "5"')
            try:
                user_input = int(input('Enter your response:'))
                if user_input == 1:
                    first_name = input('First name:').capitalize()
                    surname = input('Surname:').capitalize()
                    self._contact_book_obj.
                    contact_number = input('mobile number:')
                    email = input('email:')
                    address = input('address:')
                    break
                elif user_input == 2:
                    break
                elif user_input == 3:
                    break
                elif user_input == 4:
                    break
                elif user_input == 5:
                    break
                else:
                    print('Invalid input!! Try again.')
            except Exception:
                print('Invalid input!! Try again.')


if __name__ == '__main__':
    pass




