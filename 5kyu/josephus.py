def josephus(_soldiers, _k):
    """
    (list, int) -> list_of_int
    :param _soldiers: list with names(or numbers) of every soldier
    :param _k: number to count before killing
    :return: list_of_int with the order in which each soldier(represented by a number) was kill

    :description:
    _k = 3
    The third soldier(value) in the input list should go to output(_deads), then the six and so on
    (The are committing suicide for avoiding surrender)

    :example:
    _k = 3
    _soldiers = [1, 2, 3, 4, 5, 6, 7]
    [1, 2, 4, 5, 6, 7] -> [3]
    [1, 2, 4, 5, 7] -> [3, 6]
    [1, 4, 5, 7] -> [3, 6, 2]
    [1, 4, 5] -> [3, 6, 2, 7]
    [1, 4] -> [3, 6, 2, 7, 5]
    [4] -> [3, 6, 2, 7, 5, 1]
    [] -> [3, 6, 2, 7, 5, 1, 4]
    _deads = [3, 6, 2, 7, 5, 1, 4]

    :algorithm:
    _k = 3
    count until three, pop(third value), append third value to list, go to previous
    repeat again
    if you get to the end(_n) get back to the start and keep counting

    """
    # initial values
    _deads = []
    count = 1
    index = 0

    # execute until all soldiers are dead
    while _soldiers:

        # send last soldier to graveyard (final condition)
        if len(_soldiers) == 1:
            _deads.append(_soldiers.pop())
            continue

        # count < _k -> keep counting
        if count < _k:
            count += 1
            index = 0 if index == len(_soldiers) - 1 else index + 1  # get back to the start after last soldier
            continue

        # count == _k -> kill the third(_k) soldier
        if count == _k:
            _deads.append(_soldiers.pop(index))
            count = 1
            index = 0 if index == len(_soldiers) else index  # get back to the start if you kill last soldier
            continue

    # return graveyard
    return _deads
