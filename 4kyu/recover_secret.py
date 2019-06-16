# ----- Problem: Recover a secret string from random triplets (4kyu)
# ----- URL: https://www.codewars.com/kata/recover-a-secret-string-from-random-triplets/train/python


# --------------------------------------------------------------------------------------------------------------------
#   PURPOSE
# --------------------------------------------------------------------------------------------------------------------
# FIND A SECRET WORD FROM A LIST WITH TRIPLETS (tuple with three fields)
# Every triplet has 3 letters that may not be consecutive in the secret_word(_sw) but are always sorted same as in _sw
# You must find the secret word by drawing conclusions from these triplets


# --------------------------------------------------------------------------------------------------------------------
#   MAIN FUNCTION
# --------------------------------------------------------------------------------------------------------------------
def recover_secret(_triplets):
    """
    (list_of_triplets) -> (string)
    :param _triplets: list like [('t', 'u', 'p'), ('w', 'h', 'i'), ('t', 's', 'u'),...]
    :return _sw: string with secret word

    :algorithm:
    STEP 1: Create a dictionary with key = every_ch_in_all_triplets
                                     value1 = chs_before_key, value2 = chs_after_key
    for the example where _sw = 'whatisup' the dict will look like this:
        before_and_after = {
            t: ('am','sfhi'),
            s: ('tahim','fun'),
            f: ('tsmahi','un'),
            a: ('m','sufinth'),
            u: ('asmf','n'),
            m: ('','afuhtsn'),
            i: ('ath','nfs'),
            n: ('aisufhm',''),
            h: ('atm','ifsn')
        }

    STEP 2: initialize a list with one cell for every ch storing None in each cell
        _sw = [None, None, None, None, None, None, None, None, None]

    STEP 3: Keep going until there are 1 or less Nones in _sw
        find the key that has no other character before ('m')
        add 'm' to the start of _sw
        remove key 'm' from dict and ch 'm' from values of other keys

        find the key that has no other character after ('n')
        add 'n' to the end of _sw
        remove key 'n' from dict and ch 'n' from values of other keys

    STEP 4: Return string version of _sw
    """

    # 1. Create dict with chs before_and_after every character
    before = {}
    after = {}
    for triplet in _triplets:
        l, m, r = triplet[0], triplet[1], triplet[2]  # left, middle, right

        # after 'left' put middle and right
        before.setdefault(l, '')
        after.setdefault(l, '')
        after[l] += m if m not in after[l] else ''
        after[l] += r if r not in after[l] else ''

        # before 'middle' put 'left', after 'middle' put right
        before.setdefault(m, '')
        after.setdefault(m, '')
        before[m] += l if l not in before[m] else ''
        after[m] += r if r not in after[m] else ''

        # before 'right' put left and middle
        before.setdefault(r, '')
        after.setdefault(r, '')
        before[r] += l if l not in before[r] else ''
        before[r] += m if m not in before[r] else ''

    # 2. Initialize output string as list
    _sw = [None] * len(before)

    # 3. Add letters to _sw until all spaces all covered
    front = True  # a letter will be placed once at front(left) of _sw and once at back(right) of _sw
    while None in _sw:

        # last letter to be placed -> goes to the only empty space
        if len(before) == 1:
            remaining_key = list(before.keys())[0]
            for i, value in enumerate(_sw):
                if value is None:
                    _sw[i] = remaining_key

        # try putting a letter in the front of _sw
        elif front:
            for key, value in before.items():

                # found ch with no other chs before -> it goes to the first not_empty cell in _sw starting from the left
                if not value:
                    for i, sch in enumerate(_sw):  # sch = secret_character
                        if not sch:
                            _sw[i] = key
                            remove_ch(key, before), remove_ch(key, after)
                            break
                    break

        # try putting a letter in the back of _sw
        elif not front:
            for key, value in after.items():

                # found ch with no other chs after -> it goes to the first not_empty cell in _sw starting from the right
                if not value:
                    for i in range(len(_sw)):  # sch = secret_character
                        inv_i = len(_sw) - 1 - i  # inverted i = i starting from the end
                        sch = _sw[inv_i]

                        if not sch:
                            _sw[inv_i] = key
                            remove_ch(key, before), remove_ch(key, after)
                            break
                    break

        # a letter will be placed once at front(left) of _sw and once at back(right) of _sw
        front = False if front else True

    # 4. Return string version of _sw
    return ''.join(_sw)


# --------------------------------------------------------------------------------------------------------------------
#   AUXILIARY FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------
def remove_ch(_ch, _dict):
    """
    removes _ch from keys of _dict
    also removes _ch from strings stored as value of _dict
    doesn't return anything
    """

    # remove _ch from keys of _dict
    for key in _dict.keys():
        if key == _ch:
            _dict.pop(key)
            break

    # remove _ch from any string stored as value of _dict
    for key, value in _dict.items():
        if _ch in value:
            pos = value.index(_ch)  # pos = position
            new_string = value[:pos] + value[pos+1:]
            _dict[key] = new_string


# --------------------------------------------------------------------------------------------------------------------
#   TEST SAMPLES
# --------------------------------------------------------------------------------------------------------------------


# ----- EXAMPLE 1 -----
# mytriplets = [ ['t', 'u', 'p'],
#     ['w', 'h', 'i'],
#     ['t', 's', 'u'],
#     ['a', 't', 's'],
#     ['h', 'a', 'p'],
#     ['t', 'i', 's'],
#     ['w', 'h', 's']
# ]
# result = recover_secret(mytriplets)  # 'whatisup'
# ---------------------


# ----- EXAMPLE 2 -----
# mytriplets = [['g', 'a', 's'], ['o', 'g', 's'], ['c', 'n', 't'], ['c', 'o', 'n'], ['a', 't', 's'], ['g', 'r', 't'], ['r', 't', 's'], ['c', 'r', 'a'], ['g', 'a', 't'], ['n', 'g', 's'], ['o', 'a', 's']]
# result = recover_secret(mytriplets)  # 'congrats'
# ---------------------


# ----- EXAMPLE 3 -----
# mytriplets = [['t', 's', 'f'], ['a', 's', 'u'], ['m', 'a', 'f'], ['a', 'i', 'n'], ['s', 'u', 'n'], ['m', 'f', 'u'], ['a', 't', 'h'], ['t', 'h', 'i'], ['h', 'i', 'f'], ['m', 'h', 'f'], ['a', 'u', 'n'], ['m', 'a', 't'], ['f', 'u', 'n'], ['h', 's', 'n'], ['a', 'i', 's'], ['m', 's', 'n'], ['m', 's', 'u']]
# result = recover_secret(mytriplets)  # 'mathisfun'
# ---------------------


# ----- EXAMPLE 4 -----
# mytriplets = [['l', 'e', 'd'], ['o', 'e', 'd'], ['o', 'l', 'e'], ['o', 'v', 'e'], ['s', 'o', 'l'], ['s', 'e', 'd'], ['s', 'l', 'e'], ['v', 'e', 'd'], ['o', 'l', 'v'], ['l', 'v', 'd']]
# result = recover_secret(mytriplets)  # 'solved'
# ---------------------


# ----- EXAMPLE 5 -----
mytriplets = [['o', 'x', 'y'], ['h', 'r', 'u'], ['b', 'x', 'z'], ['r', 'y', 'z'], ['v', 'y', 'z'], ['v', 'w', 'y'], ['o', 's', 'y'], ['i', 'u', 'z'], ['q', 'y', 'z'], ['k', 'p', 'v'], ['w', 'x', 'z'], ['k', 'x', 'y'], ['r', 'w', 'x'], ['a', 'n', 'w'], ['b', 'd', 't'], ['p', 'u', 'y'], ['n', 'v', 'z'], ['f', 'k', 'q'], ['i', 'm', 'z'], ['a', 'w', 'y'], ['b', 'k', 'n'], ['t', 'u', 'w'], ['x', 'y', 'z'], ['f', 'g', 'j'], ['n', 'y', 'z'], ['s', 'y', 'z'], ['k', 'w', 'x'], ['m', 's', 'u'], ['h', 'i', 's'], ['q', 'w', 'z'], ['w', 'y', 'z'], ['j', 'o', 'p'], ['r', 'v', 'y'], ['h', 'p', 'w'], ['s', 't', 'z'], ['j', 'k', 'r'], ['n', 'u', 'w'], ['h', 'v', 'w'], ['t', 'u', 'y'], ['l', 'q', 'y'], ['v', 'w', 'x'], ['r', 'w', 'z'], ['m', 'o', 'w'], ['k', 'q', 'x'], ['e', 'h', 'r'], ['e', 'k', 'l'], ['d', 'h', 'p'], ['r', 'u', 'w'], ['e', 'g', 'n'], ['m', 'o', 'y'], ['q', 'r', 's'], ['d', 'i', 'q'], ['u', 'w', 'z'], ['u', 'w', 'x'], ['u', 'x', 'z'], ['e', 'l', 'x'], ['p', 't', 'v'], ['k', 't', 'w'], ['v', 'x', 'y'], ['f', 'y', 'z'], ['v', 'w', 'z'], ['d', 'f', 'h'], ['h', 't', 'x'], ['c', 'w', 'x'], ['v', 'x', 'z'], ['f', 'p', 'x'], ['g', 'x', 'y'], ['g', 'v', 'w'], ['f', 'l', 's'], ['c', 'f', 'v'], ['g', 'q', 's'], ['d', 't', 'y'], ['j', 'p', 't'], ['d', 'k', 's'], ['s', 'w', 'x'], ['d', 'q', 'x'], ['o', 'r', 's'], ['l', 'v', 'y'], ['r', 't', 'y'], ['i', 'y', 'z'], ['g', 'r', 'w'], ['g', 'h', 'l'], ['c', 'x', 'z'], ['g', 't', 'v'], ['f', 'g', 'n'], ['l', 'r', 't'], ['r', 'u', 'x'], ['u', 'x', 'y'], ['s', 'x', 'y'], ['b', 'u', 'z'], ['l', 'w', 'y'], ['a', 'n', 'v'], ['k', 'l', 'z'], ['n', 'q', 'w'], ['m', 'u', 'z'], ['k', 'u', 'y'], ['t', 'v', 'z'], ['o', 'w', 'z'], ['c', 'h', 'y'], ['h', 's', 'y'], ['l', 'r', 'z'], ['a', 's', 'z'], ['f', 'r', 'v'], ['d', 'q', 'v'], ['u', 'v', 'y'], ['t', 'x', 'y'], ['b', 'w', 'y'], ['j', 'q', 'u'], ['o', 't', 'y'], ['p', 'y', 'z'], ['l', 'y', 'z'], ['n', 's', 'u'], ['m', 's', 'x'], ['b', 's', 'y'], ['l', 's', 'z'], ['d', 'm', 'u'], ['i', 'o', 'w'], ['c', 'v', 'w'], ['t', 'y', 'z'], ['l', 'n', 'y'], ['m', 'x', 'y'], ['n', 'v', 'x'], ['n', 'u', 'z'], ['g', 'h', 's'], ['r', 'v', 'w'], ['j', 'u', 'x'], ['m', 'v', 'z'], ['d', 'r', 'z'], ['o', 'v', 'x'], ['f', 'n', 'q'], ['a', 'b', 't'], ['h', 'v', 'x'], ['e', 'u', 'x'], ['o', 'w', 'y'], ['d', 'i', 'm'], ['a', 'f', 'w'], ['f', 'n', 'r'], ['d', 'm', 'x'], ['p', 'r', 'z'], ['p', 'u', 'v'], ['e', 'y', 'z'], ['c', 'o', 'x'], ['c', 'x', 'y'], ['a', 'i', 'w'], ['q', 'x', 'y'], ['c', 'i', 'n'], ['u', 'v', 'z'], ['u', 'w', 'y'], ['f', 'r', 'x'], ['t', 'w', 'z'], ['e', 'r', 'v'], ['o', 'q', 't'], ['m', 'w', 'x'], ['g', 'v', 'x'], ['c', 'j', 'k'], ['i', 's', 'y'], ['g', 's', 'u'], ['i', 'j', 's'], ['d', 'm', 'n'], ['l', 'n', 'v'], ['e', 's', 'w'], ['o', 'u', 'w'], ['b', 's', 'z'], ['a', 'd', 'g'], ['l', 'w', 'x'], ['m', 'r', 'x'], ['j', 'k', 'l'], ['f', 'p', 's'], ['p', 'r', 'v'], ['g', 'x', 'z'], ['o', 'u', 'z'], ['h', 'k', 's'], ['i', 'r', 'w'], ['n', 'q', 'y'], ['o', 'q', 'r'], ['f', 'q', 'y'], ['e', 'j', 'z'], ['e', 'o', 'u'], ['j', 'k', 'z'], ['b', 'g', 't'], ['f', 'v', 'w'], ['w', 'x', 'y'], ['t', 'v', 'w'], ['a', 'p', 'w'], ['c', 'l', 'x'], ['q', 's', 'y'], ['k', 'n', 'q'], ['d', 'y', 'z'], ['i', 'p', 'v'], ['e', 'k', 'y'], ['e', 'w', 'z'], ['i', 'm', 'v'], ['j', 's', 'v'], ['l', 'o', 'u'], ['e', 'o', 'q'], ['a', 'i', 's'], ['e', 'm', 'y'], ['b', 'y', 'z'], ['c', 'k', 'u'], ['a', 'k', 'p'], ['p', 'x', 'y'], ['h', 'p', 'q'], ['p', 't', 'w'], ['e', 'x', 'z'], ['l', 'p', 'y'], ['m', 'y', 'z'], ['l', 't', 'v'], ['d', 'g', 'n'], ['h', 'o', 't'], ['c', 't', 'x'], ['a', 'o', 'v'], ['m', 'v', 'x'], ['k', 'o', 'q'], ['i', 'v', 'y'], ['b', 'm', 's'], ['h', 'q', 'w'], ['f', 'h', 'x'], ['i', 'v', 'z'], ['f', 't', 'w'], ['l', 'v', 'z'], ['f', 'g', 'w'], ['s', 'w', 'z'], ['j', 'k', 'o'], ['d', 'j', 'm'], ['r', 't', 'u'], ['k', 'm', 'z'], ['q', 'w', 'y'], ['q', 'u', 'v'], ['g', 's', 'x'], ['p', 's', 't'], ['i', 'm', 't'], ['c', 'g', 'y'], ['n', 'w', 'z'], ['o', 'r', 'z'], ['h', 'i', 'm'], ['n', 't', 'w'], ['s', 'u', 'y'], ['s', 'x', 'z'], ['h', 'x', 'z'], ['e', 'f', 'x'], ['a', 'k', 'n'], ['h', 's', 'z'], ['j', 'o', 'w'], ['o', 't', 'x'], ['l', 'n', 'r'], ['m', 'x', 'z'], ['r', 'x', 'y'], ['b', 'w', 'z'], ['c', 'j', 'q'], ['b', 'f', 'o'], ['o', 'x', 'z'], ['i', 'j', 'r'], ['p', 'q', 'y'], ['j', 'p', 's'], ['m', 'r', 'w'], ['a', 'e', 'y'], ['u', 'y', 'z'], ['j', 'l', 'u'], ['j', 's', 'y'], ['k', 'x', 'z'], ['p', 'v', 'y'], ['j', 'l', 'p'], ['p', 'v', 'z'], ['f', 'h', 't'], ['k', 'n', 'x'], ['f', 'n', 'o'], ['p', 'v', 'w'], ['k', 'v', 'y'], ['j', 'w', 'y'], ['e', 'n', 's'], ['f', 'j', 'p'], ['f', 'u', 'w'], ['g', 'm', 'z'], ['n', 's', 'y'], ['m', 's', 'z'], ['c', 'd', 'x'], ['l', 'x', 'y'], ['g', 'y', 'z'], ['b', 't', 'w'], ['n', 'q', 'z'], ['r', 'w', 'y'], ['r', 't', 'w'], ['l', 't', 'x'], ['m', 'w', 'y'], ['h', 'm', 't'], ['k', 'n', 'v'], ['a', 'j', 'y'], ['f', 'q', 'w'], ['s', 'u', 'w'], ['p', 't', 'z'], ['j', 'l', 'r'], ['m', 'n', 'w'], ['n', 't', 'v'], ['n', 'p', 'r'], ['l', 'u', 'w'], ['g', 'j', 'o'], ['b', 'j', 'v'], ['m', 'o', 't'], ['k', 'w', 'z'], ['f', 'i', 'n'], ['i', 'u', 'y'], ['p', 'v', 'x'], ['k', 'l', 'u'], ['b', 'c', 'f'], ['f', 'q', 'v'], ['c', 'h', 'u'], ['i', 'n', 'w'], ['q', 's', 't'], ['k', 'q', 'w'], ['o', 'q', 's'], ['o', 'r', 'v'], ['m', 't', 'u'], ['n', 'u', 'y'], ['c', 's', 'z'], ['o', 'q', 'x'], ['r', 't', 'z'], ['a', 'g', 'q'], ['g', 's', 'z'], ['i', 'w', 'y'], ['j', 'l', 'y'], ['e', 'v', 'x'], ['e', 'n', 't'], ['f', 'g', 'v'], ['a', 'j', 'n'], ['d', 'h', 'r'], ['a', 'p', 'u'], ['l', 's', 'v'], ['l', 'q', 'z'], ['k', 'y', 'z'], ['r', 's', 'y'], ['n', 'x', 'y'], ['o', 'u', 'x'], ['n', 'q', 't'], ['c', 'f', 'h'], ['q', 's', 'x'], ['a', 'l', 'p'], ['l', 's', 'u'], ['e', 'r', 'y'], ['k', 'v', 'x'], ['j', 'o', 's'], ['o', 'p', 'q'], ['m', 'v', 'w'], ['o', 'q', 'v'], ['a', 'w', 'z'], ['l', 'u', 'x'], ['g', 's', 'v'], ['p', 'q', 'v'], ['b', 'o', 's'], ['o', 's', 'v'], ['f', 'h', 'y'], ['k', 's', 'w'], ['h', 't', 'u'], ['t', 'v', 'x'], ['q', 'v', 'w'], ['j', 'p', 'v'], ['c', 'l', 'u'], ['m', 's', 'w'], ['e', 'j', 'p'], ['e', 'f', 'h'], ['a', 's', 't'], ['i', 'k', 't'], ['j', 'l', 'm'], ['d', 'e', 'x'], ['j', 'x', 'y'], ['a', 'k', 'v'], ['j', 'q', 'v'], ['s', 'v', 'y'], ['d', 'k', 'q'], ['g', 'o', 's'], ['a', 'u', 'y'], ['h', 'u', 'x'], ['e', 'q', 's'], ['a', 'f', 'v'], ['i', 'r', 'x'], ['o', 'y', 'z'], ['h', 'v', 'z'], ['i', 'u', 'v'], ['h', 'p', 'x'], ['i', 't', 'z'], ['f', 'o', 'q'], ['a', 'x', 'y'], ['t', 'w', 'x'], ['c', 'u', 'w'], ['b', 'g', 'u'], ['q', 'v', 'y'], ['r', 'x', 'z'], ['s', 'u', 'x'], ['s', 'v', 'z'], ['e', 'h', 'l'], ['e', 'w', 'y'], ['j', 's', 'x'], ['q', 'w', 'x'], ['q', 'x', 'z'], ['f', 'l', 'n'], ['d', 'n', 'y'], ['j', 'r', 'u'], ['u', 'v', 'w'], ['t', 'x', 'z'], ['m', 'o', 'z'], ['f', 'm', 'q'], ['k', 'l', 'y'], ['f', 's', 'x'], ['m', 'w', 'z'], ['g', 'w', 'x'], ['m', 'u', 'y'], ['n', 'q', 'u'], ['l', 't', 'w'], ['r', 'u', 'z'], ['o', 's', 'w'], ['d', 's', 'y'], ['u', 'v', 'x'], ['h', 'y', 'z'], ['g', 'm', 'u'], ['a', 'c', 'l'], ['d', 'e', 'k'], ['p', 'q', 's'], ['g', 'j', 'l'], ['c', 'e', 'g'], ['b', 'l', 'v'], ['o', 'q', 'z'], ['p', 'q', 'u'], ['m', 'u', 'w'], ['j', 'n', 'y'], ['c', 'q', 'v'], ['p', 'u', 'w'], ['i', 'o', 'y'], ['f', 'm', 'x'], ['j', 't', 'x'], ['h', 'm', 'x'], ['c', 's', 'x'], ['i', 'q', 'v'], ['s', 'v', 'w'], ['i', 'w', 'x'], ['m', 'p', 't'], ['o', 'v', 'y'], ['p', 't', 'u'], ['e', 'w', 'x'], ['n', 'r', 's'], ['e', 'l', 'z'], ['s', 'u', 'z'], ['g', 'm', 't'], ['h', 'u', 'v'], ['r', 't', 'x'], ['l', 's', 'x'], ['o', 'p', 'v'], ['n', 'v', 'w'], ['p', 's', 'u'], ['e', 's', 'u'], ['j', 'y', 'z'], ['f', 'n', 'u'], ['h', 's', 'v'], ['f', 'm', 'n'], ['i', 'q', 'x'], ['d', 'j', 'l'], ['k', 't', 'v'], ['o', 'p', 'w'], ['e', 'k', 'm'], ['j', 'n', 'v'], ['h', 'j', 'p'], ['p', 'x', 'z'], ['c', 'g', 't'], ['i', 'n', 'r'], ['h', 'o', 'p'], ['c', 'h', 'v'], ['l', 'p', 'z'], ['q', 'v', 'z'], ['e', 't', 'w'], ['b', 't', 'x'], ['d', 'v', 'x'], ['l', 'r', 'u'], ['f', 'k', 'y'], ['f', 'x', 'y'], ['h', 'm', 'n'], ['s', 'v', 'x']]
result = recover_secret(mytriplets)  # 'abcdefghijklmnopqrstuvwxyz'
# ---------------------


print(result)
