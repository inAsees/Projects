import pickle
import os


class ContactBook:
    def __init__(self):
        pass

    def create_contact_book(self):
        with open('contact_book.pkl', 'wb') as f:
            pickle.dump([], f)

    def add_contact(self, first_name, surname, contact_number, email, address):
        with open('contact_book.pkl', 'rb+') as f:
            contacts = pickle.load(f)
            contacts.append([first_name + ' ' + surname, contact_number, email, address])
            pickle.dump(contacts, f)

    def edit_contact(self):
        with open('contact_book.pkl', 'rb+') as f:
            contacts = pickle.load(f)
            pass

    def delete_contact(self, user_input) -> bool:
        with open('contact_book.pkl', 'rb+') as f:
            contacts = pickle.load(f)
            for index in range(len(contacts)):
                if user_input == contacts[index][0]:
                    contacts.pop(index)
                    break
                return True
        
        return False

    def search_contact(self, name_search):
        with open('contact_book.pkl', 'rb+') as f:
            contacts = pickle.load(f)
            for index in range(len(contacts)):
                if name_search == contacts[index][0].lower():
                    return contacts[index]
        return None

    def display_contact_book(self):
        with open('contact_book.pkl', 'rb') as f:
            contacts = pickle.load(f)
            for index in range(len(contacts)):
                pass

    def is_file_in_current_working_dir(self) -> bool:
        return 'contact_book.pkl' in os.getcwd()


class CliHandler:
    def __init__(self):
        self._contact_book_obj = ContactBook()

    def start(self):
        if not self._contact_book_obj.is_file_in_current_working_dir():
            self._contact_book_obj.create_contact_book()

        while True:
            print(
                'This is your Contact book.\nIf you want to add a contact press "1"\n'
                'If you want to edit a contact press "2"\nIf you want to delete a contact press "3"\n'
                'If you want to search for contact press "4"\nIf you want to display your contact list press "5"')

            user_input = int(input('Enter your response:'))
            if user_input == 1:
                first_name = input('First name:').capitalize()
                surname = input('Surname:').capitalize()
                contact_number = input('mobile number:')
                email = input('email:')
                address = input('address:')
                self._contact_book_obj.add_contact(first_name, surname, contact_number, email, address)
                print('You contact has been successfully created.')
                break
            elif user_input == 2:
                break
            elif user_input == 3:
                user_input = input('enter the name of the contact you want to delete:')
                if self._contact_book_obj.delete_contact(user_input):
                    print('Contact is deleted successfully.')
                else:
                    print('Contact not found')
                break
            elif user_input == 4:
                name_search = input('Enter the name:').lower()
                contacts = self._contact_book_obj.search_contact(name_search)
                if contacts == None:
                    print('Name not found')
                    break
                print(
                    f'\tName = {contacts[0]}\n\tContact number = {contacts[1]}\n\tEmail: {contacts[2]}\n'
                    f'\tAddress = {contacts[3]}')
                break
            elif user_input == 5:
                self._contact_book_obj.display_contact_book()
                break


if __name__ == '__main__':
    CliHandler().start()
