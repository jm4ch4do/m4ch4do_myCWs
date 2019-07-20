# ----- Problem: Roman Numerals Helper (4kyu)
# ----- URL: https://www.codewars.com/kata/51b66044bce5799a7f000003


# --------------------------------------------------------------------------------------------------------------------
#   PURPOSE
# --------------------------------------------------------------------------------------------------------------------
# Create a class for converting from decimal to roman numbers and viceversa

# --------------------------------------------------------------------------------------------------------------------
#   DESCRIPTION
# --------------------------------------------------------------------------------------------------------------------
# Translation of symbols
# | Symbol | Value | | I | 1 |    | V | 5 |    | X | 10 |    | L | 50 |    | C | 100 |    | D | 500 |    | M | 1000 |


# --------------------------------------------------------------------------------------------------------------------
#   ALGORITHM
# --------------------------------------------------------------------------------------------------------------------
# from_roman (ex. 'MCMXC')

# 1. divide characters into symbols (ex. 'MCMXC' -> ['M', 'CM' , 'XC'])
#    note that decreasing characters go together (i.e. 'CM' is decreasing because 'C' is 100 and 'M' is 1000)

# 2. translate symbols into numbers (ex. ['M', 'CM' , 'XC'] -> [1000, 900, 90])
#    note that decreasing numbers subtract 'CM' -> 1000 - 100 = 900

# 3. return sum of list (ex. [1000, 900, 90] -> 1990 )


# to_roman (ex. 1998)

# 1. divide number into characters (ex. '1998' -> [1, 9 , 9, 8])

# 2. transform each number into the roman equivalent roman using a list_of_dict
#                                       (ex. [1, 9 , 9, 8] -> ['M', 'CM', 'XC', 'VIII'])
#    the list_of_dict has in every position the minimum, maximum and medium values (ex. X V I for the first decimal)

# 3. return the joined list ('MCMXCVIII')
# --------------------------------------------------------------------------------------------------------------------
#   MAIN CLASS
# --------------------------------------------------------------------------------------------------------------------
class Roman:

    # constants
    ROMAN2DEC = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    a = {10: 'X', 5: 'V', 1: 'I'}
    b = {10: 'C', 5: 'L', 1: 'X'}
    c = {10: 'M', 5: 'D', 1: 'C'}
    d = {10: '?', 5: '?', 1: 'M'}  # ? = 'i don't know, the problem only gets to M'

    DEC2ROMAN = [a, b, c, d]

    def to_roman(self, _decimal):

        # divide into characters (ex. '1998' -> [1, 9 , 9, 8])
        numbers = [int(value) for value in str(_decimal)]

        # transform number into roman
        roman, romans = '', []
        for i, number in enumerate(reversed(numbers)):

            # get proper dict (ex. for numbers from 1 to 9 get {10: 'X', 5: 'V', 1: 'I'})
            chosen_dict = self.DEC2ROMAN[i]
            one, five, ten = chosen_dict[1], chosen_dict[5], chosen_dict[10]

            # 0 -> do nothing
            if not number:
                continue

            # 1, 2 or 3 -> print one 1, 2 or 3 times (ex. 3 is III)
            elif number in (1, 2, 3):
                roman = one * number

            # 4 -> print one and five (ex. 4 is IV)
            elif number == 4:
                roman = one + five

            # 5 -> print five (ex. 50 is L)
            elif number == 5:
                roman = five

            # 6 -> print five and one (ex. 60 is LX)
            elif number == 6:
                roman = five + one

            # 7 -> print five one one (ex. 70 is LXX)
            elif number == 7:
                roman = five + one * 2

            # 8 -> print five one one one (ex. 800 is DCCC)
            elif number == 8:
                roman = five + one * 3

            # 9 -> print one and ten (ex. 9 is IX)
            elif number == 9:
                roman = one + ten

            romans.append(roman)

        # return all symbols together
        return ''.join(list(reversed(romans)))

    def from_roman(self, _roman):

        # set-up
        symbols = []
        previous_sym = _roman[0]

        # single character  -> just use dictionary and return
        if len(_roman) == 1:
            return self.ROMAN2DEC[_roman]

        # divide characters into symbols (ex. 'MCMXC' -> ['M', 'CM', 'XC'])
        for ch, value in enumerate(_roman[1:]):

            # if current_value is lower (or equal) than previous_sym -> start new symbol
            if self.ROMAN2DEC[value] <= self.ROMAN2DEC[previous_sym[0]]:
                symbols.append(previous_sym)
                previous_sym = value

            # current_value higher than previous -> add to previous symbol
            else:
                previous_sym += value

        # save last symbol
        else:
            symbols.append(previous_sym)

        # translate symbols into dec (ex. ['M', 'CM', 'XC'] -> [1000, 900, 90])
        decimals = []
        for sym in symbols:

            decimal = self.ROMAN2DEC[sym[-1]]

            for ch in reversed(sym[:-1]):
                decimal -= self.ROMAN2DEC[ch]

            decimals.append(decimal)

        # return sum of all symbols (ex. [1000, 900, 90] -> 1990 )
        return sum(decimals)


# --------------------------------------------------------------------------------------------------------------------
#   TEST SAMPLES
# --------------------------------------------------------------------------------------------------------------------
RomanNumerals = Roman()
result = RomanNumerals.to_roman(1000)  # 'M'
print(result)

result = RomanNumerals.to_roman(4)  # 'IV'
print(result)

result = RomanNumerals.to_roman(1)  # 'I'
print(result)

result = RomanNumerals.to_roman(1990)  # 'MCMXC'
print(result)

result = RomanNumerals.to_roman(2008)  # 'MMVIII'
print(result)

result = RomanNumerals.from_roman('XXI')  # 21
print(result)

result = RomanNumerals.from_roman('I')  # 1
print(result)

result = RomanNumerals.from_roman('IV')  # 4
print(result)

result = RomanNumerals.from_roman('MMVIII')  # 2008
print(result)

result = RomanNumerals.from_roman('MDCLXVI')  # 1666
print(result)
