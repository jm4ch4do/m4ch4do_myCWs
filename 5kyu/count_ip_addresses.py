# ----- Problem: Count IP addresses (5kyu)
# ----- URL: https://www.codewars.com/kata/526989a41034285187000de4


def count_ip_addresses(_ip_ini, _ip_end):
    """
    (string) -> (int)
    :param _ip_ini: string with the first ip address
    :param _ip_end: string with the last ip address
    :return: int with amount address between _ip_ini and _ip_end

    :example:
    '10.0.0.10', '10.0.1.0' -> 246
    """

    # split ips into four separate numbers
    l_ini, l_end = _ip_ini.split('.'), _ip_end.split('.')

    # find difference for each of the four numbers
    difs = [int(val2) - int(val1) for val1, val2 in zip(l_ini, l_end)]

    # multiply each number by (256 ** count) before adding
    count = 3
    _amount = 0
    for value in difs:
        _amount += value * 256 ** count
        count -= 1

    return _amount


# ------------------------- MAIN CODE -------------------------
my_ip_ini = '10.0.0.10'
my_ip_end = '10.0.1.0'
result = count_ip_addresses(my_ip_ini, my_ip_end)
print(result)
