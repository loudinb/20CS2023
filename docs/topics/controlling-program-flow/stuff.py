import string

def validate_password(password):
    """ Validates a password based on the following criteria:
    1. At least 8 characters long
    2. Contains at least one uppercase letter
    3. Contains at least one lowercase letter
    4. Contains at least one digit
    5. Contains at least one special character from the set: !@#$%^&*()_+-=[]{}|;:,.<>?

    Args:
      password (str): The password to validate

    Returns:
      bool: True if the password meets all criteria, False otherwise
    """
    if len(password) < 8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    for char in password:
        if char in string.ascii_uppercase:
            has_uppercase = True
        elif char in string.ascii_lowercase:
            has_lowercase = True
        elif char in string.digits:
            has_digit = True
        elif char in special_chars:
            has_special = True

    return has_uppercase and has_lowercase and has_digit and has_special