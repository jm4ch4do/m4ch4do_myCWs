# ----- Double Cola (5ku)
# ----- URL: https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0


def double_cola_line(_persons, _turn):
    """
    (_list_of_string, int) -> string
    :param _persons: list with strings having names
    :param _turn: int with requested turn in the queue
    :return: string with name taken from _people who corresponds to the requested _turn

    :description:
    There are _persons in the line for drinking a "double cola". Everyone who drinks gets duplicated and goes
    to the end of the line. Next an example of a line:
    ["Sheldon", "Leonard", "Penny"]
    ["Leonard", "Penny", "Sheldon", "Sheldon"]
    ["Penny", "Sheldon", "Sheldon", "Leonard", "Leonard"]
    The problem aks who is up to in a given _turn

    :examples:
    (["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 1) -> "Sheldon"
    (["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) -> "Penny"
    (["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) -> "Leonard"

    :algorithm:
    The explanation uses example two to illustrate the procedure:
    1. Count amount of _persons
        (amount = drinkers = 5)
    2. Find round where the turn takes place
        round = 1, multiplier = 1, drinkers = 5, accumulated = 5
        round = 2, multiplier = 2, drinkers = 10, accumulated = 15
        round = 3, multiplier = 4, drinkers = 20, accumulated = 35
        round = 4, multiplier = 8, drinkers = 40 accumulated = 75 which is higher than _turn = 52
        So _turn happens in round = 4
    3. Find person who drinks at _turn in selected round
        For round = 4 there are accumulated = 35, so there are left remaining_turns = 52 - 35 = 17
            remaining_turns//multiplier = 17//8 = 2
            + 1 if 17%8 != 0
            So the result is 3
            This means the person who drank in _turn is _persons[3-1] = "Penny"
            17//8 = 2 + ceil(17%8)

    """
    # 1. Count amount of _persons
    amount = len(_persons)

    # 2. Find round where the turn takes place

    # set-up
    accumulated = 0
    round = 1
    multiplier = 1
    drinkers = amount

    # increase round until accumulated surpassed _turn
    while True:
        previous_acc = accumulated  # previous accumulated
        accumulated += drinkers
        if accumulated >= _turn:
            break

        round += 1
        multiplier *= 2
        drinkers = amount * multiplier

    # 3. Find person who drinks at _turn in selected round
    remaining_turns = _turn - previous_acc
    select = remaining_turns // multiplier
    select += 1 if remaining_turns % multiplier != 0 else 0

    return _persons[select - 1]


my_persons = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
my_turn = 7230702951
result = double_cola_line(my_persons, my_turn)
print(result)
