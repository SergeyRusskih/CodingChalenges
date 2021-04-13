def is_palindrome(s):

    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True

def test_is_palindrome():
    result = is_palindrome("A man, a plan, a canal: Panama")
    assert result

def test_is_palindrome():
    result = is_palindrome("race a car")
    assert not result