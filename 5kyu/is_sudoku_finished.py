# ----- Problem: Did I Finish my Sudoku (5ku)
# ----- URL: https://www.codewars.com/kata/53db96041f1a7d32dc0004d2


def is_sudoku_finished(_board):
    """
    (list2D_of_ints) -> Boolean
    :param _board: 2D-list of its representing a sudoku board or table or puzzle
    :return: True if sudoku is properly solved

    :example:
    _board = [
        [1, 3, 2, 5, 7, 9, 4, 6, 8],
        [4, 9, 8, 2, 6, 1, 3, 7, 5],
        [7, 5, 6, 3, 8, 4, 2, 1, 9],
        [6, 4, 3, 1, 5, 8, 7, 9, 2],
        [5, 2, 1, 7, 9, 3, 8, 4, 6],
        [9, 8, 7, 4, 2, 6, 5, 3, 1],
        [2, 1, 4, 9, 3, 5, 6, 8, 7],
        [3, 6, 5, 8, 1, 7, 9, 2, 4],
        [8, 7, 9, 6, 4, 2, 1, 5, 3]
    ] -> 'Finished!'

    _board = [
        [1, 3, 2, 5, 7, 9, 4, 6, 8],
        [4, 9, 8, 2, 6, 1, 3, 7, 5],
        [7, 5, 6, 3, 8, 4, 2, 1, 9],
        [6, 4, 3, 1, 5, 8, 7, 9, 2],
        [5, 2, 1, 7, 8, 3, 8, 4, 6],
        [9, 8, 7, 4, 2, 6, 5, 3, 1],
        [2, 1, 4, 9, 3, 5, 6, 8, 7],
        [3, 6, 5, 8, 1, 7, 9, 2, 4],
        [8, 7, 9, 6, 4, 2, 1, 3, 5]
    ] -> 'Try Again!'

    """
    # check rows
    for row in _board:
        if not check_rows(row):
            return 'Try Again!'

    # check columns
    for c in range(len(_board[0])):  # c is column index
        column_as_row = []
        for r in range(len(_board)):  # r is row index
            column_as_row.append(_board[r][c])

        if not check_rows(column_as_row):
            return 'Try Again!'

    # check squares
    ini_squares = [0, 3, 6]  # initial positions for squares
    for r in ini_squares:
        for c in ini_squares:
            square_as_row = make_square_as_row(r, c, _board)
            if not check_rows(square_as_row):
                return 'Try Again!'

    # No problem -> return True
    return 'Finished!'


def check_rows(_row):
    return True if sorted(_row) == [1, 2, 3, 4, 5, 6, 7, 8, 9] else False


def make_square_as_row(_r, _c, _aboard):
    len_squares = 3
    row = []
    for r_add in range(len_squares):
        for c_add in range(len_squares):
            cell = _aboard[_r + r_add][_c + c_add]
            row.append(cell)

    return row

# ----- Main Code
my_board1 = [
    [1, 3, 2, 5, 7, 9, 4, 6, 8],
    [4, 9, 8, 2, 6, 1, 3, 7, 5],
    [7, 5, 6, 3, 8, 4, 2, 1, 9],
    [6, 4, 3, 1, 5, 8, 7, 9, 2],
    [5, 2, 1, 7, 9, 3, 8, 4, 6],
    [9, 8, 7, 4, 2, 6, 5, 3, 1],
    [2, 1, 4, 9, 3, 5, 6, 8, 7],
    [3, 6, 5, 8, 1, 7, 9, 2, 4],
    [8, 7, 9, 6, 4, 2, 1, 5, 3]
]

my_board2 = [
    [1, 3, 2, 5, 7, 9, 4, 6, 8],
    [4, 9, 8, 2, 6, 1, 3, 7, 5],
    [7, 5, 6, 3, 8, 4, 2, 1, 9],
    [6, 4, 3, 1, 5, 8, 7, 9, 2],
    [5, 2, 1, 7, 8, 3, 8, 4, 6],
    [9, 8, 7, 4, 2, 6, 5, 3, 1],
    [2, 1, 4, 9, 3, 5, 6, 8, 7],
    [3, 6, 5, 8, 1, 7, 9, 2, 4],
    [8, 7, 9, 6, 4, 2, 1, 3, 5]
]

result = is_sudoku_finished(my_board1)
print(result)
