# ----- Problem: Common Denominators (5ku)
# ----- URL: https://www.codewars.com/kata/54d7660d2daf68c619000d95
from math import floor, sqrt


# WORKS FINE, BUT SLOW FOR HUGE NUMBERS -------------------------
def find_common_den(_fracs):
    """
    (list_of_duplets) -> list_of_duplets
    :param _fracs: list_of_duplets with a fraction in each duplet
    :return: list_of_duplets with every fraction with a common denominator

    :examples:
    [(2, 4), (3, 9), (20, 80)] -> [(6, 12), (4, 12), (3, 12)]

    :helper_functions:
    divisors(int) -> returns list with all divisors for int

    :algorithm:
        _fracs = [(2, 4), (3, 9), (20, 80)]
    1. Simplify individually every fraction in _fracs
        red_fracs = [(1, 2), (1, 3), (1, 4)]
    2. Find common_denominator
        denominators = [2, 3, 4]
        max = 4
        max*2 = 8 (not divisible by 3)
        max*3 = 12 (ok)
        common_den = 12
    3. Expand every faction using common_den
        exp_fracs = [(6, 12), (4, 12), (3, 12)]

    """

    # 0. Dummy input
    if not _fracs:
        return None

    # 1. Simplify individually every fraction in _fracs
    red_fracs = []  # reduced_fractions
    for frac in _fracs:
        num, den = frac[0], frac[1]

        # Divide num and den by highest common divisor while there is common
        common_div = 1  # ini value to enter while
        while common_div:
            num /= common_div
            den /= common_div
            num_div, den_div = find_divisors(num), find_divisors(den)
            common_div = find_highest_common(num_div, den_div)

        new_fraction = int(num), int(den)
        red_fracs.append(new_fraction)

    red_fracs = _fracs

    # 2. Find common_denominator
    denominators = [value[1] for value in red_fracs]
    highest = max(denominators)

    multiplier = 0
    done = False
    while not done:
        multiplier += 1
        candidate = highest * multiplier
        for den in denominators:
            done = True  # assume you are done
            if candidate % den:  # if not divisible, you are not done -> change multiplier multiplying
                done = False
                break
            else:
                continue         # if divisible -> keep checking with the other denominators

    common_den = candidate

    # 3. Expand every faction using common_den
    exp_fracs = []
    for frac in red_fracs:
        num, den = frac[0], frac[1]
        new_den = common_den
        new_num = int(common_den / den * num)
        exp_fracs.append((new_num, new_den))

    return exp_fracs


def find_highest_common(list1, list2):
    """
    Finds highest common number in both lists
    """

    # use shorter list for searching
    if len(list1) <= len(list2):
        shorter, longer = list1, list2
    else:
        shorter, longer = list2, list1

    hcommon = 0
    for value in shorter:
        if value in longer and value > hcommon:
            hcommon = value

    return hcommon if hcommon else None


def find_divisors(_number):
    """
    :description:
    Find divisors without including 1
    """
    divs = []
    limit = floor(sqrt(_number))  # you only need to check until sqrt(_number)
    for i in range(2, limit + 1):
        division_result = _number / i
        if division_result.is_integer():  # if it is a divisor -> save it
            divs.append(i)
            if division_result != i:  # save pair if not equal (ex. for 25 there is no need to save 5 two times)
                divs.append(int(division_result))

    # the number itself it always its own divisor so it should be included if it wasn't already include
    # (ex. for 2 it will be already included because 'for' gets to limit + 1 = 2, but for other number it won't)
    if not divs or divs[-1] != _number:
        divs.append(_number)

    return divs


# ---------------------------------------------------------------


# ALGO FOR HUGE NUMBERS -----------------------------------------
def find_common_den_huge(_fracs):
    """
    :examples:
    [[27115, 5262], [87546, 11111111], [43216, 255689]]
    -> [[77033412951888085, 14949283383840498], [117787497858828, 14949283383840498], [2526695441399712, 14949283383840498]]

    :algorithm:
    For two positive integers a, b gcd(a,b)lcm(a,b)=ab
    So.
        1. Find gcd
        2. Get lcm = ab/gcd

    """
    # 0. Dummy input
    if not _fracs:
        return []

    # 1. Get denominators from input
    denominators = [value[1] for value in _fracs]
    denominators.sort()
    a = denominators.pop()

    # 2. Find lcm two denominators at the time
    while denominators:
        b = denominators.pop()
        a = lcm(a, b)

    common = a

    # 3. Expand every faction using common_den
    exp_fracs = []
    for frac in _fracs:
        num, den = frac[0], frac[1]
        new_den = common
        new_num = int(common // den * num)
        exp_fracs.append([new_num, new_den])

    return exp_fracs


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)

# ---------------------------------------------------------------


# ------------------------- MAIN CODE -------------------------
my_fracs = [(1, 2), (1, 3), (1, 4)]
expected = [(6, 12), (4, 12), (3, 12)]
result = find_common_den(my_fracs)
print(result)

my_fracs = [[77033412951888085, 14949283383840498], [117787497858828, 14949283383840498], [2526695441399712, 14949283383840498]]
result = find_common_den_huge(my_fracs)
print(result)
