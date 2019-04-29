# ----- Problem: Not very secure (5ku)
# ----- URL: https://www.codewars.com/kata/526dbd6c8c0eb53254000110


def validate_alpha(_password):
    """
    (string) -> (boolean)
    :param _password: string with a password
    :return: True if password it's only alphanumeric

    :description:
    Empty string is not a valid password
    Allowed characters are uppercase/lowercase letters and digits
    No whitespaces/underscore

    :example:
    validate_alpha('myPassword123') -> True
    validate_alpha('my_pass') -> False
    validate_alpha('mypass*') -> False

    """
    # empty input -> return False
    if not _password:
        return False

    # if a characters is not letter or number -> return False
    for ch in _password:
        if ch.lower() not in 'abcdefghijklmnopqrstuvwxyz1234567890':
            return False

    # no problem -> return True
    return True


# simplest solution
def validate_alpha2(_password):
    return _password.isalnum()


# ------------------------- MAIN CODE -------------------------
result = validate_alpha('myPassword123')
print(result)
