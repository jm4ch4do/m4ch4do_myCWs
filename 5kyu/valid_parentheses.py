def valid_parentheses(_string):
    """
    (string) -> (boolean)
    :param _string: string with a series of characters and parentheses
    :return: True if _string has a valid display of parentheses

    :example:
    "()" -> True
    ")(()))" -> False
    "(" -> False
    "(())((()())())" -> True

    :algorithm:
    . check every character
        . For ( increase parentheses count,
        . For ) decrease parentheses count,
        . If ever the count gets negative -> False
    . At the end if the count != 0 -> False
    . Else -> True

    """
    count = 0
    for ch in _string:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1

        if count < 0:
            return False

    if count != 0:
        return False

    return True
