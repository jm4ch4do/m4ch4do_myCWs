# ----- Problem: Human Readable Time (5kyu)
# ----- URL: https://www.codewars.com/kata/52685f7382004e774f0001f7


def make_readable(_seconds):
    """
    (int) -> (string)
    :param _seconds: int with an amount of seconds
    :return: string with _seconds formatted to HH:MM:SS

    :example:
    _seconds = 359999
    returns = '99:59:59'
    """

    # _can't be higher than 359999 for 99:59:59
    if _seconds > 359999:
        return None

    # take hours
    hours = _seconds // (60 * 60)
    hh = str(hours) if len(str(hours)) == 2 else '0' + str(hours)
    _seconds -= hours * (60 * 60)

    # take minutes
    minutes = _seconds // 60
    mm = str(minutes) if len(str(minutes)) == 2 else '0' + str(minutes)
    _seconds -= minutes * 60

    # take seconds
    ss = str(_seconds) if len(str(_seconds)) == 2 else '0' + str(_seconds)

    # return human time
    return ':'.join([hh, mm, ss])


# ---- MAIN CODE -------------------------------------------------------------------------------
my_seconds = 359999
expected = '99:59:59'
result = make_readable(my_seconds)
print(result)
