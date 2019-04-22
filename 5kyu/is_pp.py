# ----- Problem: What's a Perfect Power anyway? (5ku)
# ----- URL: https://www.codewars.com/kata/54d4c8b08776e4ad92000835
from math import sqrt


def is_pp(_n):
    """
    (int) -> list_of_2ints
    :param _n: int with positive number
    :return: base and power if _n is perfect number (ex [3, 4] for 81 because 3**4 = 81)
             None otherwise

    :description:
    A perfect power is a positive int that can be expressed as an integer power of another positive integer
    ex. 81 is a perfect power because 3**4 = 81

    :examples:
    is_pp(4) -> (2, 2)
    is_pp(9) -> (3, 2)
    is_pp(5) -> None
    is_pp(81) -> (3, 4)

    :algorithm:
    Need two auxiliary functions: find_divisors(num) and is_pp(divisor)

    find_divisors(num) returns None or divisors from 2 until sqrt(_num) which is the higher possible divisor
    find_power(divisor, _n) returns False or _power if divisor makes _n a perfect power
    """

    # find divisors and check if there is any power for any divisor that verifies _n is a pp
    divisors = find_divisors(_n)
    for divisor in divisors:
        base = divisor
        power = find_power(base, _n)
        if power:
            return base, power

    # no (base, power) pair found -> return None
    return None


def find_divisors(_num):
    divs = []  # divisors (output list)
    for candidate in range(2, int(sqrt(_num))+1):  # check candidates for divisors until sqrt(highest possible)
        if not _num % candidate:  # if it's a divisor
            divs.append(candidate)

    return divs


def find_power(_base, _num):
    _power = 2
    value = _base ** _power

    # increase _power and compute new value until value gets higher _num
    while value <= _num:
        if value == _num:  # _n is a perfect power
            return _power
        else:              # keep searching
            _power += 1
            value = _base ** _power

    # No appropriate power -> return False
    return False


# ------------------------- MAIN CODE -------------------------
result = is_pp(81)  # (3, 4)
print(result)
