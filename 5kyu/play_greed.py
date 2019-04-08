# ----- Problem: Greed is Good (5ku)
# ----- URL: https://www.codewars.com/kata/5270d0d18625160ada0000e4


def play_greed(_trow):
    """
    (list_of_int) -> int
    :param _trow: list with 5 ints in the range 1-6 (each int represents a dice roll)
    :return: The amount of points earned by the trow

    :description:
    According to the rules of the Greed game
    Three 1's -> 1000 points
    Three 6's ->  600 points
    Three 5's ->  500 points
    Three 4's ->  400 points
    Three 3's ->  300 points
    Three 2's ->  200 points
    One   1   ->  100 points
    One   5   ->   50 points

    Every dice can only be counted once for earning points

    :examples:
    [5, 1, 3, 4, 1] -> 250  (50 + 1*100)
    [1, 1, 1, 3, 1] -> 1100 (1000 + 100)
    [2, 4, 4, 5, 4] -> 450  (400 + 50)

    :internal_var:
    rep -> dict with the number of repetitions of each number
                ex. for input [1, 1, 1, 3, 1] -> rep = {1: 4, 3: 1}
                because number 1 was repeated 4 times and number 3 one time

    """
    # initial values
    total_points = 0  # output variable

    pointx3 = {  # points earned when a number is repeated three times
        1: 1000,
        6: 600,
        5: 500,
        4: 400,
        3: 300,
        2: 200
    }

    pointx1 = {  # points earned when a number appears at least one time
        1: 100,
        5: 50
    }

    # count number of repetitions
    rep = {}  # counting dictionary
    for value in _trow:
        rep.setdefault(value, 0)
        rep[value] += 1

    # earn points
    for key, value in rep.items():
        if value == 1:
            total_points += pointx1.get(key, 0)
        elif value == 2:
            total_points += pointx1.get(key, 0) * 2
        elif value == 3:
            total_points += pointx3[key]
        elif value == 4:
            total_points += pointx3[key] + pointx1.get(key, 0)
        elif value == 5:
            total_points += pointx3[key] + pointx1.get(key, 0) * 2

    return total_points


my_trow = [2, 4, 4, 5, 4]
result = play_greed(my_trow)
print(result)
