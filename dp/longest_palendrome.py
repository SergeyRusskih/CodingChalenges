def longest_palindrome(s):
    def is_palindrome(value):
        i = 0
        j = len(value) - 1
            
        while i < j:
            if value[i] != value[j]:
                return False
                
            i += 1
            j -= 1
                
        return True
        
    result = s[0]
    for i in range(len(s)):
        memo = set()
        for j in range(i, len(s)):
            if s[j] in memo:
                memo.remove(s[j])
            else:
                memo.add(s[j])
                    
            substr = s[i:j+1]
            if len(memo) < 2 and len(result) < len(substr):
                if is_palindrome(substr):
                    result = substr    
                
    return result


def test_longest_palindrome():
    result = longest_palindrome("cbbd")
    assert result == "bb"