# ----- Memorized Fibonacci (5ku)
# ----- URL: https://www.codewars.com/kata/529adbf7533b761c560004e5
from functools import lru_cache


@lru_cache()
def memorized_fib(_n):
    """
    (int) -> (int)
    :param _n: int with a number asking for its fib
    :return: int with the fib result using memorization

    :description:
    Traditional fibonacci uses recursion and is very slow because every sequence has to be computed from the start,
    so it best to use memorization which means storing previously calculated values.
    Memorization can be explicit which means than you use a global variable external to the function or
    Implicit which uses a python decorator

    For this problem:
        memorized_fib is the implicit solution
        memorized_fib2 is the explicit solution
    """
    return memorized_fib(_n - 1) + memorized_fib(_n - 2) if _n not in (0, 1) else 1


fib_cache = {}
def memorized_fib2(_n):
    # if the value is cached, then return it
    if _n in fib_cache:
        return fib_cache[_n]

    # compute the nth term
    value = memorized_fib(_n - 1) + memorized_fib(_n - 2) if _n not in (0, 1) else 1

    # cache the computed value and return it
    fib_cache[_n] = value
    return value


my_n = 318
result = memorized_fib(my_n)
print(result)
