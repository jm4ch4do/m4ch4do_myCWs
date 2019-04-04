# ----- Problem: Weight for weight (5ku)
# ----- URL: https://www.codewars.com/kata/55c6126177c9441a570000cc


def sort_by_sum(_numbers):
    """
    (string) -> string
    :param _numbers: string with a series of ints separated by one or multiple spaces
    :return: string with ints from _numbers sorted according to:
                1. sum of it digits (ex. 100 will take 1 for sorting, and 180 will have 9)
                2. if equal sum sort like a string (ex. 180 will go before 90 and before 9)

    :example:
    "56 65 74 100 99 68 86 180 90" -> "100 180 90 56 65 74 68 86 99"
    """
    # extract number that may be separated by one or multiple spaces
    list_num = extract_num(_numbers)

    # use sorting function
    list_num.sort(key=my_sort)

    return ' '.join(list_num)


def extract_num(_numbers):
    """
    (string) -> list
    :param _numbers: string with a series of ints separated by one or multiple spaces
    :return: list with ints from _numbers

    :example:
    "56 65 74 100 99 68 86 180 90" -> [100, 180, 90, 56, 65, 74, 68, 86, 99]
    """
    # put a space at the end for the algorithm to work properly
    _numbers += ' '

    # initialize
    previous, string = ' ', ''
    _list_num = []

    # check every character and save ints to output list
    for ch in _numbers:
        if ch == ' ' and previous == ' ':  # ignore several spaces
            continue
        elif ch != ' ' and previous == ' ':  # start word when letter appears after space
            string = ch
        elif ch != ' ' and previous != ' ':  # continue word when letter appears after letter
            string += ch
        elif ch == ' ' and previous != ' ':  # end word when spaces appears after letters
            _list_num.append(string)

        previous = ch

    return _list_num


def my_sort(x):
    """
    (string) -> (tuple)
    :param x: every cell of the list which is going to be sorted
    :return: tuple with first sorting criteria and second sorting criteria

    :description:
    This is a typical python sorting function.
        It sort first by the sum of the elements in the int(passed as string)
        The sorts like an string(see description of main function)
    """
    sort1 = 0
    for ch in x:
        sort1 += int(ch)

    sort2 = x

    return sort1, sort2


my_numbers = "     56 65 74 100    99 68  86 180 90"
expected = "100 180 90 56 65 74 68 86 99"
result = sort_by_sum(my_numbers)
print(result == expected)
