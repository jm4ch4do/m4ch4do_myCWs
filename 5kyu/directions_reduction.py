# ----- Directions Reduction (5ku)
# ----- URL: https://www.codewars.com/kata/550f22f4d758534c1100025a


def directions_reduction(_lon_dir):
    """
    (list) -> (list)
    :param _lon_dir: list with string having "NORTH", "SOUTH", "EAST", "WEST"
    :return: list with simplified() directions (i.e. there is no point in going "NORTH" and the "SOUTH")

    :example:
    ["NORTH", "SOUTH", "SOUTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] -> ["SOUTH", "SOUTH", "WEST"]
    """

    # initial setup
    ini_dir = _lon_dir  # initial list
    opposites = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST'
    }

    # simplify directions until there is nothing left to reduce
    while True:
        erase_next = False
        new_dir = []

        # check records making simplifications
        for i, value in enumerate(ini_dir):
            if erase_next:
                erase_next = False
                continue

            # gets next value except for last where it gets previous value
            next_value = ini_dir[i + 1] if i < len(ini_dir) - 1 else ini_dir[i - 1]

            # decide if the value should be included in the short_list
            if not are_opposites(value, next_value, opposites):
                new_dir.append(value)
            else:
                erase_next = True

        # stop criteria
        if len(ini_dir) == len(new_dir):  # no simplification took place -> return list
            return new_dir
        elif not new_dir:  # all directions simplified -> return empty list
            return []
        else:  # a simplification took place
            ini_dir = new_dir.copy()  # restart ini_dir and run again


def are_opposites(_value1, _value2, _opposites):
    return True if _value1 == _opposites[_value2] else False


my_long_dir = ["NORTH", "SOUTH", "SOUTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
expected = ["SOUTH", "SOUTH", "WEST"]
result = directions_reduction(my_long_dir)
print(result)
