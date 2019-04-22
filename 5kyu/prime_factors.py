# ----- Problem: Primes in numbers (5ku)
# ----- URL: https://www.codewars.com/kata/54d512e62a5e54c96200019e
from math import floor, sqrt


def prime_factors(_n):
    """
    (int) -> (string)
    :param _n: int with positive int
    :return: string with the decomposition in prime factors of _n

    :example:
    prime_factors(7775460) -> "(2**2)(3**3)(5)(7)(11**2)(17)"

    :description:
    The first key here is to realize that you don't really need to search for primes
    If you search divisors starting from 2 and going up, you'll only find prime divisors
    The second key is to search divisors from 2 until sqrt of the given number
        No divisor will appear after sqrt

    :algorithm:
    The algorithm is very simple if you implement first two auxiliary functions:
        find_divisor(_smallest_candidate, _number): returns the smallest divisor and a remainder after division
            starting from _smallest_candidate until sqrt(_number); doesn't include 1 or _number in divisors
        format_output(_divisors): returns the output formated as the problem demands taking as input
            a list with all divisors

    Using these two auxiliary functions the algorithm goes as follows:
    1. Initialize variables (Set-up)
    2. Until there are no more divisors
            run find_divisor() to find smallest_divisor and remainder
            prepare smallest divisor and new_n = remainder for next iteration
    3. After ending iterations add new_n as a divisor (every number is divisible by it-self)
    4. Run format_output() to prepare output as problem demands

    """
    # 1. Set-up
    divisors = []
    smallest_candidate = 2
    new_divisor, new_n = find_divisor(smallest_candidate, _n)

    # 2. Find divisors
    while new_divisor:
        divisors.append(new_divisor)
        smallest_candidate = new_divisor
        new_divisor, new_n = find_divisor(smallest_candidate, new_n)

    # 3. Add remainder as divisor
    divisors.append(int(new_n))

    # 4. Return required string
    return format_output(divisors)


def find_divisor(_smallest_candidate, _number):
    limit = floor(sqrt(_number))  # you only need to check until sqrt(_number)
    s = _smallest_candidate
    for i in range(s, limit+1):
        division_result = _number / i
        if division_result.is_integer():  # if it is a divisor -> save it
            divisor = i
            return divisor, division_result

    # no divisor found
    divisor, division_result = None, _number
    return divisor, division_result


def format_output(_divisors):

    # group divisors in counting dictionary
    _div_count = {}
    for div in _divisors:
        _div_count.setdefault(div, 0)
        _div_count[div] += 1

    # sort divisors removing repetitions
    keys_sorted = sorted(list(set(_div_count)))

    # use dictionary for producing output
    output_string = ''

    for key in keys_sorted:
        value = _div_count[key]
        if value == 1:
            output_string += '(' + str(key) + ')'
        elif value > 1:
            output_string += '(' + str(key) + '**' + str(value) + ')'

    return output_string


# ------------------------------ MAIN CODE ------------------------------
my_n = 7775460
output = prime_factors(7775460)
print(output)
