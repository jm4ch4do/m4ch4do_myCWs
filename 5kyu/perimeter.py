def perimeter(_n):
    """
    (int) -> (int)
    :param _n: int with fib order
    :return: int with sum(fib) * 4

    :description:
    Is an application of the Fibonacci sequence,
    so its basically just computing Fib in a list

    :example:
    perimeter(5) -> 80
    perimeter(7) -> 216
    """

    # compute fibonacci
    fib = make_fib(_n)

    # multiply by 4
    return sum(fib) * 4


# fib using list
def make_fib(_m):
    output = [1, 1]
    for i in range(_m-1):
        output.append(output[-1] + output[-2])

    return output
