def zeros_to_end(_alist):
    """
    (list) -> (list)
    :param _alist: a list with random characters and zeros
    :return: same list but with zeros at the end

    :example:
    [False, 1, 0, 1, 2, 0, 1, 3, "a"] -> [False, 1, 1, 2, 1, 3, "a", 0, 0]
    """
    count = 0
    output = []
    for value in _alist:
        if not value and type(value) != bool:
            count += 1
        else:
            output.append(value)

    output.extend([0]*count)
    return output
