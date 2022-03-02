class EmailSlicer:
    def __init__(self, email):
        self._email = email

    def is_valid_email(self) -> bool:
        return '@' not in self._email or self._email[len(self._email) - 4:] != '.com'

    def username(self):
        return self._email[:self._email.index('@')]

    def domain_name(self):
        return self._email[self._email.index('@') + 1:]


class CliHandler:
    def start(self):
        while True:
            email = input('Enter the email:')
            email_slicer_obj = EmailSlicer(email)
            if email_slicer_obj.is_valid_email():
                print('Enter a valid email address.')
                continue
            else:
                print(
                    f'Your username is {email_slicer_obj.username()} and domain name is {email_slicer_obj.domain_name()}')
                break


if __name__ == '__main__':
    CliHandler().start()
