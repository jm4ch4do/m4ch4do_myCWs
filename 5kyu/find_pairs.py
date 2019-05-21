# ----- Problem: Is my friend cheating? (5ku)
# ----- URL: https://www.codewars.com/kata/5547cc7dcad755e480000004
from math import sqrt, floor


# too slow
def find_pairs(_n):
    """
    :param _n: int with limit
    :return: after sum from 1 to _n find pairs whose multiplication is equal to _sum - pairs

    :examples:
    (26) -> [(15, 21), (21, 15)]
        sum(26)
        > 315
        15*21
        > 351  (total)
        351 - 15 - 21
        > 315

    (100) -> []

    (101) -> [(55, 91), (91, 55)]
    """
    # SET-UP
    output = []
    values_all = list(range(_n, 0, -1))  # decreasing values from requested number to 1
    total = sum(values_all)
    the_sqrt = int(floor(sqrt(total)))
    values_sqrt = list(range(1, the_sqrt))  # values from 0 to the root of requested number

    # find values that meet criteria
    for value1 in values_sqrt:
        for value2 in values_all:
            product = value1 * value2
            reference = total - value1 - value2

            # product too high -> keep testing with lower numbers for value2
            if product > reference:
                continue

            # product too low -> the remaining value2 will all be lower -> start with another value1
            if product < reference:
                break

            # product equal to reference -> save pair that meets criteria and get another value1
            if product == reference:
                output.append((value1, value2))

    # copy reverse values (ie. if (15, 21) is a solution then (21, 15) it's a solution as well )
    [output.append((value[1], value[0])) for value in reversed(output)]

    # return
    return output


# faster using algebra
def find_pairs2(_n):
    """
    The trick is you can remove the inner loop because for every value1 you can find value2 using algebra
    The problem states that
        x * y = total - x - y
    after a little algebra
        y = (total - x)/(x + 1)
    So, if you assume x you can quickly find y

    """
    # SET-UP
    output = []
    values_all = list(range(_n, 0, -1))  # decreasing values from requested number to 1
    total = sum(values_all)
    the_sqrt = int(floor(sqrt(total)))
    values_sqrt = list(range(1, the_sqrt))  # values from 0 to the root of requested number

    # find values that meet criteria
    for x in values_sqrt:
        y = (total - x)/(x + 1)
        if y.is_integer() and y < _n:
            output.append((x, y))

    # copy reverse values
    [output.append((value[1], value[0])) for value in reversed(output)]

    return output


# ----- MAIN CODE --------------------------------------------------
my_n = 26
result = find_pairs2(my_n)
print(result)
