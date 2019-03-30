# ----- Problem: Number of trailing zeros of N! (5ku)
# ----- URL: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34


def trailing_zeros_factorial(_n):
    """
        (int) -> (int)
        :param _n: int for computing factorial
        :return: int with amount of zeros to the right after computing factorial

        :example:
        !0 = 1 => returns 0
        !6 = 720 => returns 1
        !12 = 479001600 => returns 2

        :description:
        To avoid computing the factorial, a method is need for estimating the amount of zeros.
            in this site you can find such a method: http://mathworld.wolfram.com/Factorial.html
            so this script just uses the method which includes a sum and log among other things
    """
    # Initialize result
    count = 0

    # Keep dividing n by
    # powers of 5 and
    # update Count
    i = 5
    while _n / i >= 1:
        count += int(_n / i)
        i *= 5

    return int(count)


print(trailing_zeros_factorial(30))
