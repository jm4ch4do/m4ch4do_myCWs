# ----- Problem: Codewars style ranking system (4kyu)
# ----- URL: https://www.codewars.com/kata/51fda2d95d6efda45e00004e


# --------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION
# --------------------------------------------------------------------------------------------------------------------
#   A user starts at rank -8 and can progress all the way to 8.
#   There is no 0 rank. The next rank after -1 is 1.
#   Users will complete activities. These activities also have ranks.
#   Each time the user completes a ranked activity the user's rank progress is updated based on the activity's rank.
#   The progress earned from the completed activity depends on the user's rank and the activity's rank
#   A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next level.
#   Any remaining progress earned while in the previous rank will be applied towards the next rank's progress.
#   User cannot progress beyond rank 8.
#   The only acceptable ranks are -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8. Any other value raises an error.
#
#   The progress is scored like this:
#       Completing an activity ranked same as use worth 3 points.
#       Completing and activity one rank lower worth 1 point.
#       Any activities two or more ranks lower will be ignored.
#       Completing an activity ranked higher will accelerate the progression based on difference(d).
#           Progress = 10*d*d
#
#   :examples:
#     user(-8) makes act(-7) -> receives 10 progress
#     user(-8) makes act(-6) -> receives 40
#     user(-8) makes act(-5) -> receives 90
#     user(-8) makes act(-4) -> receives 160, resulting in new_rank (-7) and 60 extra progress
#     user(-1) makes act(1) -> receives 10 progress (remember, zero rank is ignored)
#
#     user = User()
#     user.rank # -8
#     user.progress # 0
#     user.inc #


# --------------------------------------------------------------------------------------------------------------
#   MAIN CLASS
# --------------------------------------------------------------------------------------------------------------------
class User:

    # translate codewars ranking into an easier version with only positive integers
    EASY_RANK = {
        -8: 1,
        -7: 2,
        -6: 3,
        -5: 4,
        -4: 5,
        -3: 6,
        -2: 7,
        -1: 8,
        1: 9,
        2: 10,
        3: 11,
        4: 12,
        5: 13,
        6: 14,
        7: 15,
        8: 16,
    }

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, kata_rank):

        # translate codewars ranking into an easier version with only positive integers
        kata_rank = User.EASY_RANK[kata_rank]
        user_rank = User.EASY_RANK[self.rank]

        # no progress increase for if user.rank = 8
        if self.rank == 8:
            return

        # kata_rank is much lower(two ranks) than user_rank -> ignore
        elif kata_rank <= user_rank - 2:
            return

        # kata_rank is one_rank lower than user_rank -> add 1 progress
        elif kata_rank <= user_rank - 1:
            self.progress += 1

        # kata_rank same rank than user_rank -> add 3 progress
        elif kata_rank == user_rank:
            self.progress += 3

        # kata_rank is higher than user_rank -> apply super_progress formula
        elif kata_rank > user_rank:

            # find rank difference
            d = kata_rank - user_rank

            # compute progress
            super_progress = 10 * d * d
            self.progress += super_progress

        # check if progress went beyond 100 and increase rank accordingly
        self.apply_progress()

    def apply_progress(self):

        # if progress < 100 -> no need to increase rank
        if self.progress < 100:
            return

        # if progress < 100 -> increase rank for every 100
        elif self.progress >= 100:
            self.progress -= 100
            self.upgrade_rank()
            self.apply_progress()

        # after rank = 8 progress is forced to 0
        if self.rank == 8:
            self.progress = 0

    def upgrade_rank(self):

        # no upgrades beyond max rank
        if self.rank == 8:
            return

        # rank -1 upgrades to 1
        elif self.rank == -1:
            self.rank = 1

        # otherwise -> increase one rank
        else:
            self.rank += 1

# --------------------------------------------------------------------------------------------------------------------
#   TEST SAMPLES
# --------------------------------------------------------------------------------------------------------------------
user = User()
my_current_rank = user.rank  # => -8
my_current_progress = user.progress  # => 0
user.inc_progress(-7)
my_new_progress = user.progress  # => 10
user.inc_progress(-5)  # will add 90 progress
my_new_new_progress = user.progress  # => 0 # progress is now zero
my_new_new_rank = user.rank  # => -7 # rank was upgraded to -7
