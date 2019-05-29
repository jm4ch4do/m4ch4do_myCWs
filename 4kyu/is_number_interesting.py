# ----- Problem: Catching Car Mileage Numbers (4kyu)
# ----- URL: https://www.codewars.com/kata/52c4dd683bfd3b434c000292


def is_number_interesting(_number, _awesome):
    """
    (int) -> (int)
    :param _number: int with any number between 0 and 1 000 000
    :param _awesome: list with ints that will always be interesting
    :return: 2 if number is interesting, 1 if next or double_next number will be interesting, 0 otherwise

    :description:
    An interesting number should always be greater than 99
    These are the interesting numbers:
    1. Any digit followed by all zeros (100. 90000)
    2. Every digit is the same (1111)
    3. Digits are sequential, incrementing (1234, 7890)
    4. Digits are sequential, decrementing (5432, 3210)
    5. Digits are a palindrome (1221, 73837)
    6. Digits match one of the values in the awesome_phrases list

    :examples:
    3, [1337, 256] -> 0
    3236, [1337, 256] -> 0

    11207, [] -> 0
    11208, [] -> 0
    11209, [] -> 1
    11210, [] -> 1
    11211, [] -> 2

    1335, [1337, 256] -> 1
    1336, [1337, 256] -> 1
    1337, [1337, 256] -> 2
    """
    # Handle slow numbers
    if _number < 98:  # too low -> 0
        return 0

    elif _number in (98, 99):  # 100 will come soon -> 1
        return 1

    elif _number == 100:  # followed by zeros -> 1
        return 2

    # Next tests will handle current, next and double_next numbers
    nums = [0, 0, 0]
    nums[0], nums[1], nums[2] = str(_number), str(_number + 1), str(_number + 2)

    # Check if any condition is met for any of the three numbers
    for i, num in enumerate(nums):

        # verify conditions
        if is_followed_by_zeros(num) or \
                are_all_digits_equal(num) or \
                are_digits_incrementing(num) or \
                are_digits_decrementing(num) or \
                are_digits_palindrome(num) or \
                int(num) in _awesome:

            # conditions met for first number -> 2
            if i == 0:
                return 2

            # conditions met for next or double_next -> 1
            else:
                return 1

    # no condition met for any of the three numbers -> 0
    return 0


def is_followed_by_zeros(_n):

    # first digit zero -> False
    if _n[0] == 0:
        return False

    # any other digit is non-zero -> False
    for d in _n[1:]:
        if d != '0':
            return False

    # otherwise -> True
    return True


def are_all_digits_equal(_n):
    ref = _n[0]

    # if any digit is different from ref -> False
    for d in _n[1:]:
        if d != ref:
            return False

    # otherwise -> True
    return True


def are_digits_incrementing(_n):

    # set-up
    ref = _n[0]  # reference to compare next number with
    digits = _n[1:]  # first number is excluded (first is ref)

    # if any digit is not incrementing -> False
    for d in digits:

        # If '9' is not followed by '0' -> False
        if ref == '9':
            if d != '0':
                return False

        # If any other number is not followed by number + 1 -> False
        else:
            if int(d) - 1 != int(ref):
                return False

        # save ref for next iteration
        # If '0'
        ref = d

    # no problem -> digits are incrementing
    return True


def are_digits_decrementing(_n):
    # set-up
    ref = _n[0]  # reference to compare next number with
    digits = _n[1:]  # first number is excluded (first is ref)

    # if any digit is not decrementing -> False
    for d in digits:

        # If '0' -> False (no number is accepted after zero when evaluating decrement)
        if ref == '0':
                return False

        # If any other number is not followed by number - 1 -> False
        else:
            if int(d) + 1 != int(ref):
                return False

        # save ref for next iteration
        ref = d

    # no problem -> digits are decrementing
    return True


def are_digits_palindrome(_n):
    # --- divide in two sides for latter comparison
    front, back = [], []

    # numbers like '1221' must be split in '12' adn '21'
    if is_even(len(_n)):
        front = _n[:len(_n) // 2]
        back = _n[len(_n) // 2:]

    # numbers like '73837' must be split in '73' adn '37'
    else:
        front = _n[:len(_n) // 2]
        back = _n[len(_n) // 2 + 1:]

    # if front is different to reversed back -> False
    front = list(front)
    back = list(reversed(list(back)))

    if front != back:
        return False

    # no problem found -> True
    return True


def is_even(_d):
    return True if _d % 2 == 0 else False


# ----- MAIN CODE --------------------------------------------------
my_num, my_awe = 67890, []
result = is_number_interesting(my_num, my_awe)
print(result)
