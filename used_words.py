# ----- Problem: Most frequently used words in a text (4kyu)
# ----- URL: https://www.codewars.com/kata/51e056fe544cf36c410000fb

# --------------------------------------------------------------------------------------------------------------------
#   PURPOSE
# --------------------------------------------------------------------------------------------------------------------
# Scan a text and find the most used words, return the three more used in a list

# any letter and ' are considered to form a word. The characters ',', '.', ' ' and others are not part of any word
# words are case insensitive

# --------------------------------------------------------------------------------------------------------------------
#   ALGORITHM
# --------------------------------------------------------------------------------------------------------------------
# 1. Scan the text one character at the time
#   When a word ends -> save it to a counting dictionary

# 2. Scan dictionary for getting the three more used words


# --------------------------------------------------------------------------------------------------------------------
#   MAIN FUNCTION
# --------------------------------------------------------------------------------------------------------------------
def find_most_used(text):

    text = text.lower()

    # scan chs for obtaining words
    word_rep = {}  # word_repetition
    word = ''
    for ch in text:
        ch_is_valid = is_valid(ch)

        # if ch is valid -> append it to current word
        if ch_is_valid:
            word += ch

        # not_valid ch + previous word -> start new word with it
        elif word:
            word_rep.setdefault(word, 0)
            word_rep[word] += 1
            word = ''

        # not_valid ch + no previous word -> go to next ch
        else:
            continue

    # save last word after loop
    else:
        if word:
            word_rep.setdefault(word, 0)
            word_rep[word] += 1

    # erase words containing only one or several '
    to_erase = []
    for word in word_rep.keys():
        if has_only_apost(word):
            to_erase.append(word)

    for value in to_erase:
        word_rep.pop(value)

    # find three most repeated words
    gold_record = silver_record = bronze_record = 0
    gold_word = silver_word = bronze_word = ''
    for word, record in word_rep.items():

        # new gold medal
        if record > gold_record:
            bronze_record, bronze_word = silver_record, silver_word
            silver_record, silver_word = gold_record, gold_word
            gold_record, gold_word = record, word

        # new silver medal
        elif record > silver_record:
            bronze_record, bronze_word = silver_record, silver_word
            silver_record, silver_word = record, word

        # new bronze medal
        elif record > bronze_record:
            bronze_record, bronze_word = record, word

    # return the three highest, but don't return any zeros
    if not gold_record:
        return []
    elif not silver_record:
        return [gold_word]
    elif not bronze_record:
        return [gold_word, silver_word]
    else:
        return [gold_word, silver_word, bronze_word]


# --------------------------------------------------------------------------------------------------------------------
#   AUXILIARY FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------
def is_valid(_ch):
    if _ch in "abcdefghijklmnopqrstuvwxyz" or _ch in "'":
        return True
    else:
        return False


def has_only_apost(_word):

    for _ch in _word:
        if _ch == "'":
            continue
        else:
            return False

    return True


# --------------------------------------------------------------------------------------------------------------------
#   TEST SAMPLES
# --------------------------------------------------------------------------------------------------------------------
# my_text = "e e e e DD'D dd'd Dd'D: dd'd. ddd aa aA Aa, bb cc cC e e e"
# result = find_most_used(my_text)
# print(result)  # ["e", "dd'd", "aa"]

my_text = "'''"
result = find_most_used(my_text)
print(result)  # ['e', 'ddd', 'aa']
