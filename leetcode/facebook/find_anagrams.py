def find_anagrams(s, p):
    letters_count = dict()

    def add(dict, value):
        if value in dict:
            dict[value] += 1
        else:
            dict[value] = 1

    def remove(dict, value):
        if dict[value] > 1:
            dict[value] -= 1
        else:
            del dict[value]

    for letter in p:
        add(letters_count, letter)

    window = dict()
    result = []
    i = j = 0
    while j < len(s):
        add(window, s[j])
        j += 1
        
        if j - i == len(p):
            if window.__eq__(letters_count):
                result.append(i)

            remove(window, s[i])
            i += 1
                          
    return result


def test_example_1():
    result = find_anagrams("cbaebabacd", "abc")
    assert result == [0, 6]

def test_example_2():
    result = find_anagrams("abab", "ab")
    assert result == [0, 1, 2]

def test_example_3():
    result = find_anagrams("af", "be")
    assert result == []