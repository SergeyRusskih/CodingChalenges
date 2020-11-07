'Single' and "Double" #quetes doesn't matter
r"Raw string. \don't / notice special characters."

# multy line string - add '\' to exclude new line symbol
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
'unununium'

# literals automatically concatinated
'Py' 'thon'


#Strings can be indexed
word = 'Python'
word[5]  # character in position 5 - 'n'
word[-2] # second-last character - 'o'
word[2:5] # characters from position 2 (included) to 5 (excluded) -'tho'
word[:2]  # character from the beginning to position 2 (excluded) - 'Py'
word[4:]  # characters from position 4 (included) to the end - 'on'
word[-2:] # characters from the second-last (included) to the end - 'on'


# Lists also support operations like concatenation:
squares = [1, 4, 9, 16, 25]
squares + [36, 49, 64, 81, 100] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]