# every group will be evaluated from the start of the string
a = "\A"    

# group 1: string has more than 6 characters and less than 10(alphanumeric)
b = "(?=\w{6, 10})"  # () group, ?= lookahead assertion meaning that previous match works only if this match works(is True)  
                     # \w any word or character, {6, 10} lenght from 6 to 10

# group 2: string has at least one lowercase
c = "(?=[^a-z]*[a-z])"  # () group, ?= same
                        # [^a-z]*[a-z] accept zero o more repetitions of something that is not a lowercase
                        #              until you find a lowercase

# group 3: string has at least one uppercase
d = "(?=[^A-Z]*[A-Z])"  # () group, ?= same
                        # [^A-Z]*[A-Z] same as before for uppercase

# group 4: string has at least one string
e = "(?=\D*\d)"  # () group, ?= same
                 # \D*\d accept zero o more repetitions of something that is not a digit
                 # until you find a digit

# group 5: string has only alphanumeric characters
f = "(?!\w*[\W|_]+)"  # () group, ?! negative lookahead assertion meaning that previous match works only if this match is False  
                      # \w* accept any zero or more repetitions of words(alphanumeric characters)
                      # [\W|_] until you find one or more of not-words or one or more of '_'(the _ is considered a word)

# put together all the groups
regex = a + b + c + d + e + f
