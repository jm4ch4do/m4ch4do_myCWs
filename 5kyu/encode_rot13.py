# ----- Problem: Rot13 (5ku)
# ----- URL: https://www.codewars.com/kata/rot13-1/train/python


def encode_rot13(_message):
    """
    (string) -> (string)
    :param _message: string with any sequence of characters
    :return: every character rotated 13 letters in the alphabet (classic rot13 encoding)

    :example:
    _message = "test"
    returns "grfg"

    _message = "Test"
    returns "Grfg"

    _message = "abcdefghijklmnopqrstuvwxyz"
    returns nopqrstuvwxyzabcdefghijklm
    """

    # constants
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    BASE = 13
    LEN = len(ALPHABET)

    # Translate every character
    code = ''
    for ch in _message:

        if ch.lower() not in ALPHABET:  # unknown characters are not modified
            code += ch
        else:
            index = ALPHABET.find(ch.lower())

            # increase index by 13 (_BASE) and return to the start after last character (_LEN)
            index += BASE if index + BASE < LEN else BASE - LEN
            coded_ch = ALPHABET[index] if ch.islower() else ALPHABET[index].upper()
            code += coded_ch

    return code


my_message = 'abcdefghijklmnopqrstuvwxyz'
result = encode_rot13(my_message)
expected = 'nopqrstuvwxyzabcdefghijklm'
print(result == expected)
