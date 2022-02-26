def email_slicer(email: str):
    user_name = email[:email.index('@')]
    domain_name = email[email.index('@') + 1:]
    return user_name, domain_name


email = input('Enter your email:')
print(f'your username and domain names are {email_slicer(email)}')
