# ----- Problem: Tic-Tac-Toe Checker (5ku)
# ----- URL: https://www.codewars.com/kata/525caa5c1bf619d28c000335


def ttt_checker(_board):
    """
    (list)
    :param _board: list with 3x3 board having 0(empty), 1(X) or 2(O) in each cell
    :return: -1 not yet finished, 1 X won, 2 O won, 0 it's a draw

    :description:
    Tic Tac Toe is a game where you play in a 3x3 board putting X and 0 until you completer a line
    which means you won.

    :algorithm:
    1. Extract from _board every possible combination of three cells that may signal victory if full with same number
    2. Check if any combination leads to victory -> return number in victory combination (1 or 2)
    3. If there is an empty cell -> return -1 (not finished)
    4. If there is no victory combination -> return 0(draw)

    :example:
    my_board = [[1, 2, 1], [2, 1, 2], [1, 2, 1]]  # returns 1

    """

    # 1. Extract possible winning combinations
    combinations = []
    combinations.append([_board[0][0], _board[0][1], _board[0][2]])  # top row
    combinations.append([_board[1][0], _board[1][1], _board[1][2]])  # middle row
    combinations.append([_board[2][0], _board[2][1], _board[2][2]])  # bottom row

    combinations.append([_board[0][0], _board[1][0], _board[2][0]])  # left column
    combinations.append([_board[0][1], _board[1][1], _board[2][1]])  # middle column
    combinations.append([_board[0][2], _board[1][2], _board[2][2]])  # right column

    combinations.append([_board[0][0], _board[1][1], _board[2][2]])  # left to right diagonal
    combinations.append([_board[0][2], _board[1][1], _board[2][0]])  # right to left diagonal

    # 2. Check if any combination leads to victory
    for combination in combinations:
        if combination[0] == combination[1] == combination[2] and combination[0] != 0:
            return combination[0]

    # 3. Game is not finished yet if there is an empty cell
    for row in _board:
        for cell in row:
            if cell == 0:
                return -1

    # 4. If there is no victory combination, then is a draw
    return 0


# ------------------------- MAIN BOARD -------------------------
my_board = [[0, 1, 1], [2, 0, 2], [2, 1, 0]]  # returns 1
result = ttt_checker(my_board)
print(result)
