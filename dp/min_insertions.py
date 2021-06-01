def min_insertions(s):
    if len(s) < 2: return 0
    if len(s) == 2: return 1

    length = len(s)

    dp = [ [0] * (length+1) for i in range(length+1 ) ]

    for i in range(length):
        for j in range(length):
            dp[i+1][j+1] = dp[i][j]+1 if s[i] == s[~j] else max(dp[i+1][j], dp[i][j+1])

    return length - dp[length][length]

def test_5():
    result = min_insertions("no")
    assert result == 1
     
def test_2():
    result = min_insertions("mbadm")
    assert result == 2

def test_6():
    result = min_insertions("zjveiiwvc") # czjvweiiewvjzc
    assert result == 5

def test_1():
    result = min_insertions("zzazz")
    assert result == 0

def test_3():
    result = min_insertions("leetcode")
    assert result == 5

def test_4():
    result = min_insertions("g")
    assert result == 0