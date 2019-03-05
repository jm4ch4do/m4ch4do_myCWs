def string_mix(str1, str2):
    """
    :param str1: string with a given sentence
    :param str2: string with another sentence
    :return: returns the count of lower letters in each string with a given format (see examples)

    :algorithm:
    ("Are the kids at home? aaaaa fffff xx", "Yes they are here! aaaaa fffff xx")
    1. Find amount of letters: Fill 2 dicts with amount of each letter in each string
        (dict1 = {'r': 1, 'e': 3, 't': 2, 'h': 2, 'k': 1, 'i': 1, 'd': 1, 's': '1', 'a': 6, 'o': 1, 'm': 1, 'f': 5, 'x': 2})
        (dict2 = ...)
    2. Erase keys with only 1 occurrence
        (dict1 = {'e': 3, 't': 2, 'h': 2, 'a': 6, 'f': 5, 'x': 2})
        (dict2 = {'e': 5, 'h': 2, 'a': 6, 'r': 2, 'f': 5, 'x': 2})
    3. Search for equal keys in both dict:
            if key has higher number in dict1, erase key in dict 2 and viceversa
            if key has equal number in both dicts, erase from both and add to new dict
        (existing_keys= {'t', 'e', 'r', 'h', 'a', 'f', 'x'})
        (dict1 = {'t': 2})
        (dict2 = {'e': 5, 'r': 2})
        (dict12) = {'h': 2, 'a': 6, 'f': 5, 'x': 2}
    4. Transform dict into lists_of_tuples ('letter, occurrences, dict')
        (list1 = [('t', 2, '1:')]
        (list2 = [('r', 2, '2:'), ('r', 5, '2:')]
        (list3 = [('a', 6, '=:'), ('h', 2, '=:'), ('x', 2, '=:'), ('f', 5, '=:')])
    5. Concat lists and sort by field 1, then field 2 and then field 0
        (final_list = [('a', 6, '=:'), ('e', 5, '2:'), ('f', 5, '=:'), ('t', 2, '1:'), ('r', 2, '2:'), ('h', 2, '=:'), ('x', 2, '=:')])
    6. Create final string
    ("=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh/=:xx")

    :examples:
    >> s1 = "Are the kids at home? aaaaa fffff xx"
    >> s2 = "Yes they are here! aaaaa fffff xx"
    >> mix(s1, s2)
    "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh/=:xx"
    # this means
        (The max of 'a's is in both strings with 6 'a's)
        (The max of 'e's is in string 2 with 5 'e's)
        (The max of 'f's is in both strings with 5 'a's) ('f' goes after 'e' for sorting 1,2,:)
        (The max of 't's is in string 1 with 2 't's)
        (The max of 'r's is in string 2 with 2 'r's) ('r' goes after 't' for sorting 1,2,:)
        (The max of 'h's is in both strings with 2 'h's) ('h' goes after 'r' for sorting 1,2,:)
        (The max of 'x's is in both strings with 2 'x's) ('x' goes after 'h' for sorting alphabetically)
        ((note that max = 1 is not taken into account))

    """

    # 1. Find amount of letters
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'

    dict1 = {}
    for ch in str1:
        if ch in lower_letters:
            dict1.setdefault(ch, 0)  # initialize key with 0 with doesn't exits
            dict1[ch] += 1

    dict2 = {}
    for ch in str2:
        if ch in lower_letters:
            dict2.setdefault(ch, 0)  # initialize key with 0 with doesn't exits
            dict2[ch] += 1

    # 2. Erase keys with only 1 occurrence
    dict1_ok = {}
    for key in dict1.keys():
        if dict1[key] > 1:
            dict1_ok[key] = dict1[key]
    dict1 = dict1_ok

    dict2_ok = {}
    for key in dict2.keys():
        if dict2[key] > 1:
            dict2_ok[key] = dict2[key]
    dict2 = dict2_ok

    # 3. Search for equal keys and erase the one with lower value
    # (same value goes to new dict)

    # get keys from both dict
    keys_with_repetitions = list(dict1.keys())
    keys_with_repetitions.extend(list(dict2.keys()))
    existing_keys = set(keys_with_repetitions)

    dict1_ok, dict2_ok = {}, {}
    dict3 = {}
    for key in existing_keys:
        if dict1.get(key, 1) > dict2.get(key, 1):  # returns 1 if key doesn't
            dict1_ok[key] = dict1[key]
        elif dict2.get(key, 1) > dict1.get(key, 1):
            dict2_ok[key] = dict2[key]
        else:
            dict3[key] = dict1[key]
    dict1 = dict1_ok
    dict2 = dict2_ok

    # 4. Transform dicts into lists_of_tuples
    list1, list2, list3 = [], [], []
    [list1.append((item[0], item[1], '1:')) for item in dict1.items()]
    [list2.append((item[0], item[1], '2:')) for item in dict2.items()]
    [list3.append((item[0], item[1], '=:')) for item in dict3.items()]

    # 5. Concat list_of_tuples and sort
    final_list = list1
    final_list.extend(list2)
    final_list.extend(list3)

    # sorting by field1(reverse), field2(list_based) and field0
    def my_sort(x):  # user_sort_function
        comp1 = -x[1]  # inverse sort

        ref_list = ['1:', '2:', '=:']  # reference list for sorting
        comp2 = [i for i, value in enumerate(ref_list) if x[2] == value]
        comp2 = comp2[0]  # list_based sort

        comp3 = x[0]  # regular sort
        return comp1, comp2, comp3

    final_list.sort(key=my_sort)

    # 6. Create final string
    final_string = ''
    for i, value in enumerate(final_list):
        final_string += '' if i == 0 else '/'  # separator between elements but missing at the beginning
        tuple_string = value[2] + value[0]*value[1]  # from ('a',6,'=:') make '=:aaaaaa'
        final_string += tuple_string

    return final_string
