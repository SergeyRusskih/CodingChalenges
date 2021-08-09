# https://leetcode.com/problems/decode-ways
def solution(s):
    def find(encoded, memo):
        if not encoded: return 1
        if encoded[0] == "0": return 0
            
        candidate1 = find(encoded[1:], memo)

        candidate2 = 0
        if len(encoded) > 1 and encoded[:3] < "27":
            candidate2 = find(encoded[2:], memo)
            
        result = candidate1 + candidate2
        memo[encoded] = result

        return result
        
    return find(s, {})

def test_1():
    assert solution("27") == 1

def test_2():
    assert solution("12") == 2

def test_3():
    assert solution("226") == 3
