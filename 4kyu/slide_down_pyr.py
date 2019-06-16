# ----- Problem: Pyramid Slide Down (4kyu)
# ----- URL: https://www.codewars.com/kata/551f23362ff852e2ab000037
# ----- HELP: https://www.youtube.com/watch?v=VENf0GXRd6E


# ---------------------------------------------------------------------------
#       COMMENTS
# ---------------------------------------------------------------------------
#       The problems requires you to find the longest path sliding down a pyramid.
#           I solved this by finding the max of the pyramid and updating every cell to max - cell_value.
#           I call this: finding the mirror pyramid
#
#       Then I used Dijkstra for finding shortest path in the mirror which indicates the longest path
#           in the original pyramid. So, the problem requires to implement Dijkstra
#
#     :algo:
#     Dijkstra for shortest path
#     In the worst case Dijkstra requires to find every possible combination, nevertheless this worst case almost
#     never happens. Dijkstra states that you should carry on trough one path until you find it's sum is too high
#     and there is another path with lower cost(at least the next cell has lower cost):
#     In the case:
#     1 1 1 1
#     7 9 9 1
#     1 9 9 1
#     1 9 9 9
#     0 0 0 0
#
#     Starting in the 1 at the top-left, Dijkstra will carry to the path of 1s to the right and
#     then will go down until he reaches the dead-end with 9s.
#     Then he'll go back and try jumping trough 7 because 1 + 1 + 1 + 1 + 1 + 9 = 14 is higher than 7.
#     The he'll keep going down until he reaches 0, which in this case is an exit.
#
#     :example 1:
#     [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]] -> 23
#
#           /3/
#         \7\  4
#       2  \4\  6
#      8  5 \9\  3
#
#     where 3 + 7 + 4 + 9 = 23
#
#     The steps are:
#         1. Find mirror:
#               7
#             3  6
#           8  6  4
#         2  5  1  7
#
#         list has (position, sum)
#         2. paths = [
#                     [(0, 0), 7] # <0 split this one since it's the only one
#                    ]
#
#         3. paths = [
#                     [(0,0), (1, 0)], 10]  <- split this one since it has lower sum (10)
#                     [(0,0), (1, 1)], 13]
#                    ]
#
#         4. paths = [
#                     [(0,0), (1, 0), (2, 0)], 18]
#                     [(0,0), (1, 0), (2, 1)], 16]
#                     [(0,0), (1, 1)], 13, 7] <-
#                    ]
#
#         5. paths = [
#                     [(0,0), (1, 0), (2, 0)], 18]
#                     [(0,0), (1, 0), (2, 1)], 16] <-
#                     [(0,0), (1, 1), (2, 1)], 19] X erase (head of path (2,1) was reached by another path with lower cost)
#                     [(0,0), (1, 1), (2, 2)], 17]
#                    ]
#
#         6. paths = [
#                     [(0,0), (1, 0), (2, 1), (3, 1)], 21]
#                     [(0,0), (1, 0), (2, 1), (3, 2)], 17] <- winner (it's the lower cost and it's already at the end)
#                     [(0,0), (1, 0), (2, 0)], 18]
#                     [(0,0), (1, 1), (2, 2)], 17]
#                    ]
#
#         So higher sum is original matrix is (0,0) + (1, 0) + (2, 1) + (3, 2)
#                                               3   +   7    +    4   +   9    = 23
#
#         *if two path have equal weight -> follow longest (closer to the end) (this is not original Dijkstra)
#         *if hops are also equal -> just go left
#         ** The implemented algorithm doesn't store the whole path, it just stores the last node for increasing speed
#         ** The implemented algorithm doesn't  compute the mirror either, also for increasing speed it only finds mirror
#            value for cells that are being traversed by a valid path
#         *** The implementation stores every visited cell and it's weight. When a path move to a new cell, the algo
#             verifies that this cell has not been previously visited or it had a longest path when visited, otherwise
#             it kills that path because another better path already went that way
#
#         ** The implemented algorithm stores for every path (pos, sum_mirror, sum_weight) and returns sum_weight at the end
#         Here are the same steps as before, but as the algo actually implements them
#         1. # No need to find mirror
#
#         2. paths = [
#                     [(0, 0), 7, 3] # position, sum_mirror, sum_weight
#                    ]
#
#         3. paths = [
#                     [(1, 0)], 10, 10]  <- split this one
#                     [(1, 1)], 13, 7]
#                    ]
#
#         4. paths = [
#                     [(2, 0)], 18, 12]
#                     [(2, 1)], 16, 14]
#                     [(1, 1)], 13, 7] <-
#                    ]
#
#         5. paths = [
#                     [(2, 0)], 18, 12]
#                     [(2, 1)], 16, 14] <-
#                     [(2, 1)], 19, 11] X erase
#                     [(2, 2)], 17, 13]
#                    ]
#
#         6. paths = [
#                     [(3, 1)], 21, 19]
#                     [(3, 2)], 17, 23] <- winner
#                     [(2, 0)], 18, 12]
#                     [(2, 2)], 17, 13]
#                    ]
#
#
#     :example 2:
#
#     [
#                          [75],
#                        [95, 64],
#                       [17, 47, 82],
#                     [18, 35, 87, 10],
#                    [20, 4, 82, 47, 65],
#                   [19, 1, 23, 75, 3, 34],
#                 [88, 2, 77, 73, 7, 63, 67],
#               [99, 65, 4, 28, 6, 16, 70, 92],
#            [41, 41, 26, 56, 83, 40, 80, 70, 33],
#          [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#         [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#       [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#      [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#     [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
#     ] -> 1074
#
#                             longest path
#                                |75|
#                               95  |64|
#                             17  47  |82|
#                           18  35  |87| 10
#                         20   4  |82| 47  65
#                       19   1  23   |75|   3  34
#                     88   2  77   |73|  7  63  67
#                   99  65   4  |28|   6  16  70  92
#                 41  41  26  56  |83|   40  80  70  33
#               41  48  72  33  47  |32|  37  16  94  29
#             53  71  44  65  25  43  |91|   52  97  51  14
#           70  11  33  28  77  73  17  |78|   39  68  17  57
#         91  71  52  38  17  14  91  43   |58| 50  27  29  48
#       63  66   4  68  89  53  67  30  |73|  16  69  87  40  31
#      4  62  98  27  23   9  70  98  73  |93|  38  53  60   4  23
#
#     93+73+58+78+91+32+83+28+73+75+82+87+82+64+75 = 1074
#
#
#                                 mirror
#                                  |25|
#                                 5  |36|
#                             83   53  |18|
#                           82  65   |13|   90
#                         80   96   |18|   53  35
#                       81   99  77   |25|   97  66
#                     12   98  33   |27|   93  37  33
#                   1  35   96   |72|   94  84  30  8
#                 59  59  74  44   |17| 60  20  30  77
#               59  52  28  77   53  |68|  63  84  6  71
#              47  29  66  35  75  57  |9|  48  3  49  86
#           30  89  23  72  33  27  83  |22|  61  32  83  43
#          9   29  48  62  83  86   9  57  |42|  50  73  71  52
#       37  34   96  32  11  47  33  60 |27| 84  31  13  60  69
#      96  38  2  73  77   91  30  2  27  |7|  62  47  40  96  77


def slide_down_pir(_pyr):
    """
    (list_of_list_of_int) -> list_of_int
    :param _pyr: list with internal list having rows of the pyramid, where each cell of row has a weight(number)
    :return: list_of_int with the max sum of sliding down the pyramid

    This is the main function, the comments at the start of file belong to this function
    """

    # set-up
    base = max(max(_pyr))  # base is used to find mirror_pyr
    last_row = len(_pyr) - 1

    # ini paths with top of _pyr
    paths = [[
        (0, 0),             # position of head of path
        base - _pyr[0][0],  # value for shortest path
        _pyr[0][0]          # value for higher sum
    ]]

    # ini visited_cells
    visited = {}

    # split paths until you get to bottom
    while True:
        # sort by lower weight and then longer path (this puts on top the next candidate_path)
        paths.sort(key=lambda x: (x[1], -x[0][0]))
        candidate = paths.pop(0)

        # if candidate is at bottom -> best candidate_path found
        cand_row = candidate[0][0]
        if cand_row == last_row:
            break

        # save candidate as visited before splitting(go down the path)
        visited.setdefault(candidate[0], 0)
        visited[candidate[0]] = candidate[1]

        # split candidate in two different paths
        new_cand1, new_cand2 = split_candidate(candidate, _pyr, base)
        save_paths(new_cand1, new_cand2, paths, visited)

    # candidate found -> return higher_sum (longest_path)
    return candidate[2]


def save_paths(_c1, _c2, _paths, _visited):
    """
    Saves 'candidates'(_c1, _c2) into the 'paths'.
    If the cell of a candidate matches a cell of another path(rival) in 'paths'
        If candidate has lower path -> candidate replaces rival
        Else candidate is drop and rival stays.

    ElIf the cell of a candidate is found in visited_cells
        If candidate has longer path -> drop candidate
        Else candidate is added to 'paths'

    :example:
    _paths = [
        [(2, 0)], 18, 12],
        [(2, 1)], 16, 14]
    ]

    _c1 = [(2, 1)], 19, 11]  # this one is drop since it has longer path than rival in _path
    _c2 = [(2, 2)], 17, 13]
    """

    # for every candidate
    for _c in [_c1, _c2]:

        # check 'paths' for rivals of _c1 and _c2
        for i, path in enumerate(_paths):

            # if there is a rival -> save candidate if has lower path
            if _c[0] == path[0]:
                rival = path
                if _c[1] < rival[1]:
                    _paths[i] = _c

                break  # it will never be more than one rival so it's safe to stop searching after the first match

        # if no rival was found
        else:
            # if candidate_cell has not been previously visited -> save candidate
            if _c[0] not in list(_visited.keys()):
                _paths.append(_c)

            # if candidate_cell has lower path than visited -> save candidate
            elif _c[1] < _visited[_c[0]]:
                _paths.append(_c)


def split_candidate(_cand, _apyr, _b):
    """
    For the input path in _cand it produces two new paths by moving down_left and down_right
    _cand = candidate
    _apyr = pyramid
    _b    = base

    :example:
        _cand = [(1, 0),  7]
             -> [(2, 0), 15]
             -> [(2, 1), 18]
    """

    # store position of current candidate(head of path)
    x = _cand[0][0]
    y = _cand[0][1]

    # find positions for two new candidates (for (1,0) make (2,0) and (2,1))
    x1 = x + 1
    y1 = y + 0
    x2 = x + 1
    y2 = y + 1

    # sum new weight to accumulated path
    acc = _cand[-2]
    asum = _cand[-1]
    v1 = acc + _b - _apyr[x1][y1]
    v2 = acc + _b - _apyr[x2][y2]
    sum1 = asum + _apyr[x1][y1]
    sum2 = asum + _apyr[x2][y2]

    # return the candidates
    cand1 = [(x1, y1), v1, sum1]
    cand2 = [(x2, y2), v2, sum2]
    return cand1, cand2


# ----- MAIN CODE --------------------------------------------------
my_pyr = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]

my_pyr = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

result = slide_down_pir(my_pyr)

print(result)
