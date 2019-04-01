# ----- Problem: Where my anagrams at? (5ku)
# ----- URL: https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def find_anagrams(_ref, _candidates):
    """
    (string, list_of_string) -> list_of_string
    :param _ref: string with a reference word to compared for anagrams
    :param _candidates: list with candidates strings to be compared with _ref for anagrams
    :return: list of string with candidates that were suitable anagrams

    :descriptions:
        anagramas are words with the same letter arranged in different order

    :examples:
        find_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) -> ['aabb', 'bbaa']
        find_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) -> ['carer', 'racer']
        find_anagrams('laser', ['lazing', 'lazy', 'lacer']) -> []
    """
    anagrams = [word for word in _candidates if sorted(word) == sorted(_ref)]
    return anagrams


result = find_anagrams('laser', ['lazing', 'lazy', 'lacer'])
print(result)
