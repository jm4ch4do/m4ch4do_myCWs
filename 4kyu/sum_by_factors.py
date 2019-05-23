# ----- Problem: Sum by Factors (4kyu)
# ----- URL: https://www.codewars.com/kata/54d396788776e49e6b00052f
from math import floor, sqrt


def sum_by_factors(_nums):
    """
    (list_of_ints) -> (list_of_duplets_of_int)
    :param _nums: list of pos and neg ints
    :return: duplet[0] = prime of a num in _nums
             duplet[1] = sum of all _nums for which it's a prime

    :auxiliary functions:
    find_divisors -> returns all divisors for a given number
    is_prime -> returns True if a number is prime

    :example:
    [12, 15] -> [[2, 12], [3, 27], [5, 15]]
                where 2 is prime divisor of 12
                      3 is prime divisor of 12 and 15
                      5 is prime divisor of 15

    """

    # check every number for prime divisors
    primes_by_num = {}
    for num in _nums:
        primes = []

        # find divisors for pos and neg numbers
        if num > 0:
            divs = find_divisors(num)
        else:
            divs = find_divisors(-num)

        # find prime divisors
        if divs:
            for div in divs:
                if is_prime(div):
                    primes.append(div)

        # sum nums for each prime
        if primes:
            for prime in primes:
                primes_by_num.setdefault(prime, 0)
                primes_by_num[prime] += num

    # create output string
    output = []
    for key, value in primes_by_num.items():
        output.append([key, value])

    return sorted(output, key=lambda x: x[0])


def find_divisors(_number):
    divs = []
    limit = floor(sqrt(_number))  # you only need to check until sqrt(_number)

    # find divisors checking every number lower that limit
    for i in range(2, limit + 1):
        division_result = _number / i

        # if it is a divisor -> save it
        if division_result.is_integer():
            divs.append(i)

            # save pair if not equal (ex. for 25 there is no need to save 5 two times)
            if division_result != i:
                divs.append(int(division_result))

    # every number can be divided by itself
    divs.append(_number)
    return divs


def is_prime(_int):
    """
    idem to find_divisors, but this one stops after finding the first divisor
    """

    limit = floor(sqrt(_int))

    for i in range(2, limit + 1):
        division_result = _int / i

        # if it is a divisor -> then is not a prime
        if division_result.is_integer():
            return False

    # no divisor found -> return True
    return True


# ----- MAIN CODE --------------------------------------------------
my_nums = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
result = sum_by_factors(my_nums)
print(result)
