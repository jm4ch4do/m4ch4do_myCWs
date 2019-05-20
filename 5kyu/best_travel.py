# ----- Problem: Best travel (5ku)
# ----- URL: https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa
from itertools import combinations


def choose_best_sum(_fuel, _visits, _distances):
    """
    (int, list_of_ints, int) -> int
    :param _fuel: int with kilometers the car may go with the remaining fuel
    :param _visits: int with amount of towns to visit
    :param _distances: list with ints representing distances to towns
    :return: list_with_ints having len = _visits and using values from _distances such that
             sum(output) <= _fuel and as high as possible

    :description:
    The goal is to go as many kms as you can(under the limit given by fuel), visiting exactly
        amount of towns specified in _visits. The distance to every town is in _distances

    :note:
    This is a classic combinations problem were you find all combinations of _distances an
    choose the one that meets a given criteria

    :examples:
    (174, [50, 55, 57, 58, 60], 3) -> 173   (55, 58, 60)
    (2300, [1000, 640, 1230, 2333, 1440, 500, 1320, 1230, 340, 890, 732, 1346], 4) -> None
    (2300, [1000, 640, 1230, 2333, 1440, 500, 1320, 1230, 340, 890, 732, 1346], 4) -> 2260
    """
    # dummy case
    if len(_distances) < _visits:  # there are not enough towns to complete _visits
        return None
    elif len(_distances) == 1:  # only one town
        return _distances[0]

    # remove _distances that will always sum higher than _fuel
    _distances.sort()
    smallest_dist = sum(_distances[0:_visits - 1])
    for i, value in enumerate(_distances[_visits-1:]):  # if a town makes sum higher than _fuel -> erase all others
        if smallest_dist + value > _fuel:
            if i == 0:  # the smallest dist doesn't is over fuel
                return None
            else:
                _distances = _distances[:_visits + i]
                break

    # find all combinations of _distances to make the requested _visits
    combs = list(combinations(_distances, _visits))

    # compute sums of combinations
    sums = [sum(comb) for comb in combs]

    # find sum closer to _fuel
    index, winner = 0, 0
    for i, candidate in enumerate(sums):
        if candidate <= _fuel:
            if candidate > winner or not candidate:
                winner = candidate
                index = i

    # return the winner sum unless the best candidate is higher than _fuel (there is no proper candidate)
    return sum(combs[index]) if sum(combs[index]) <= _fuel else None


# ----- MAIN CODE --------------------------------------------------
my_fuel = 185
my_distances = [94, 217, 474, 434, 159, 360, 57, 322, 412, 315]
my_visits = 2
result = best_travel(my_fuel, my_visits, my_distances)
print(result)
