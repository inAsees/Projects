class Email_slicer:
    def __init__(self, email):
        self._email = email

    def is_valid_email(self) -> bool:
        return '@' not in self._email or self._email[len(self._email) - 4:] != '.com'

    def username(self):
        return self._email[:self._email.index('@')]

    def domain_name(self):
        return self._email[self._email.index('@') + 1:]


class Cli_handler:
    def __init__(self, email):
        self._email = email
        self._email_slicer_obj = Email_slicer(email)

    def start(self):
        while True:
            if self._email_slicer_obj.is_valid_email():
                print('Enter a valid email address.')
                Cli_handler(input('Enter your email:')).start()
            else:
                print(
                    f'Your username is {self._email_slicer_obj.username()} and domain name is {self._email_slicer_obj.domain_name()}')
                break


if __name__ == '__main__':
    Cli_handler(input('Enter your email:')).start()
