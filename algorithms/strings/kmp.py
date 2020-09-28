def kmp(str, pattern):
    lps_arr = lps(pattern)

    index = -1
    matches = 0
    for i in range(len(str)):
        while str[i] != pattern[index + 1] and index > -1:
            index = lps_arr[index] - 1

        if str[i] == pattern[index + 1]:
            index +=1

        if index == len(pattern) - 1:
            matches += 1
            index = -1

    return matches


def test_kmp_1():
    assert kmp('ababcabcabababd', 'ababd') == 1

def test_kmp_2():
    assert kmp('ababcabcabababd', 'abab') == 2

def lps(str):
    lps = [0] * len(str)
    index = 0
    for i in range(1, len(str)):
        if str[i] == str[index]:
            index += 1
            lps[i] = index
        else:
            index = 0
    return lps

def test_lps_1():
    assert lps('abcdabeabf') == [0, 0, 0, 0, 1, 2, 0, 1, 2, 0]

def test_lps_2():
    assert lps('abcdeabfabc') == [0, 0, 0, 0, 0, 1, 2, 0, 1, 2, 3]

def test_lps_3():
    assert lps('aabcadaabe') == [0, 1, 0, 0, 1, 0, 1, 2, 3, 0]
        
def test_lps_4():
    assert lps('aaaabaacd') == [0, 1, 2, 3, 0, 1, 2, 0, 0]