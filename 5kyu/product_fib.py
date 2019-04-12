# ----- Problem: Product of consecutive Fib numbers (5ku)
# ----- URL: https://www.codewars.com/kata/5541f58a944b85ce6d00006a


def product_fib(_candidate):
    """
    (int) -> (int, int, boolean)
    :param _candidate: int that may have resulted from finding the product of two fibonacci consecutive numbers
    :return: Two connectives fibonacci ints whose product is equal or inmediately superior to _candidate
             True if it was equal (i.e. the candidate was a truly product of two consecutive fibs)

    :examples:
    productFib(714) -> [21, 34, true]
    productFib(800) -> [34, 55, false]

    """
    # initial fib set-up
    fib1 = [0]
    fib2 = [1]

    # keep computing fib until you get to _candidate
    while True:

        # get two new fibs and find their product
        product = iterate_fib(fib1, fib2)

        # stop criteria
        if product == _candidate:  # _candidate match -> return True
            return [fib1[0], fib2[0], True]
        elif product > _candidate:  # _candidate surpassed -> return False
            return [fib1[0], fib2[0], False]


def iterate_fib(_fib1, _fib2):
    _fib1[0], _fib2[0] = _fib2[0], _fib1[0] + _fib2[0]
    _product = _fib1[0] * _fib2[0]
    return _product


my_candidate = 714
result = product_fib(my_candidate)
print(result)
