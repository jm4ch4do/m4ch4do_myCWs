# ----- Problem: Permutations (4kyu)
# ----- URL: https://www.codewars.com/kata/5254ca2719453dcc0b00027d


def my_permutations(_str):
    """
    (string) -> list_of_string
    :param _str: string with a series of characters
    :return: list_of_string where each string is a different permutation of chs in _str

    :examples:
    'a' -> ['a']
    'ab' -> ['ab', 'ba']
    'aabb' -> ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

    :algorithm:
    explained with example _str = 'abc'
        The algo takes the first ch
            'a'
        Then combines it with the second
            'ab', 'ba'
        Then this two are combined with the third
            'cab', 'acb', 'abc', 'cba', 'bca', 'bac'
        And so on

        The rest is just erasing duplicates which is just sorting are erasing if value == previous
    """
    # take the first ch
    pers = [_str[0]]  # permutations
    _str = _str[1:]

    # find permutations for all chs
    for ch in _str:

        # new permutations from current ch
        new_pers = []

        # for every previous permutation (ex. 'ab', 'ba')
        for per in pers:

            # for every position in permutation (ex. for 'ab' positions are 'HEREab', 'aHEREb', 'abHERE')
            for i in range(len(per) + 1):
                new_per = per[:i] + ch + per[i:]  # put ch in position
                new_pers.append(new_per)

        pers = new_pers.copy()  # every character defines a new set of permutations

    # erase duplicate permutations that will appear if _str has repeated characters
    pers.sort()
    pers_no_rep = [pers.pop(0)]
    for value in pers:
        if value != pers_no_rep[-1]:
            pers_no_rep.append(value)

    # return permutations with no repetitions
    return pers_no_rep


# ----- MAIN CODE --------------------------------------------------
my_str = 'aabb'
result = my_permutations(my_str)
print(result)
