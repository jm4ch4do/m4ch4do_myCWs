# ----- Problem: Sudoku Solution Validator (4kyu)
# ----- URL: https://www.codewars.com/kata/529bf0e9bdf7657179000008/

def make_row_from_3x3(_row_start, _col_start, _board):
    """
    (int, int, list_9x9) -> list
    :param _row_start: start row for the 3x3_list to be extracted
    :param _col_start: start col for the 3x3_list to be extracted
    :param _board: list_9x9 with ints from 1 to 9

    :return: list with a single row having the same values of the selected 3x3_list


    :description:
    Starting from _row_start and _col_start takes a 3x3 portion of _sudoku a returns it in a single row

    :example:
    (input)
    _row_start = 6
    _col_start = 6
    _sudoku = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    (explanatory_var) this var doesn't really exists
    selected3x3 = [
        [2, 8, 4],
        [6, 3, 5],
        [1, 7, 9]
    ]
    (output)
    selected_to_row = [2, 8, 4, 6, 3, 5, 1, 7, 9]
    """
    range_col = list(range(0+_col_start, 3+_col_start))
    range_row = list(range(0+_row_start, 3+_row_start))
    selected_to_row = [_board[row_i][col_i] for row_i in range_row for col_i in range_col]
    return selected_to_row


def is_row_valid(_row):
    """
    (list_of_int) -> (Boolean)
    :param _row: list_of_int with 9 int between 1 and 9
    :return: True if _row has exclusively every number between 1 and 9 with no repetition

    :note:
    By first sorting the list, the algorithm gets simpler

    :algorithm:
    1. Sorts the input list
    2. True if list == [1-9]
        .else False
    """

    if sorted(_row) == list(range(1, 10)):
        return True
    else:
        return False


def valid_solution(_board):
    """
    (list_of_list) -> (Boolean)

    :param _board: list with a 9x9 array representing a sudoku game
    :return: True if _sudoku is a valid solution (i.e the sudoku is finished)

    :description:
    For a sudoku match to be finished this conditions must be fulfill
        a-) No pos with 0 value (i.e no empty cells)
        b-) all rows have every number from 1-9
        c-) all cols have every number from 1-9
        d-) all nine 3x3 sub-arrays must have every number from 1-9

    :algorithm:
    1. Return false if there is any cell with 0
    2. Check that every row has [1-9]
    3. Check that every col has [1-9]
    4. Check that every 3x3 has [1-9]

    :helper_functions:
    is_row_valid -> checks for [1-9] in the input row
                 -> also used to check cols
                    (i.e cols are turned into rows an passed to this function)
                 -> also used to check 3x3
                    (i.e same as previous)

    make_row_from_3x3 -> Turns a 3x3 2D_list into a row

    :example:

    _sudoku = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    """

    # 1. Return false if any cell has 0
    for r in range(9):
        for c in range(9):
            if not _board[r][c]:
                return False

    # 2. Check that every row has [1-9]
    for row in _board:
        if not is_row_valid(row):
            return False

    # 3. Check that every col has [1-9]
    for col_i in range(9):
        row_from_col = [_board[row_i][col_i] for row_i in range(9)]
        if not is_row_valid(row_from_col):
            return False

    # 4. Check that every 3x3 has [1-9]
    jump_list = [0, 3, 6]  # start positions for making the nine 3x3_lists
    for row in jump_list:
        for col in jump_list:
            row_from_3x3 = make_row_from_3x3(row, col, _board)
            if not is_row_valid(row_from_3x3):
                return False

    # 5. If everything checks, then return true
    return True


myboard = (
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
)

result = valid_solution(myboard)
print(result)
