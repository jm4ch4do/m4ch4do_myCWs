# ----- Problem: RGB to Hex Conversion (5ku)
# ----- URL: https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb2hex(_red, _green, _blue):
    """
    (int, int, int) -> (string)
    :param _red: int in range 0-255 representing the red color
    :param _green: int in range 0-255 representing the green color
    :param _blue: int in range 0-255 representing the blue color
    :return: string with hexadecimal representation of color

    :example:
    rgb2hex(255, 255, 300) -> 'FFFFFF'
    rgb2hex(148, 0 , 211) -> '9400D3'
    """
    # constants
    base = 16
    to_hex = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    # fix inputs out of range
    f_red, f_green, f_blue = fix_out_of_range([_red, _green, _blue])

    hex = ''
    for value in [f_red, f_green, f_blue]:
        int1 = value // base
        int2 = value % base
        str1 = str(int1) if int1 <= 9 else str(to_hex[int1])
        str2 = str(int2) if int2 <= 9 else str(to_hex[int2])
        hex += str1 + str2

    return hex


def fix_out_of_range(_int):
    _list = []
    for value in _int:
        if value > 255:
            fixed = 255
        elif value < 0:
            fixed = 0
        else:
            fixed = value
        _list.append(fixed)

    return _list


result = rgb2hex(148, 0, 211)
print(result)
