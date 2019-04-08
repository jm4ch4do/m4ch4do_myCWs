# ----- Problem: String incrementer (5ku)
# ----- URL: https://www.codewars.com/kata/54a91a4883a7de5d7800009c


def string_inc(_string):
    """
    (string) -> string
    :param _string: string with characters and the ints
    :return: same _string but with + 1 in the final int

    :examples:
    (foo) -> (foo1)
    (foobar23) -> (foobar24)
    (foo0042) -> (foo0043)
    (foo9) -> (foo10)
    (foo099) -> (foo100)
    """
    if not _string or _string[-1] not in '0123456789':  # no number or empty string -> add 1 at the end
        return _string + str(1)
    else:
        # split str from int and make increment
        my_str, my_int = split_str_int(_string)
        new_int = int(my_int) + 1

        # put back together str and int maintaining initial zeros like in (foo0042) -> (foo0043)
        len_dif = len(str(my_int)) - len(str(new_int))
        new_int = str(new_int) if len_dif < 0 else '0'*len_dif + str(new_int)  # adds 000s for matching previous len

    return my_str + new_int


def split_str_int(_str):
    """
    :param _str: input _string
    :return: _string separated in string part and int part
    """
    for i in range(len(_str)):
        inv = len(_str) - i - 1  # inverse index
        if _str[inv] not in '0123456789':
            return _str[:inv+1], _str[inv+1:]

    # for input with no string like "1" or "001" return empty string and int
    return '', _str


my_string = 'foobar23'
result = string_inc(my_string)
expected = 'foo0043'
print(result)
