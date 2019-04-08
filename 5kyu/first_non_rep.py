# ----- Problem: First non-repeating character (5ku)
# ----- URL: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e


def first_non_rep(_chs):
    """
    (string) -> (string)
    :param _chs: string with a word
    :return: string with first character that is not repeated in _chs
             all letter must be read in lower but returned in their original case

    :example:
    ('stress') -> ('t')
    """

    # ---- initialize
    rep, nrep = [], []  # list for storing repeated and not repeated letters
    lower_chs = _chs.lower()  # lowercase will match uppercase

    # ---- check every character
    for ch in lower_chs:

        # -- verify conditions
        # character may be in nrep, rep or neither
        ch_in_nrep = ch in nrep

        # it can only be in rep in it was not in nrep
        ch_in_rep = ch in rep if not ch_in_nrep else False

        # -- insert to lists depending on conditions
        if (not ch_in_nrep) and (not ch_in_rep):  # new character -> append in nrep
            nrep.append(ch)
        elif ch_in_nrep:  # non-repeated character -> remove from nrep, append in rep
            nrep.remove(ch)
            rep.append(ch)

    # ---- return
    _output = nrep[0] if nrep else ''
    if not _output:  # return empty string for no-match
        return ''
    else:  # make sure ch is returned in its original case
        for ch in _chs:
            if ch.lower() == _output:
                return ch


my_chs = 'sTreSS'
result = first_non_rep(my_chs)
expected = 't'
print(result)
