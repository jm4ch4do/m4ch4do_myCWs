# ----- Problem: Strip Comments (4kyu)
# ----- URL: https://www.codewars.com/kata/strip-comments


def strip_comments(_text, _comment_types):
    """
    (string, list) -> (string)
    :param _text: string with a long text having /n and line comments
    :param _comment_types: list_of_characters where each character represents a type of comments
    :return: string with the same text but without comments

    :example:
        _text = "apples, pears # and bananas\ngrapes\nbananas  !apples"
        _comment_types = ["#","!"]
        returns "apples, pears\ngrapes\nbananas"
    """

    # set-up
    lines = _text.split('\n')
    cleaned_text = ''

    # clean line by line
    for i, line in enumerate(lines):
        cleaned_line = clean_line(line, _comment_types)
        cleaned_text += cleaned_line if (not i) else '\n' + cleaned_line

    return cleaned_text


def clean_line(_line, _comment_types):
    for i, ch in enumerate(_line):
        if ch in _comment_types:
            return _line[:i].strip()

    # no comments -> return _line with no changes
    return _line


# ---- MAIN CODE -------------------------------------------------------------------------------

my_text = "apples, pears # and bananas\ngrapes\nbananas  !apples"
my_comment_types = ['#', '!']
expected = "apples, pears\ngrapes\nbananas"
my_cleaned_text = strip_comments(my_text, my_comment_types)
print(my_cleaned_text == expected)
