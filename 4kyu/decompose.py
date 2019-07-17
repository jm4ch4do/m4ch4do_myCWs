# ----- Problem: Square into Squares. Protect trees! (4kyu)
# ----- URL: https://www.codewars.com/kata/54eb33e5bc1a25440d000891


# --------------------------------------------------------------------------------------------------------------------
#   PURPOSE
# --------------------------------------------------------------------------------------------------------------------
# For a given int(n) find all combinations of successions of ints lower than n that sum n_squared after being squared
# Then return the combination with the larger possible value


# --------------------------------------------------------------------------------------------------------------------
#   EXAMPLE
# --------------------------------------------------------------------------------------------------------------------
# If n = 11 the n_squared = 121
# Then these two combinations are possible
# [1, 2, 4, 10] whose squared_sum is 1 + 4 + 16 + 100 = 121
# and
# [2, 6, 9] whose squared_sum is 4 + 36 + 81 = 121
# you should return the first one since 10 is higher than 9


# --------------------------------------------------------------------------------------------------------------------
#   ALGORITHM
# --------------------------------------------------------------------------------------------------------------------
# I used three functions. The first and the last are really simple, just the second one has a little complexity.

# First function initialises the list of candidates for making the sum of squares (ex. [1, 2, 4, 10])
# (in the example, candidates will be all integers from 1 to 10 because n = 11 )

# Then the first function calls the second function which is a recursive function, that will select one candidate
# and combine it with all others to check whether 10 was suitable starter for the output list.
# The second function will combine the for 9, 8, ... 1 until it finds one match, in which case it stops.

# The third function is auxiliary for computing the square of all number in a list and the the sum. This is necessary
# for the algorithm in function two.

# Example:
# Function one gets n = 11
# Function two gets _n = 11, _candidates = [1,2,3,4,5,6,7,8,9,10], _selected = []  # no initial selection
# Function two selects first candidate so _selected = [10], since 10**2 = 100 < 11**2 = 121
# Function two calls itself for a new search with _n = 11, _candidates = [1,2,3,4,5,6,7,8,9], _selected = [10]
# Function two tries candidates 9, 8, 7, 6, 5 realizing that they make the squared sum go beyond 121
# Then it finds that 4 was a good candidate but [10, 4] was still below 121 so it call it-self again with
# _n = 11, _candidates = [1,2,3], _selected = [10, 4]
# At this point you probably understood the algorithm
# If no good candidates appear beyond this point it will go back and replace 4 by 3 for selected = [10, 3]
# If this path is no good it will go back to the first call of function two and change 10 for 9 making selected = [9]
# If no combination of candidates is good, every call will return False and the final result will be False.
# The first function turns this False into None which means there is no decomposition for the requested number.


# --------------------------------------------------------------------------------------------------------------------
#   IMPORTS
# --------------------------------------------------------------------------------------------------------------------
from math import sqrt, ceil


# --------------------------------------------------------------------------------------------------------------------
#   MAIN FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------
def decompose(n):
    """
    :param n: (int) number to be decomposed in a sum of squares
    :return: (list_of_ints) squared and them sum these numbers to get n
    """

    # feed initial candidates to recursive function that test them all
    candidates = list(range(1, n))
    final_selection = _decompose(n, candidates, [])

    # return sorted output of recursive function
    return sorted(final_selection) if final_selection else None


def _decompose(_n, _candidates, selected=[]):
    """
    :param _n: (int) number to be decomposed in a sum of squares
    :param _candidates: (list_of_ints) candidates that may be appended to param 'selected'
    :param selected: (list_of_ints) selected numbers to be later squared and summed
    :return: False if 'selected' could not be completed with '_candidates' to make '_n'
             Otherwise, returns the selected candidates stored in 'selected'
    """
    # this avoids computing _n ** 2 several times
    ceiling = _n ** 2

    # keep trying every candidate until you find a good solution of there are no candidates left
    while _candidates:

        # take one candidate and see how the new 'selected' looks
        selected.append(_candidates.pop())
        sum2_selected = find_squared_sum(selected)  # sum2_selected = square and the sum

        # sum2 is perfect -> your done, return selected candidates
        if sum2_selected == ceiling:
            return selected

        # sum2 is too high -> drop last candidate and repeat
        elif sum2_selected > ceiling:
            selected.pop()
            continue

        # sum2 is too low -> this candidate may lead to a perfect selection so try adding more candidates
        elif sum2_selected < ceiling:

            # after adding a new candidate the next suitable will be far away
            # (ex. for n = 11 after taking 10, the next 9 will evidently make selected too high)
            # so remaining stores the next lower candidate that may be suitable
            remaining = ceil(sqrt(ceiling - sum2_selected))

            # no candidates left -> call the next recursion with no candidates left (this will cause a return False)
            if not _candidates:
                available_candidates = []

            # there are more candidates -> call recursion with candidates that are under remaining
            else:
                top = min(max(_candidates), remaining)
                available_candidates = list(range(1, top+1))

                # small fix for the case where the last candidate is [1]
                if not available_candidates and 1 in _candidates:
                    available_candidates = [1]

            # call a new recursion to expand 'selected'
            expanded_selection = _decompose(_n, available_candidates, selected.copy())

            # if selection could not be expanded to find a solution -> drop last candidate and try with next
            if not expanded_selection:
                selected.pop()
                continue

            # if found good expansion of selecction -> you're done, return 'expanded_selection'
            else:
                return expanded_selection

    # if all candidates where tried and no good selection was found -> return False
    else:
        return False


def find_squared_sum(_numbers):
    """
    :param _numbers: (list_of_int) numbers that will be squared before making the sum that will be finally return
    :return: read above
    """
    output = [value**2 for value in _numbers]
    return sum(output)


# --------------------------------------------------------------------------------------------------------------------
#   TEST SAMPLES
# --------------------------------------------------------------------------------------------------------------------
my_n = 6  # None
result = decompose(my_n)
print(result)

my_n = 11  # [1, 2, 4, 10]
result = decompose(my_n)
print(result)

my_n = 12  # [1, 2, 3, 7, 9]
result = decompose(my_n)
print(result)

my_n = 50  # [1, 4, 11, 69, 3912, 7654321]
result = decompose(my_n)
print(result)
