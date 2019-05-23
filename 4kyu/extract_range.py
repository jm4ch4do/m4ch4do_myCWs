# ----- Problem: Range Extraction (4kyu)
# ----- URL: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f


def extract_range(_nums):
    """
    (list_of_int) -> (string)
    :param _nums: list_of_int with sorted negative and positive integers
    :return: string with a reduced notation of numbers
             three or more consecutive numbers like [1, 2, 3] will be "1-3"
             two consecutive numbers like [1, 2] will be "1, 2"
             no consecutive numbers like [1, 3] will be "1, 3"

    :example:
    [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
    -> "-6, -3-1, 3-5, 7-11, 14, 15, 17-20"
    """
    # set-up
    output = []
    previous = [_nums[0]]

    # check every number for creating reduced notation
    for num in _nums[1:]:

        # no previous stored -> append to previous
        if not previous:
            previous = [num]

        # previous is -1 lower -> append to previous
        elif previous[-1] + 1 == num:
            previous.append(num)

        # previous is far from num -> previous to output, and previous = num
        else:
            output.append(make_range(previous))
            previous = [num]

    # save last previous after ending loop
    output.append(make_range(previous))

    return ', '.join(output)


def make_range(_num_list):
    """
    turns a list_of_ints into a reduce notation
    :example:
    [1] -> '1'
    [1,2] -> '12'
    [1,2,3] -> '123'
    """
    if len(_num_list) == 1:
        out_str = str(_num_list[0])

    elif len(_num_list) == 2:
        out_str = str(_num_list[0]) + ', ' + str(_num_list[1])

    else:
        out_str = str(_num_list[0]) + '-' + str(_num_list[-1])

    return out_str

# ---- MAIN CODE ------------------------------------------------------------
my_nums = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
result = extract_range(my_nums)
print(result)
