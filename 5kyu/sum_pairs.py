# ----- Problem: Sum of Pairs (5ku)
# ----- URL: https://www.codewars.com/kata/54d81488b981293527000c8f


def sum_pairs(_candidates, _target_sum):
    """
    (list_of_int, int) -> (list_of_2int)
    :param _candidates: list of pos and neg ints
    :param _target_sum: int with a reference sum value
    :return: list_of_2int with first pair than sums = _target_sum

    :internal_vars:
        brother: int which is necessary to make sum = _target_sum for a given value

    :internal_vars:
        brother: int which is necessary to make sum = _target_sum for a given value
                (ie. candidate + brother = _target_sum)

    :algorithm:
        .For every candidate find its brother and save it in brothers
            .If a candidate is in brothers -> you are done because you found the closest pair

        .Return None if no candidate was someones brother


    :examples:
    ([11, 3, 7, 5], 10)       -> [3, 7]
    ([4, 3, 2, 3, 4], 6)      -> [4, 2]
    ([0, 0, -2, 3], 2)        -> None
    ([10, 5, 2, 3, 7, 5], 10) -> [3, 7]
    ([1, 4, 8, 7, 3, 15], 8)  -> [1, 7]
    """

    brothers = set()
    for candidate in _candidates:
        # find brother for this _candidate
        brother = _target_sum - candidate

        # compare with brothers
        if candidate in brothers:  # if candidate is in brothers -> you found the closest [candidate, brother] pair
            return [_target_sum - candidate, candidate]
        else:  # brother not in brothers -> store for later comparison
            brothers.update([brother])

    # return None if all _candidates were checked and there was no brother
    return None


my_candidates = [1, 4, 8, 7, 3, 15]
my_target_sum = 8
result = sum_pairs(my_candidates, my_target_sum)
print(result)
