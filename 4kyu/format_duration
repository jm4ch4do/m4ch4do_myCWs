def format_duration(n):
    """
    (number) -> (string)

    :param n: number representing an amount of seconds
    :return : string with param n divided in years, days, hours, minutes and seconds

    :algorithm:
    (input) = 172860
    1. Find seconds equivalency: the amount of seconds in a year, day, hour, minutes and seconds
        (SE = [365*24*60*60, 24*60*60, 60*60, 60, 1])
    2. Transform to human format:
        (human = [0, 2, 0, 1, 0])
        If n > seconds_in_year compute n // seconds_in_year to get years and use % to get remaining seconds
            Repeat for days, hours, minutes until there are less than 60 seconds
    3. Create output string:
        (human_string_list = ['2 days', '1 minute'])
        (human_string_ready = '2 days and 1 minute')
        Create output string which says 'year' for 1 year and years for more than 1 year
            Repeat for days, hours, minutes, seconds
            Remove empty years, days, hours, minutes or seconds from output
            Add ',' or 'and' for concat of output
    (output) = '2 years, 2 days, 2 hours, 2 minutes and 2 seconds'

    :var: [human]               -> list with amount of years, days, hours, minutes, seconds
          [human_string_list]   -> list similar to 'human' but add tails like 'year' or 'seconds'
          [human_string_ready]  -> string concat of 'human_string_list' adding ',' or 'and' between elements

    :examples:
    (63252122) -> (2 years, 2 days, 2 hours, 2 minutes and 2 seconds)
    (31626061) -> (1 year, 1 day, 1 hour, 1 minutes and 1 second)
    (172860)   -> (2 days and 1 minute)
    (7200)     -> (2 hours)
    """

    # 0. Dummy input
    if n == 0:
        return "now"

    # 1. Find seconds equivalency
    S = 1  # 1 second
    M = 60 * S  # 1 minutes = 60 seconds
    H = 60 * M  # 1 hour = 60 minutes
    D = 24 * H  # 1 day = 24 hours
    Y = 365 * D  # 1 year = 365 days

    SE = [Y, D, H, M]  # seconds equivalency

    # 2. Transform to human format
    human = [0, 0, 0, 0, 0]  # human format
    while n >= 60:  # keep going until there are less than 60 seconds
        for i, value in enumerate(SE):
            if n >= value:
                human[i] = n // value
                n %= value
                break

    human[-1] = n

    # 3. Create output string
    tails = ['year', 'day', 'hour', 'minute', 'second']
    human_string_list = []
    for i in range(len(human)):
        if human[i] != 0:  # output cannot say '0 years' or '0 days'
            plural = '' if human[i] == 1 else 's'  # '1 year' or '2 years' with 's' at the end
            human_string_list.append(' '.join([str(human[i]), tails[i]+plural]))

    # make final string using concat with ',' or 'and'
    human_string_ready = ''
    for i in range(len(human_string_list)):
        if i == 0:
            human_string_ready = human_string_list[0]
        elif i == len(human_string_list)-1:
            human_string_ready = ' and '.join([human_string_ready, human_string_list[i]])
        else:
            human_string_ready = ', '.join([human_string_ready, human_string_list[i]])

    return human_string_ready
