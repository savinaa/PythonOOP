import ErrorsHandling.Errors.Errors as e

valid_domains=['com', 'bg', 'org', 'net']

while True:
    text = input()
    if text == 'End':
        break

    if '@' not in text:
        raise e.MustContainAtSymbolError("Email must contain @")

    email_parts = text.split('@')
    name=email_parts[0]
    domain = email_parts[1]
    extension=domain.split('.')[-1]

    if len(name) <= 4:
        raise e.NameTooShortError("Name must be more than 4 characters")

    if extension not in valid_domains:
        raise e.InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    print('Email is valid')


