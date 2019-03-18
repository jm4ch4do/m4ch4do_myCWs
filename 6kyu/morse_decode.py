# ----- Problem: Decode the Morse Code (6ku)
# ----- URL: https://www.codewars.com/kata/54b724efac3d5402db00065e


def decode_morse(morse_string):
    """
    (string) -> (string)
    :param morse_string: string containing morse code which is a series of '.'s and '-'s
    :return human_string: string with the translation of the morse code to human words

    :description:
    A character in morse code is always in capital letter and is represented by a sequence of '.'s and '-'
    A space signals the start of a new letter of the same word
    Three spaces signals the start of a new word
    Spaces a the start or end mean nothing and should be ignored

    :algorithm:
    1. Remove spaces at the start and end
    2. Divide in words using three spaces as separator
    3. Divide each word in characters and use dictionay to translate every character
    4. Return human word

    :pre-loaded variables:
    MORSE_CODE: A dictionary with keys like '.--' and values like 'A'

    :example:
    >> sample_morse = ('  .... . -.--   .--- ..- -.. .   ')
    'HEY JUDE'

    """
    # 1. Remove spaces at the start and at the end
    start, end = 0, len(morse_string)
    # remove spaces at the start
    for ch in morse_string:
        if ch == ' ':
            start +=1
        else:
            break

    # remove spaces at the end
    for i in range(len(morse_string)):
        reverse_i = len(morse_string)-1-i
        if morse_string[reverse_i] == ' ':
            end -= 1
        else:
            break

    morse_string = morse_string[start:end]

    # 2. Divide in words using three spaces as separator
    morse_words = morse_string.split('   ')

    # 3. Divide each word in characters and use dictionary to translate every character
    human_string = ''
    for word in morse_words:
        letters = word.split(' ')
        for letter in letters:
            human_string += MORSE_CODE[letter]
        human_string += ' '  # add space between letters

    human_string = human_string[:-1]  # erase space after the last word

    # 4. Return human word
    return human_string


MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}

sample_morse = ('  .... . -.--   .--- ..- -.. .   ')
expected = 'HEY JUDE'
result = decode_morse(sample_morse)
print(result)
