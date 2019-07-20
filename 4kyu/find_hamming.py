# ----- Problem: Hamming Numbers (4kyu)
# ----- URL: https://www.codewars.com/kata/526d84b98f428f14a60008da


# --------------------------------------------------------------------------------------------------------------------
#   PURPOSE
# --------------------------------------------------------------------------------------------------------------------
# Function that output the nth smallest requested hamming number
# (i.e. find_hamming(10) means give the the 10th smaller hamming number)

# Hamming numbers are given by: 2**i * 3 **j * 5 ** k where i, j, k are non-negative integers
# To find the next smaller hamming number you find out if the next smaller is obtained by increasing i, j or k


# --------------------------------------------------------------------------------------------------------------------
#   ALGORITHM
# --------------------------------------------------------------------------------------------------------------------
# This problem can be solved using a genetic algorithm.
# Start i, j, k with 0 and increase one of then in three separated instances (make three mutations).
# The resulting smaller instance wins and goes forward (the smaller mutation prevails, the others wait)
# The winner mutation mutates again into three possible variations, so now you have two previous mutations + three new

# This differs from traditional genetic algorithm were losing mutations die, but is just more fun to use mutation as
# a variable name :)

# The problem test cases ask for the first, second, third and so on until the 1999 smaller hamming number
# I just used input 2000 and then stored partial results from 1 to 1999, for latter use in memoization.

# --------------------------------------------------------------------------------------------------------------------
#   MAIN FUNCTION
# --------------------------------------------------------------------------------------------------------------------
previous = {}  # global variable for memoization


def find_hamming(n):
    """
    :param n: (int) number of the requested smaller hamming number
    :return: (int) value of the requested smaller hamming number
    """
    # check if result was previously computed
    global previous
    if n in previous.keys():
        return previous[n]

    # set-up
    leading_mutation = [[0, 0, 0], 1]
    count = 0  # counts until it gets to requested n
    mutations = []

    # keep counting until you reach n
    while count < n-1:
        # count one iteration
        count += 1

        # copy data from leading mutation
        i, j, k = leading_mutation[0]

        # create three new mutations from leading mutation
        mutation_i = [(i + 1, j, k), formula(i + 1, j, k)]
        mutation_j = [(i, j + 1, k), formula(i, j + 1, k)]
        mutation_k = [(i, j, k + 1), formula(i, j, k + 1)]

        # save new mutations if they were not yet in the list
        for mut in [mutation_i, mutation_j, mutation_k]:
            if mut not in mutations:
                mutations.append(mut)

        # find new leading mutation (the one with lower weight)
        mutations.sort(key=lambda x: x[1])
        leading_mutation = mutations.pop(0)

        # save current mutation for memoization
        previous[count+1] = leading_mutation[1]

    # return hamming number when count == n
    return leading_mutation[1]


# --------------------------------------------------------------------------------------------------------------------
#   AUXILIARY FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------
def formula(i, j, k):
    """
    (int, int, int) -> (int)
    It implements the formula for hamming number hamming
    """

    return 2**i * 3**j * 5**k


# --------------------------------------------------------------------------------------------------------------------
#   TEST SAMPLES
# --------------------------------------------------------------------------------------------------------------------
print(find_hamming(2000))
print(find_hamming(2))  # 2
print(find_hamming(3))  # 3
print(find_hamming(4))  # 4
print(find_hamming(5))  # 5
print(find_hamming(6))  # 6
print(find_hamming(7))  # 8
print(find_hamming(8))  # 9
print(find_hamming(10))  # 12
print(find_hamming(11))  # 15
print(find_hamming(12))  # 16
print(find_hamming(13))  # 18
print(find_hamming(14))  # 20
print(find_hamming(15))  # 24
print(find_hamming(16))  # 25
print(find_hamming(17))  # 27
print(find_hamming(18))  # 30
print(find_hamming(19))  # 32
