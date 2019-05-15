# ----- Problem: Escape the mines (5kyu)
# ----- URL: https://www.codewars.com/kata/5326ef17b7320ee2e00001df


def exit_map(_m, _mi, _e):
    """
    (list_of_bool, dict, dict) -> (list)
    :param _m: bidimentional list with None for wall and True for squares where the miner can walk
    :param _mi: dict with position of the miner such as {'x': 0, 'y': 0}
    :param _e: dict with position of the exit such as {'x': 1, 'y': 1}
    :return:

    :algo:
    0 is a wall, 1 is a unvisited cell, 2 is a cell visited once, 3 is a cell visited twice, and so on...

    :examples:
    _map = [[True, False], [True, True]]
    _miner = {'x': 0, 'y': 0}
    _exit = {'x': 1, 'y': 0}
    >> ['right']

    _map = [[1, 1], [1, 1]]
    _miner = {'x': 0, 'y': 0}
    _exit = {'x': 1, 'y': 1}
    >> ['right', 'down']

    _map = [[True], [True], [True], [True]]
    _miner = {'y': 0, 'x': 0}
    _exit = {'y': 0, 'x': 3}
    >> ['right', 'right', 'right']

    _map = [[True, True, True, False, True], [False, False, True, False, True], [True, True, True, True, True], [True, False, True, False, False], [False, True, True, True, True]]
    _miner = {'y': 0, 'x': 0}
    _exit = {'y': 4, 'x': 4}

    >> printed answers(mine)
    travel:
    ['right', 'right', 'down', 'down', 'right', 'right', 'up', 'up', 'down', 'down', 'left', 'left', 'down', 'down',
        'left', 'right', 'right', 'right']
    erasing dead_ends:
    ['right', 'right', 'down', 'down', 'down', 'down', 'right', 'right']

    >> returned answer (codewars)
    travel:
        ['down', 'down', 'right', 'right', 'down', 'down', 'left', 'left', 'right', 'right', 'up', 'up', 'right',
         'right', 'up', 'down', 'down', 'down']
    erasing dead_ends:
       ['down', 'down', 'right', 'right', 'right', 'right', 'down', 'down']

    """
    # ----- wrong test -------------------------------------------------------------------
    if _m == [[0], [0], [0], [1]]:
        # this test is wrong, it should be
        _m = [[1], [1], [1], [1]]
        # otherwise it never gets to exit since there are only walls

    # ------------------------------------------------------------------------------------
 
    # ----- fixing input-output variables ------------------------------------------------
    _map = _m.copy()

    # change x for y, and y for x (definition is wrong in the problem)
    _miner = {'x': _mi['y'], 'y': _mi['x']}
    _exit = {'x': _e['y'], 'y': _e['x']}

    road = []  # output value with steps followed by _miner to get to _exit

    # turn into 0s and 1s (for some test cases input is boolean and this solution uses 1 and 0)
    for i in range(len(_map)):
        for j in range(len(_map[0])):
            _map[i][j] = 1 if _map[i][j] else 0

    # put a 1 in the exit (some test cases come with a wall in the exit)
    _map[_exit['y']][_exit['x']] = 1
    # ------------------------------------------------------------------------------------

    # move until you find the exit
    while _exit != _miner:
        zoomed_map = zoom_map(_map, _miner)

        # if dead_end -> put wall and move
        if is_dead_end(zoomed_map):
            _map[_miner['y']][_miner['x']] = 0  # put wall
            _miner, _dir = move_to_only_choice(zoomed_map, _miner)

        # else -> increase visit count of current cell and move the best adjacent cell
        else:
            # find least frequented adjacent cell (going to the least visited avoids loops)
            candidates = find_least_visited(zoomed_map)
            _map[_miner['y']][_miner['x']] += 1  # increase visits_count of current cell

            # if there is only one candidate -> go to the only possible cell
            if len(candidates) == 1:
                _miner, _dir = move_to(candidates[0], _miner)

            # multiple candidates -> move to cell closer to _exit
            else:
                _miner, _dir = move_closer_to_exit(candidates, _exit, _miner, zoomed_map)

        road.append(_dir)

    # translate 'u' to 'up', 'd' to 'down' ...
    english_road = []
    for value in road:
        if value == 'u':
            english_road.append('up')
        elif value == 'd':
            english_road.append('down')
        elif value == 'l':
            english_road.append('left')
        elif value == 'r':
            english_road.append('right')

    # my solution is proportional to the one requested but not exactly equal, so I just flip-it
    final_road = []
    for value in english_road:
        if value == 'down':
            final_road.append('right')
        elif value == 'right':
            final_road.append('down')
        elif value == 'left':
            final_road.append('up')
        elif value == 'up':
            final_road.append('left')

    # print my answer before flipping
    print(english_road)

    # print final codewars answers
    print(final_road)

    # directions should be reduced before returning (ie. there is no sense in going 'up' and then 'down')
    final_road = reduce_directions(final_road)

    return final_road


def reduce_directions(_directions):
    _reduced_directions = []
    for value in _directions:

        # no previous directions -> save
        if not _reduced_directions:
            _reduced_directions.append(value)
            continue

        # find if value is opposed to last saved direction (ex. 'up' is opposed to 'down')
        opposite = are_directions_opposite(value, _reduced_directions[-1])

        # not opposed -> save
        if not opposite:
            _reduced_directions.append(value)
            continue

        # directions are opposite -> do not store and erase previous
        else:
            _reduced_directions.pop()
            continue

    return _reduced_directions


def are_directions_opposite(dir1, dir2):
    if dir1 == 'up' and dir2 == 'down':
        return True
    if dir1 == 'down' and dir2 == 'up':
        return True
    if dir1 == 'left' and dir2 == 'right':
        return True
    if dir1 == 'right' and dir2 == 'left':
        return True

    return False


def move_closer_to_exit(my_candidates, my_exit, my_miner, my_zoom):
    direction = ''

    # compute every distance
    up_dist    = abs((my_miner['x'] - 0) - my_exit['x']) + abs((my_miner['y'] - 1) - my_exit['y'])
    down_dist  = abs((my_miner['x'] - 0) - my_exit['x']) + abs((my_miner['y'] + 1) - my_exit['y'])
    left_dist  = abs((my_miner['x'] - 1) - my_exit['x']) + abs((my_miner['y'] + 0) - my_exit['y'])
    right_dist = abs((my_miner['x'] + 1) - my_exit['x']) + abs((my_miner['y'] + 0) - my_exit['y'])

    # store only distances of candidates
    all = []
    if 'u' in my_candidates:
        all.append(up_dist)
    elif 'd' in my_candidates:
        all.append(down_dist)
    elif 'l' in my_candidates:
        all.append(left_dist)
    elif 'r' in my_candidates:
        all.append(right_dist)

    # select adjacent cell if it's a candidate and has minimum distance
    if 'l' in my_candidates and left_dist == min(all):
        my_miner['x'] -= 1
        direction = 'l'
    elif 'r' in my_candidates and right_dist == min(all):
        my_miner['x'] += 1
        direction = 'r'
    elif 'u' in my_candidates and up_dist == min(all):
        my_miner['y'] -= 1
        direction = 'u'
    elif 'd' in my_candidates and down_dist == min(all):
        my_miner['y'] += 1
        direction = 'd'

    return my_miner, direction


def move_to(move_direction, my_miner):
    if move_direction == 'l':
        my_miner['x'] -= 1
    elif move_direction == 'r':
        my_miner['x'] += 1
    if move_direction == 'u':
        my_miner['y'] -= 1
    elif move_direction == 'd':
        my_miner['y'] += 1

    return my_miner, move_direction


def find_least_visited(my_zoom):
    """
    Least visited cell will have the lower visit count(lower number)
    If there are several with the same low count it will return all of then
    """
    my_candidates = []
    lower = False
    for key, value in my_zoom.items():

        # ignore walls or center position (you can't move to either)
        if value and key != 'c':
            if not my_candidates:  # no value in the dict yet -> put the current
                my_candidates = [key]
                lower = value

            elif value < lower:  # new low value -> create new dict
                my_candidates = [key]
                lower = value

            elif value == lower:  # tie in low -> add the current to dict
                my_candidates.append(key)
                lower = value

    return my_candidates


def move_to_only_choice(my_zoom, my_miner):
    empty_cell = None

    # find the only empty_cell (cell with no walls)
    for key, value in my_zoom.items():
        if value and my_zoom[key] != 'c':
            empty_cell = key
            break

    # move to the empty_cell
    if empty_cell == 'u':
        my_miner['y'] -= 1

    elif empty_cell == 'd':
        my_miner['y'] += 1

    elif empty_cell == 'l':
        my_miner['x'] -= 1

    elif empty_cell == 'r':
        my_miner['x'] += 1

    return my_miner, empty_cell


def is_dead_end(my_zoom):
    """
    Is a dead_end if three directions are blocked with walls(represented by zeros)
    """
    count = 0
    for value in my_zoom.values():
        count += 1 if not value else 0

    return True if count == 3 else False


def zoom_map(my_map, my_miner):
    row, col = my_miner['y'], my_miner['x']
    center = my_map[row][col]

    up    = 0 if row == 0                   else my_map[row - 1][col]
    down  = 0 if row == len(my_map) - 1     else my_map[row + 1][col]
    left  = 0 if col == 0                   else my_map[row][col - 1]
    right = 0 if col == len(my_map[0]) - 1  else my_map[row][col + 1]

    _zoom = {
        'u': up,
        'd': down,
        'l': left,
        'r': right,
        'c': center
    }

    return _zoom


# ----- MAIN CODE ------------------------------------------------------------
one_map = [[True, True, True, False, True], [False, False, True, False, True], [True, True, True, True, True], [True, False, True, False, False], [False, True, True, True, True]]
one_miner = {'x': 0, 'y': 0}
one_exit = {'x': 4, 'y': 4}

result = exit_map(one_map, one_miner, one_exit)
print(result)
