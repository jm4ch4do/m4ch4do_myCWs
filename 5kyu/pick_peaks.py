# ----- Problem: Pick Peaks (5ku)
# ----- URL: https://www.codewars.com/kata/5279f6fe5ab7f447890006a7


def pick_peaks(_signal):
    """
    (list_of_int) -> (list_of_int, list_of_int)
    :param _signal: list with positive ints representing a signal that goes up and down
    :return _pos: list with ints representing the positions where the local max occur
    :return _peaks: list with ints representing the value of the local max

    :example:
    [3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3, 3, 3, 4, 5, 5, 5, 3, 4] -> [3, 7, 15], [6, 3, 5]

    :description:
    In the flat region [2 3 3 3 4] there is no max
    In the flat region [4 5 5 5 3] the max is the first 5
    Extremes are never considered as max

    """
    # set-up
    _pos = []  # output list
    _peaks = []  # output list
    previous = -1  # previous signal for comparison
    candidate = None  # there is no initial max_candidate

    # check every sample in the _signal
    for i, sample in enumerate(_signal):

        # ignore first sample
        if i == 0:
            previous = sample
            continue

        # perform action depending on signal change
        if sample > previous:  # on signal increase -> set max_candidate
            candidate = (i, sample)
        elif sample == previous:  # in flat region -> maintain candidate
            pass
        elif sample < previous:  # on signal decrease -> save and delete candidate if exist
            if candidate:
                _pos.append(candidate[0])
                _peaks.append(candidate[1])
                candidate = None
            else:  # there is nothing to be done when the signal keeps decreasing
                pass

        # save sample for later comparison
        previous = sample

    # return output lists
    return {"pos": _pos, "peaks": _peaks}


my_signal = [3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3, 3, 3, 4, 5, 5, 5, 3, 4]

result = pick_peaks(my_signal)
print(result)
