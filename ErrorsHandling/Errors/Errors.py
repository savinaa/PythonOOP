class Error(Exception):
    pass

class NameTooShortError(Error):
    #raise it when the name in the email is less than or equal to 4
    pass

class MustContainAtSymbolError(Error):
    #raise it when there is no "@" in the email
    pass

class InvalidDomainError(Error):
    #raise it when the domain of the email is invalid (valid domains are: .com, .bg, .net, .org)
    pass