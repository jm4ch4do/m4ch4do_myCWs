# ----- Problem: Gap in Primes (5ku)
# ----- URL: https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4
from math import sqrt


def find_gap(_gap, _s, _e):
    """
    (int, int, int) -> list_of_2ints
    :param _gap: int with gap size we are looking for
    :param _s: int with start of search
    :param _e: int with end of search
    :return: First pair of primer numbers separated by _gap between _s and _e

    :description:
    gap = distance(difference) between number

    :examples:
    find_gap(2, 5, 7) -> (5, 7)
    find_gap(2, 5, 5) -> None
    find_gap(4, 130, 200) -> (163, 167)

    :algorithm:
    Create auxiliary function that verifies if number is prime: is_prime()

    for every number between _s and _e
        If number is_prime()
            Find difference with previous_prime
            Return both primes if difference == gap
    """
    # dummy case
    if _s == _e:
        return None

    # check numbers in given range
    previous = None
    for num in range(_s, _e + 1):
        if is_prime(num):

            # store first prime
            if not previous:
                previous = num
                continue

            # check if gap was found
            dif = num - previous
            if dif == _gap:
                return previous, num
            else:
                previous = num

    # if no good pair of primes was found -> return None
    return None


def is_prime(_num):
    for n in range(2, int(sqrt(_num)) + 1):  # only need to check until sqrt
        if not _num % n:  # if finds divisor
            return False

    # return True if no divisor was found (ie. a prime is a number with no divisors)
    return True


# ------------------------- MAIN CODE -------------------------
result = find_gap(2, 5, 7)  # (5, 7)
# result = find_gap(2, 5, 5)  # None
# result = find_gap(4, 130, 200)  # (163, 167)
print(result)
