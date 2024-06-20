# exceptions.py

class LoginPageException(Exception):
    """Base class for exceptions in this module."""
    pass


class LoginFailedException(LoginPageException):
    """Raised when login fails."""
    pass


class LoginSuccessException(LoginPageException):
    """Raised when login is expected to succeed but fails."""
    pass


class LoginTimeoutException(LoginPageException):
    """Raised when the login operation times out."""
    pass

class ProductInteractionError(Exception):
    pass