# https://leetcode.com/problems/roman-to-integer/solution/
def roman_to_int(s):
    exceptions = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = index = 0
    while index < len(s):
        if index+1 < len(s) and s[index:index+2] in exceptions:
            result += exceptions[s[index:index+2]] 
            index += 2
        else:
            result += mapping[s[index]]
            index += 1

    return result

def test_1():
    result = roman_to_int("III")
    assert result == 3

def test_2():
    result = roman_to_int("IV")
    assert result == 4

def test_3():
    result = roman_to_int("IX")
    assert result == 9

def test_4():
    result = roman_to_int("LVIII")
    assert result == 58

def test_5():
    result = roman_to_int("MCMXCIV")
    assert result == 1994