# ----- Problem: Extract the domain name from a URL (5ku)
# ----- URL: https://www.codewars.com/kata/514a024011ea4fb54200004b


def get_domain(_url):
    """
    (string) -> (string)
    :param _url: string with a long url
    :return: string with only the domain name from _url

    :examples:
    ("http://github.com/carbonfive/raygun") -> "github"
    ("http://www.zombie-bites.com") -> "zombie-bites"
    ("https://www.cnet.com") -> "cnet"
    ("www.xakep.ru") -> "xakep"
    """
    # get pieces separated by '/'
    pieces = _url.split('/')

    # remove 'http'/'https' part if present
    if pieces[0][0:4] == 'http':
        pieces.pop(0)
        pieces.pop(0)

    # remove 'www' part if present
    name = pieces[0] if not pieces[0][:4] == "www." else pieces[0][4:]

    # get all characters before the '.'
    name = name[:name.index('.')]
    return name


my_url = "www.xakep.ru"
result = get_domain(my_url)
expected = "github"
print(result)
