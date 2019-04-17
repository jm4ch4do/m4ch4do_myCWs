# ----- Problem: Integers: Recreation One (5ku)
# ----- URL: https://www.codewars.com/kata/55aa075506463dac6600010d
from math import sqrt, floor


def list_squared(_ini, _last):
    """
    (int, int) -> list_of_list_of_two_strings
    :param _ini: int with initial value which is to be included
    :param _last: int with ending value which is to be included
    :return: list with list of two ints
                first int a number between _ini and _last that meets certain criteria
                second int is a value that verifies the criteria

    :description:
    The selection criteria is best understood with the following example:
        Divisors of 42 are: 1, 2, 3, 6, 7, 14, 21, 42
        These divisors squared are 1, 4, 9, 36, 49, 196, 441, 1764
        The sum of the squared divisor is 2500 which is 50*50, a square!
        So 42 meets the criteria

    :example:
    list_squared(1, 250) -> [[1, 1], [42, 2500], [246, 84100]]

    :algorithm:
    To find 'winners' who match the given criteria you have to:
        Check every number in the input range
            For every number you have to
                Find divisors
                Square and Sum Divisors to get a value
                Check if value meets criteria

    The process is simple, the only trick is in the 'Find divisors part' you'll gain speed if you only check until sqrt
    Example, for 10, the divisors are 1, 2 and 5; to find this I only checked 1, 2 and 3 because sqrt(10) = 3.162
        every number after sqrt that may be a divisor will be paired with one from before sqrt
        in the previous example 5 was paired with 5

    """
    # set-up
    winners = []  # output list

    # check every number from _ini to _last
    for number in range(_ini, _last+1):
        divisors = find_divisors(number)
        value = square_and_sum(divisors)
        if check_criteria(value):
            winners.append([number, value])

    return winners


def find_divisors(_number):
    divs = []
    limit = floor(sqrt(_number))  # you only need to check until sqrt(_number)
    for i in range(1, limit+1):
        division_result = _number / i
        if division_result.is_integer():  # if it is a divisor -> save it
            divs.append(i)
            if division_result != i:  # save pair if not equal (ex. for 25 there is no need to save 5 two times)
                divs.append(int(division_result))

    return divs


def square_and_sum(_divisors):
    output = 0
    for divisor in _divisors:
        output += divisor ** 2

    return output


def check_criteria(_value):
    return sqrt(_value).is_integer()
