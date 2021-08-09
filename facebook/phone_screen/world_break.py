# https://leetcode.com/problems/word-break/
def solution(s, word_dict):
    words = {}
    for word in word_dict:
        key = word[0]
        if key in words:
            words[key].append(word)
        else:
            words[key] = [word]

    def find(index, memo):
        if index == len(s):
            return True

        if s[index:] in memo:
            return memo[s[index:]]

        if s[index] not in words:
            memo[s[index:]] = False
            return False

        result = False
        for word in words[s[index]]:
            if s[index:].startswith(word):
                result |= find(index + len(word), memo)

        memo[s[index:]] = result
        return result

    return find(0, {})


def test_1():
    assert solution("leetcode", ["leet","code"])

def test_2():
    assert solution("applepenapple", ["apple","pen"])

def test_3():
    assert not solution("catsandog", ["cats","dog","sand","and","cat"])