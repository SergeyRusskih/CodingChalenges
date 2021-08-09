# https://leetcode.com/problems/longest-common-subsequence/
def solution(text1, text2):
    if not text1 or not text2:
        return 0
        
    dp = [[ 0 for i in range(len(text1)+1) ] for j in range(len(text2)+1) ]

    for i in range(1, len(text1)+1):
        for j in range(1, len(text2)+1):
            if text1[i-1] == text2[j-1]:
                dp[j][i] = dp[j-1][i-1] + 1
            else:
                dp[j][i] = max(dp[j-1][i], dp[j][i-1])
            
    return dp[-1][-1]


def test_1():
    assert solution("ezupkr", "ubmrapg") == 2

def test_2():
    assert solution("abcde", "ace") == 3