# ----- Problem: Molecule to atoms (5ku)
# ----- URL: https://www.codewars.com/kata/52f831fa9d332c6591000511


def count_atoms(_formula):
    """
    (string) -> (dict)
    :param _formula: string with a chemical formula of a given molecule
    :return: dict with amount of every type of atom in the molecule

    :description:
    For a given chemical formula represented by a string, count the number of atoms of each element contained
    in the molecule and return an object

    :algorithm:
    _formula = 'Mg4[ON(SO3)20]2'
    1. Split symbols
        Split similar to list(my_string), but has two differences:
        a-) Maintaining together lower with previous upper (ex. 'Mg')
        b-) Also keeps together number with previous number (ex. '20')
        -> symbols = ['Mg', '4', '[', 'O', 'N', '(', 'S', 'O', '3', ')', '20', ']', '2']
    2. Count atoms
       Uses generator select_atom to get atoms one by one
       For each atom
       -> atoms = {'Mg': 4, 'S': 40, 'O': 122, 'N': 2}


    :examples:
    water = 'H2O'
    count_atoms(water)  # returns {'H': 2, 'O': 1}

    magnesium_hydroxide = 'Mg(OH)2'
    count_atoms(magnesium_hydroxide)  # return {'Mg: 1, 'O':2, 'H': 2'}

    fremy_salt = 'K4[ON(SO3)2]2'
    count_atoms(fremy_salt)  # return {'K': 4, 'O': 14, 'N': 2, 'S': 4}

    difficult = 'Mg4[ON(SO3)20]2'
    count_atoms(fremy_salt)  # return {'Mg': 4, 'S': 40, 'O': 122, 'N': 2}
    """
    # 1. Split symbols:
    #   unite lowercase with previous character ('M' followed by 'g' is really 'Mg')
    #   and number with previous number, if there is any ('1' followed by '0' is really a '10')
    symbols = []
    was_number = False
    for i, ch in enumerate(_formula):
        # is lower -> goes with previous Upper
        if ch.islower():
            previous = symbols.pop()
            symbols.append(previous + ch)
            was_number = False

        # is number -> goes with previous number if previous exists, otherwise goes alone
        elif ch in '1234567890':
            if was_number:
                previous = symbols.pop()
                symbols.append(previous + ch)
            else:
                symbols.append(ch)
            was_number = True

        # is upper or in '[](){}' -> goes alone
        else:
            symbols.append(ch)
            was_number = False

    # 2. Count atoms
    atoms = {}  # output dictionary
    gen_select_atom = select_atom(symbols)  # call generator to return symbols one by one
    while True:
        # get atoms one by one
        atom_pos, atom_name = next(gen_select_atom)
        if atom_name is None:
            break

        # save atom count to output dict
        count = count_atom(atom_pos, symbols)
        atoms.setdefault(atom_name, 0)
        atoms[atom_name] += count

    return atoms


def count_atom(_pos, _symbols):
    """
    (int, list_of_string) -> int
    :param _pos: int with index of atom_name(selected atom) in _symbols
    :param _symbols: list_of_string where each string has a symbols from original _formula
    :returns _multiplier: int with multiplier of symbol in _pos inside _symbols

    :example:
    _pos = 5  # 'S'
    _symbols = ['Mg', '4', '[', 'O', 'N', '(', 'S', 'O', '3', ')', '20', ']', '2']
    -> _multiplier = 40


    :description:
    every atom(symbol) gets multiplied by the consecutive number(to the right) , if there is one
    it also gets multiplied by every other number to the right(not consecutive),
        which is next to an unbalanced closing parenthesis
        An unbalanced closing parenthesis is one for which there is no previous open parenthesis to the right of _pos

    """
    # set-up
    was_unbalanced = False
    _multiplier = 1
    open_par = []  # open parenthesis

    # check every symbol
    for i, sym in enumerate(_symbols[_pos+1:]):
        # C1. first time rule, if number -> multiply  (ie. in K2, multiply K by 2)
        if i == 0 and sym[0] in '1234567890':
            _multiplier *= int(sym)
            continue

        # C2. handle numbers -> multiply if was_unbalanced (ie. in 'K2)3', multiply also by 3)
        if sym[0] in '1234567890':
            if was_unbalanced:
                _multiplier *= int(sym)
                was_unbalanced = False
                continue
            else:
                continue

        # C3. handle parenthesis
        if sym in '([{':    # found open parenthesis -> save (ie. in 'K2(', next ')' will be balanced)
            open_par.append(sym)
            was_unbalanced = False
            continue
        elif sym in '})]':  # found close parenthesis
            ref = '' if not len(open_par) else open_par[-1]

            if (sym == ')' and ref == '(') or \
                    (sym == ']' and ref == '[') or \
                    (sym == '}' and ref == '{'):    # balanced -> pop from open_par (ie. in 'K2()', set balanced = True)
                open_par.pop()
                was_unbalanced = False
                continue
            else:          # unbalanced -> flag = True (ie. in 'K2)', is unbalanced so be ready for next number)
                was_unbalanced = True
                continue

        # C4. ignore other symbols
        was_unbalanced = False

    return _multiplier


def select_atom(_symbols):
    for i, value in enumerate(_symbols):
        if value[0] not in '[](){}1234567890':
            yield i, value

    yield None, None


# ------------------------- MAIN CODE -------------------------
fremy_salt = 'As2{Be4C5[BCo3(CO2)3]2}4Cu5'
result = count_atoms(fremy_salt)
print(result)
