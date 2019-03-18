# ----- Problem: The observed PIN (4ku)
# ----- URL: https://www.codewars.com/kata/5263c6999e0f40dee200059d


def rotate(_pin_choices, _rot_state):
    """
    (list_of_tuples, list_of_int) -> boolean
    :param _pin_choices: list with tuples having possible choices for brute force combination
    :param _rot_state: list with ints indicating the current state in rotation

    :return: Modifies _rot_state by changing it to the next state in rotation
             Returns _end = True when rot_state passed all states and get back to original [0, 0, 0 ...]

    :example:
        (_pin_choices = [('1', '2', '4'), ('1', '2', '4')])
        (_rot_state = [2, 1])

        modifies (rot_state = [0, 2])
        returns _end = False
    """
    for i, etuple in enumerate(_pin_choices):
        if _rot_state[i] < len(etuple)-1:
            _rot_state[i] += 1
            break
        else:
            _rot_state[i] = 0

    _end = True if sum(_rot_state) == 0 else False
    return _end


def get_pins(pin):
    """
    (string) -> (list_of_strings)
    :param pin: observed pin
    :return: all possible combinations for observed pin

    :descrition:

    | 1 | 2 | 3 |
    | 4 | 5 | 6 |
    | 7 | 8 | 9 |
        | 0 |

    The digits in pin where observed in the previous keyboard
    Every observed digit could be confused with any in top, down, left or right (see example 1 for input '8')
    The function returns every possible combination of pins for the digits in observed pin

    :examples:
    ('8') -> ['5','7','8','9','0']
    ('11') -> ["11", "22", "44", "12", "21", "14", "41", "24", "42"],
    ('369') -> ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638",
                "396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298",
                "236","239"])]

    :internal_variables:
    choices = dictionary that has the top, down, left and right choices for every digit in the keyboard
    pin_choices = list_of_tuples where every tuple has the possible choices for every character in ping
        (pin_choices = [('1', '2', '4'), ('1', '2', '4')) for example 2
    rot_state = current state of rotation for pin_choices
        (rot_state = [2, 1] means take pos = 2 from pin_choises[0] and pos = 1 from pin_choices[1])
        (i.e. make '42')

    :helper_functions:
    end = rotate(pin_choices, rot_state)
    Modifies rot_state by moving to the next possible position in pin_choices
    Returns end when all positions where covered
    (ex. for pin_choices = [('1', '2', '4'), ('1', '2', '4') and rot_state = [2, 1] modifies to rot_state = [0, 2]
    (ex. will return true when rot_state = [2, 2] modifying rot_state = [0, 0] which is the final state )

    :algorithm:
    1. Define choices dictionary and find pin_choices
        (choices = {'1': ('1', '2', '4'), '2': ('1', '2', '3', '5'), ...})
        (pin_choices = [('1', '2', '4'), ('1', '2', '4')])
    2. Loop rotating all positions
        . For every rot_state produce a ppin (possible pin)
    3. Return all possible pins (all_ppin)
    """

    # 1. Define choices dictionary and find pin_choices
    choices = {
                '1': ('1', '2', '4'),
                '2': ('1', '2', '3', '5'),
                '3': ('2', '3', '6'),
                '4': ('1', '4', '5', '7'),
                '5': ('2', '4', '5', '6', '8'),
                '6': ('3', '5', '6', '9'),
                '7': ('4', '7', '8'),
                '8': ('5', '7', '8', '9', '0'),
                '9': ('6', '8', '9'),
                '0': ('8', '0')
    }

    pin_choices = [choices[ch] for ch in pin]

    # 2. Loop rotating all positions
    rot_state = [0]*len(pin_choices)
    ppins = []
    end = False
    while not end:
        ppin = ''
        for i, pos in enumerate(rot_state):
            ppin += pin_choices[i][pos]

        ppins.append(ppin)
        end = rotate(pin_choices, rot_state)

    return ppins


mypin = '11'
real = get_pins(mypin)
expected = ["11", "22", "44", "12", "21", "14", "41", "24", "42"]

print(real)
print(expected)
