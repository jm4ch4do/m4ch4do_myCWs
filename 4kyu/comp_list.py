# ----- Problem: Nesting Structure Comparison (4kyu)
# ----- URL: https://www.codewars.com/kata/529446778469526ec0000001


def comp_list(_l1, _l2):
    """
    (list_of_list, list_of_list) -> int
    :param _l1: list_of_list with a given structure
    :param _l2: list_of_list with a given structure than may be equal or different from _l1
    :return: True if both list have the same structure

    :note:
    This is a classic recursion problem

    """
    # both input must be list
    if not isinstance(_l1, list) or not isinstance(_l2, list):
        return False

    # list must have equal length
    if len(_l1) != len(_l2):
        return False

    # check every element
    for val1, val2 in zip(_l1, _l2):

        # if one element is a list, then the other must also be a list
        a = isinstance(val1, list) and not isinstance(val1, list)
        b = isinstance(val2, list) and not isinstance(val1, list)
        if a or b:
            return False

        # list elements must be checked further
        elif isinstance(val1, list):
            if not comp_list(val1, val2):
                return False

    # return True if no check returned False
    return True


def test():

    # --- test 1 ---------------
    name = 'test1'
    l1 = [1, 1, 1]
    l2 = [2, 2, 2]
    result = comp_list(l1, l2)
    expected = True
    if result == expected:
        print(name + ' OK')
    else:
        print('-------------------------')
        print('inputs')
        print(l1)
        print(l2)
        print('result: ' + str(result))
        print('expected: ' + str(expected))
        print('-------------------------')

    # --- test 2 ---------------
    name = 'test2'
    l1 = [1, [1, 1]]
    l2 = [2, [2, 2]]
    result = comp_list(l1, l2)
    expected = True
    if result == expected:
        print(name + ' OK')
    else:
        print('-------------------------')
        print('inputs')
        print(l1)
        print(l2)
        print('result: ' + str(result))
        print('expected: ' + str(expected))
    print('-------------------------')

    # --- test 3 ---------------
    name = 'test3'
    l1 = [1, [1, 1]]
    l2 = [[2, 2], 2]
    result = comp_list(l1, l2)
    expected = False
    if result == expected:
        print(name + ' OK')
    else:
        print('-------------------------')
        print('inputs')
        print(l1)
        print(l2)
        print('result: ' + str(result))
        print('expected: ' + str(expected))
        print('-------------------------')

    # --- test 4 ---------------
    name = 'test4'
    l1 = [1, [1, 1]]
    l2 = [[2, 2]]
    result = comp_list(l1, l2)
    expected = False
    if result == expected:
        print(name + ' OK')
    else:
        print('-------------------------')
        print('inputs')
        print(l1)
        print(l2)
        print('result: ' + str(result))
        print('expected: ' + str(expected))
        print('-------------------------')

    # --- test 5 ---------------
    name = 'test5'
    l1 = [[[], []]]
    l2 = [[[], []]]
    result = comp_list(l1, l2)
    expected = True
    if result == expected:
        print(name + ' OK')
    else:
        print('-------------------------')
        print('inputs')
        print(l1)
        print(l2)
        print('result: ' + str(result))
        print('expected: ' + str(expected))
        print('-------------------------')

    # --- test 6 ---------------
    name = 'test6'
    l1 = [[[], []]]
    l2 = [[1, 1]]
    result = comp_list(l1, l2)
    expected = False
    if result == expected:
        print(name + ' OK')
    else:
        print('-------------------------')
        print('inputs')
        print(l1)
        print(l2)
        print('result: ' + str(result))
        print('expected: ' + str(expected))
        print('-------------------------')


# ----- MAIN CODE --------------------------------------------------
test()

my_l1 = [1, '[', ']']
my_l2 = ['[', ']', 1]
the_result = comp_list(my_l1, my_l2)
print(the_result)
