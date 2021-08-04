# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3009/
def atoi(s):
    if not s:
        return 0
        
    end = 0
    s = s.strip()
    for i, leter in enumerate(s):
        if not leter.isdigit() and not (i == 0 and (leter == '-' or leter == '+')):
            break
        end = i+1

    if not end or (len(s[:end]) == 1 and not s[:end].isdigit()):
        return 0

    result = int(s[:end])
    if result > 2**31-1: return 2**31-1
    elif result < -2**31: return -2**31
    return result

def test_7():
    result = atoi("3.14159")
    assert result == 3

def test_6():
    result = atoi("+-12")
    assert result == 0

def test_1():
    result = atoi("42")
    assert result == 42

def test_2():
    result = atoi("  -42")
    assert result == -42

def test_3():
    result = atoi("4193 with words")
    assert result == 4193

def test_4():
    result = atoi("words and 987")
    assert result == 0

def test_5():
    result = atoi("-91283472332")
    assert result == -2147483648