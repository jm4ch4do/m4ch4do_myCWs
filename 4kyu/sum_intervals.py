# ----- Problem: Sum of intervals(4kyu)
# ----- URL: https://www.codewars.com/kata/52c4dd683bfd3b434c000292


def sum_intervals(_intervals):
    """
    (list_of_duplets_of_int) -> (int)
    :param _intervals: list_of_duplets where each duplet is an interval
    :return: The length of all interval after being overlap

    :examples:
    [[1, 4], [7, 10], [3, 5]] -> 7 because [1, 4] overlaps with [3, 5] making [1, 5] which has len = 4
    [[1, 2], [6, 10], [11, 15]] -> 9
    [[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]

    """
    # sort by duplet_1 so every duplet may form an interval only with next
    _intervals.sort(key=lambda x: x[0])

    # set-up
    last_len = 0
    new_intervals = []
    skip_next = False

    # overlap every duplet with adjacent if possible until there are no more duplet to overlap
    while last_len != len(_intervals):

        # check if duplet may be overlapped with next_duplet
        for i, duplet in enumerate(_intervals):

            # if duplet was already overlapped with previous -> skip
            if skip_next:
                skip_next = False
                continue

            # if duplet is last in _intervals -> save
            if i == len(_intervals) - 1:
                new_intervals.append(duplet)
                continue

            # save next_duplet for latter comparison
            next_duplet = _intervals[i + 1]

            # if duplet doesn't overlap with next_duplet -> save duplet
            if duplet[1] < next_duplet[0]:
                new_intervals.append(duplet)
                continue

            # if duplet overlaps with next_duplet -> save both as overlap
            else:
                overlapped_duplet = [duplet[0], max(duplet[1], next_duplet[1])]
                new_intervals.append(overlapped_duplet)
                skip_next = True  # next duplet was already included as overlap

        # set-up for next iteration
        skip_next = False
        last_len = len(_intervals)
        _intervals = new_intervals
        new_intervals = []

    # sum individual length of each overlapped duplet
    sum_len = 0
    for dup in _intervals:
        sum_len += dup[1] - dup[0]

    # return len of duplets that were overlapped
    return sum_len


# ----- MAIN CODE --------------------------------------------------
my_intervals = [[1, 2], [6, 10], [11, 15]]
result = sum_intervals(my_intervals)
print(result)
