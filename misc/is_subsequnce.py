def is_subsequence(s: str, t: str) -> bool:
    if len(s) == 0 and len(t) != 0:
        return True
        
    if len(s) == 0 and len(t) == 0:
        return True
        
    if len(s) > len(t):
        return False
        
    idx = 0
    for item in t:
        if item == s[idx]:
            idx += 1
                
    return idx == len(s)

def test_1():
    result = is_subsequence("axc", "ahbgdc")
    assert not result


def test_2():
    result = is_subsequence("abc", "")
    assert not result