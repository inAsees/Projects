def email_slicer(email: str):
    user_name = email[:email.index('@')]
    domain_name = email[email.index('@') + 1:]
    return user_name, domain_name


while True:
    email = input('Enter your email:')
    if '@' not in email or email[len(email)-4:] != '.com':
        print('Enter a valid email address.')
    else:
        print(f'your username and domain names are {email_slicer(email)}')
        break
