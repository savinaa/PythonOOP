class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    email_to_check = input()
    constants = {
        "separator": "@",
        "length name": 4,
        "allowed domains": (".com", ".bg", ".net", ".org")
    }
    if constants["separator"] not in email_to_check:
        raise MustContainAtSymbolError("Email must contain @")

    name, host_domain = email_to_check.split("@")
    if len(name) < constants["length name"]:
        raise NameTooShortError("Name must be more than 4 characters")

    for domain in constants["allowed domains"]:
        if host_domain.endswith(domain):
            print("Email is valid")
            break
    else:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
