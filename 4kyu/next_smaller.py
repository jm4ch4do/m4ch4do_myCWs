def next_smaller(n):
    """
    (number) -> (number)

    :param n: number integer
    :returns: the next smaller number with the same digits of n

    :var: [jumper]    -> first number that goes from low to high reading from the rigth.
                         the jumper is going to jump to a new position
          [subs]      -> number to the right of jumper being lower than jumper and as close to it as posible
                         the subs is going the take the jumper position
          [safe_part] -> digits to the left of the jumper which are not to be moved or modified
          [remainder] -> digits to the right of the jumper from which the subs is selected
                         digits in the reaminder are sorted after removing the subs and including the jumper

    Returns the next smaller number with the same digits of input n [safe_part + jumper + remainder_part]

    :algorithm:
     (input) = 1423
     1. find jumper: reading from right to left find jumper which is the first digit being higher than the previous one
        (in 1423 the jumper = 4, jumper_rpos = -3, jumper_pos = 1)
     2. select safe part: all digits to the left of the jumper are the safe_part
        (in 1423 safe_part = 1)
     3. find subs: find in remainder_part a digit (subs) lower than jumper but as close to it as posible
        (subs = 3, remainder_part = 423 )
     4. remove subs from remainder_part
        (remainder_part = 42)
     5. sort remainder_part
        (remainder_part = 42)
     6. return string concat = safe_part + subs + sorted_remainder_part
        (ie '1' + '3' + '42')
     (output) = 1342

    :examples:
    >>> next_smaller(143568)
    138654

    (143568)     -> (138654)
    (505)        -> (-1)
    (907)        -> (790)
    (531)        -> (513)
    (721)        -> (-1)
    (135)        -> (-1)
    (2071)       -> (2017)
    (414)        -> (144)
    (123456798)  -> (123456789)
    (123456789)  -> (-1)
    (1234567908) -> (1234567890)
    """

    # basic exit condition (no number below 21 have valid solution)
    if n < 21:
        return -1

    # 1. Find jumper
    string = str(n)
    slen = len(string)
    jumper_rpos = ''  # reverse_position
    for i in range(-2, (slen+1)*-1, -1):  # ie -2, -3, -4, -5 ..., -(len+1)
        if string[i] > string[i+1]:
            jumper_rpos = i
            break

    # no jumper = no valid solution
    if not jumper_rpos:
        return -1

    # 2. Select safe_part
    jumper_pos = slen + jumper_rpos  # regular_position
    safe_part = string[:jumper_pos]

    # 3. Find subs in remainder
    subs = ''
    subs_pos = ''
    remainder_positions = range(jumper_pos+1, slen)
    for i in remainder_positions:
        if string[i] < string[jumper_pos] and (string[i] > subs or not subs):
            if not (jumper_pos == 0 and string[i] == '0'):  # avoids input 550 to produce a 055 (0 cannot be at start)
                subs = string[i]
                subs_pos = i

    # for input 550 there is no subs = no possible solution
    if not subs:
        return -1

    subs_pos -= jumper_pos  # make subs_pos relative to jumper_pos

    # 4. Remove subs from the remaining part
    remaining_part = string[jumper_pos:]  # create remaining_part
    remaining_part = remaining_part[:subs_pos] + remaining_part[subs_pos+1:]  # remove subs

    # 5. Sort remainder (from higher to lower) and return string concat
    remaining_part = list(remaining_part)
    remaining_part.sort(reverse=True)
    string_remaining_part = ''.join(remaining_part)

    # 6. Return concat of the three parts
    next_lower_number = safe_part + subs + string_remaining_part
    return int(next_lower_number)
