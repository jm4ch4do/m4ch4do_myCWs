# ----- Problem: Counting Change Combinations (4kyu)
# ----- URL: https://www.codewars.com/kata/531af676b589989aed0009e7

# --------------------------------------------------------------------------------------------------------------------
#   PURPOSE
# --------------------------------------------------------------------------------------------------------------------
# You are provided with a list of coins and bills (ex. 1dollar coin, 2 dollar coin, 5 dollar bill)
# You are provided with a total amount of money
# You have to find out how many combinations can you made with your coins to make the total amount
# You must assume you have infinite coins or bills of each type.

# --------------------------------------------------------------------------------------------------------------------
#   ALGORITHM
# --------------------------------------------------------------------------------------------------------------------
# I used two function, the first initializes the recursion and the second is the recursion itself

# The recursive function loop trough the coins in inverse order. If it finds a coin that matches the required total
# it increases the amount of posible combinations.

# If a coin surpasses the amount it's dropped

# If a coin is under the amount the function calls itself recursively to re-initialize with
# a lower total = total - previous_coin, and the process it's repeated again
# The combinations found in the recursion are returned to the main function.
# The recursion is repeated as new coins are still smaller than the required total.

# --------------------------------------------------------------------------------------------------------------------
#   EXAMPLE
# --------------------------------------------------------------------------------------------------------------------
# coins = [2, 3, 5]
# total = 10
# result = 4  # 5+5, 5+3+2, 3+3+2+2, 2+2+2+2+2


# --------------------------------------------------------------------------------------------------------------------
#   MAIN FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------
def count_combinations(total, coins):
    """
    :param total: (int) total amount to be decomposed in a sum of coins
    :param coins: (list_of_ints) coins available for making combinations
    :return: (int) amount of combinations that made the requested 'total'
    """
    coins.sort(reverse=True)

    # feed coins to recursive function that finds all possible combinations
    combinations = _count_combinations(total, coins)

    # return sorted output of recursive function
    return combinations


def _count_combinations(_total, _coins):
    """
    :param _total: (int) number to be decomposed in a sum of _coins
    :param _coins: (list_of_ints) coins available for making combinations
    :return: False if 'selected' could not be completed with '_coins' to make '_n'
             Otherwise, returns the selected candidates stored in 'selected'
    """
    combinations = 0

    # keep trying every coin until there are no more combinations to be made
    for i, coin in enumerate(_coins):

        # coin is perfect -> save selected to combination, try next coin for a new combination
        if coin == _total:
            combinations += 1
            continue

        # coin was too high -> try smaller coins
        elif coin > _total:
            continue

        # coin was too low -> last added coin may lead to a good combination so try adding more coins
        else:

            # call a new recursion to add more coins
            remaining_coins = _coins[i:]  # only smaller coins are passed to avoid duplicates
            deeper_combinations = _count_combinations(_total - coin, remaining_coins)
            combinations += deeper_combinations

    return combinations

# --------------------------------------------------------------------------------------------------------------------
#   TEST SAMPLES
# --------------------------------------------------------------------------------------------------------------------
my_coins = [2, 3, 5]
my_total = 10
result = count_combinations(my_total, my_coins)
print(result)  # 4

my_coins = [1, 2, 3]
my_total = 4
result = count_combinations(my_total, my_coins)
print(result)  # 4
