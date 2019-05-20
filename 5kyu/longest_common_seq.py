# ----- Problem: Longest Common Sequence (5ku)
# ----- URL: https://www.codewars.com/kata/52756e5ad454534f220001ef
from itertools import combinations


def longest_common_seq(_str1, _str2):
    """
    (string, string) -> (string)
    :param _str1: string with a sequence of characters
    :param _str2: another string
    :return: string with the longest common sequence

    :examples:
    ('abcdef',  'abc') -> 'abc'
    ('132535365', '123456789') -> '12356'

    """

    # find all sequences from both strings
    seqs_str1 = find_seqs(_str1)
    seqs_str2 = find_seqs(_str2)

    winner = ''
    w_len = 0
    for seq in seqs_str1:
        if seq in seqs_str2:
            if len(seq) > w_len or not winner:
                winner = seq
                w_len = len(seq)

    winner_str = ''
    for ch in winner:
        winner_str += ch

    return winner_str


def find_seqs(mystr):
    mystr = list(mystr)
    seqs = []
    for i in range(1, len(mystr) + 1):
        seqs.extend(combinations(mystr, i))

    return seqs


# ----- MAIN CODE --------------------------------------------------
my_str1 = '132535365'
my_str2 = '123456789'
result = longest_common_seq(my_str1, my_str2)
print(result)
