# ----- Problem: Matrix Determinant (4kyu)
# ----- URL: https://www.codewars.com/kata/52a382ee44408cea2500074c


# --------------------------------------------------------------------------------------------------------------------
#   PURPOSE
# --------------------------------------------------------------------------------------------------------------------
# Find the determinant of a given matrix entered as a list_of_list_of_ints.
# The determinant is an algebraic operation only valid for squared matrices.

# This implementation uses the Laplace Expansion method for computing the determinant.
# There are other methods but Laplace Expansion is usually the basic because is easy to remember.
# Besides, it was the method suggested in the description of the problem.


# --------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION
# --------------------------------------------------------------------------------------------------------------------
# Laplace Expansion method for computing the determinant of a matrix goes as follows:

# The determinant of a 1x1 matrix is:
#       matrix = [ a ]
#       determ = a

# The determinant of a 2x2 matrix is:
#       matrix = [
#                   [ a, b ]
#                   [ c, d ]
# ]
#
#       determ = a * d - b * c

# The determinant of a 3x3 matrix is:
#       matrix = [
#                   [ a, b, c ]
#                   [ d, e, f ]
#                   [ g, h, i ]
# ]
#
#       determ = a * determ([[e,f],[h,i]]) +
#               -b * determ([[f,d],[i,g]]) +
#                c * determ([[d,e],[g,h]])

# The determinant of a 4x4 or 5x5 or larger matrix is found using the same method that for 3x3
# but it requires more iterations for finding the result

# Assuming the the values from the first row are 'kings' and the rest of the values are 'soldiers'
# Every king is multiplied by 1 or -1 alternatively
# Every king is also multiplier by the determ of his soldiers (soldiers away from the king's row and column)
# The determ of the king's soldier is refer to as the king's strength
# The final result is the sum of every king's strength (the whole multiplication of alter*king*strength)


# --------------------------------------------------------------------------------------------------------------------
#   ALGORITHM
# --------------------------------------------------------------------------------------------------------------------
# As main function a used a recursively function that returns the direct result for 1x1 or 2x2 matrices and calls
# itself for larger matrices after dividing the problem in smaller pieces as recommended in the Laplace Exp. method.

# I also used an auxiliary function for selecting the soldiers of a given king


# --------------------------------------------------------------------------------------------------------------------
#   MAIN FUNCTION
# --------------------------------------------------------------------------------------------------------------------
def find_det(matrix):
    """
    (list_of_list_of_ints) -> (int)
    :param matrix: list_of_list_of_ints representing a matrix
    :return: Determinant of a given matrix

    """
    # set-up
    rows, cols = len(matrix), len(matrix[0])

    # one cell matrix -> determ is the only value in matrix
    if rows == cols == 1:
        return matrix[0]

    # 2x2 matrix -> use standard method
    if rows == cols == 2:
        a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
        return a * d - b * c

    # matrix larger than 2x2 -> divide in smaller matrices
    kings, soldiers = matrix[0], matrix[1:]
    sign = -1
    armies = []

    for k, king in enumerate(kings):
        sign *= -1
        king_soldiers = select_soldiers(k, soldiers)
        king_strength = find_det(king_soldiers)
        armies.append(sign*king*king_strength)

    return sum(armies)


# --------------------------------------------------------------------------------------------------------------------
#   AUXILIARY FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------
def select_soldiers(_k, _soldiers):
    """
    (int, list_of_list_of_int) -> list_of_list_of_int
    :param _k: the king doesn't want soldier from this column
    :param _soldiers: 2D matrix with all available solider
    :return: 2D matrix with selected soldiers
    """
    selected_soldiers = []

    # check every soldier for selection
    for r in range(len(_soldiers)):  # r = rows
        line = []

        for c in range(len(_soldiers[0])):  # c = # cols
            # use only soldiers whose column is different from the king's column
            if c != _k:
                new_soldier = _soldiers[r][c]
                line.append(new_soldier)

        # save soldier in the line
        selected_soldiers.append(line)

    return selected_soldiers


# --------------------------------------------------------------------------------------------------------------------
#   TEST SAMPLES
# --------------------------------------------------------------------------------------------------------------------
my_matrix = [
    [ 3,  8],
    [ 4,  6]
]

result = find_det(my_matrix)
print(result)  # -14

# ---------------------------
my_matrix = [
    [ 6,  1, 1],
    [ 4, -2, 5],
    [ 2,  8, 7]
]

result = find_det(my_matrix)
print(result)  # -306

# ---------------------------
my_matrix = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
]

result = find_det(my_matrix)
print(result)  # 0
