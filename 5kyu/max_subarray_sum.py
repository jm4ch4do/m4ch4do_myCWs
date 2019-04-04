# ----- Problem: Maximum subarray sum (5ku)
# ----- URL: https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c


def max_subarray_sum(_numbers):
    """
    (list_of_int) -> int
    :param _numbers: list with a sequence of positive and negative ints
    :return: int with sum of the subarray with the maximum possible sum

    :algorithm:
    Find the max of all cells together
        Then find the max sum checking individual cells
        Then find the max sum checking groups of two cells
        Then find the max sum checking groups of three cells
        And so on
        ...
        At the end return the max of all max
            return 0 if max is negative

    :example:
    [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> returns 6 because [4, -1, 2, 1] has the greater sum

    [-7, -28, 0, -7, 26, 29, 9, -18, 28, -2, 0, -25, 3, -3, -2, -16, 13, 17, 7, 25, -21, 15, 26, 25, -6, -1, 16, -15, 8, -14, -8, 27, -17, 18, 19, -16, -14, 18, -27, -2, 8, -6, -13, -6, -25, -7, -28, 2, 6, 29] -> 163

    :interval_var:
    size -> stores the size of the group to be checked (ex. size = 2 means groups like [-2, 1], [1, -3], [-3, 4], ...)

    """
    max_sum_all_sizes = sum(_numbers)  # initial value (max of all cells together)

    for size in range(1, len(_numbers) + 1):
        all_groups = make_groups(_numbers, size)
        max_sum_this_size = find_max_sum(all_groups)
        max_sum_all_sizes = max_sum_this_size if max_sum_this_size > max_sum_all_sizes else max_sum_all_sizes

    return max_sum_all_sizes if max_sum_all_sizes >= 0 else 0


def make_groups(_list, _size):
    """
    (_list, _int) -> _list_of_lists
    :param _list: list with positive and negative ints
    :param _size: int with size of mini_list to be formed every each cell in _list
    :return: list with len(_list) - _int cells
        In each cell of the output list there is a mini_list or group
        Each mini_list has the value of the same cell in _list
            And also _int consecutive values

    :example:
    [-2, 1, -3, 4, -1, 2, 1, 5, 4], 1 -> [-2, 1, -3, 4, -1, 2, 1, 5, 4]
    [-2, 1, -3, 4, -1, 2, 1, 5, 4], 2 -> [[-2, 1], [1, -3], [-3, 4], [4, -1], [-1, 2], [2, 1], [1, 5], [5, 4]]
    """
    _all_mini = []
    for l in range(len(_list)):  # for every cell
        # create a mini_list
        mini_list = []

        # exit before getting out of index error
        if l + _size > len(_list):
            break

        # put _int consecutive values in the mini_list
        for i in range(_size):
            mini_list.append(_list[l+i])

        # save the mini_list to output variable
        _all_mini.append(mini_list)

    return _all_mini


def find_max_sum(_list):
    """
    (list_of_lists) -> int
    :param _list: list with mini_lists in each cell
    :return: Computes the sum of mini_lists in every cell of _list
             Returns the max of all sums

    :example:
    [[-2, 1], [1, -3], [-3, 4], [4, -1], [-1, 2], [2, 1], [1, 5], [5, 4]] -> 9 using last mini_list = [5, 4]
    """
    _max_sum = sum(_list[0])

    for mini_list in _list[1:]:
        new_sum = sum(mini_list)
        _max_sum = new_sum if new_sum > _max_sum else _max_sum

    return _max_sum


my_numbers = [-7, -28, 0, -7, 26, 29, 9, -18, 28, -2, 0, -25, 3, -3, -2, -16, 13, 17, 7, 25, -21, 15, 26, 25, -6, -1, 16, -15, 8, -14, -8, 27, -17, 18, 19, -16, -14, 18, -27, -2, 8, -6, -13, -6, -25, -7, -28, 2, 6, 29]
result = max_subarray_sum(my_numbers)
print(result)
