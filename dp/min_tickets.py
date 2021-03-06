import this

def min_tickets(days, costs):

    days_set = set(days)
    dp = [0] * (days[-1]+1)
    for i in range(days[-1]+1):
        if i not in days_set:
            dp[i] = dp[i-1]
        else:         
            dp[i] = min(
                dp[max(0, i-1)] + costs[0],
                dp[max(0, i-7)] + costs[1],
                dp[max(0, i-30)] + costs[2]
            )

    return dp[-1]

def test_min_tickets_even_more():
    result = min_tickets([1,4,6,7,8,20], [7, 2, 15])
    assert result == 6

def test_min_tickets_one():
    result = min_tickets([1], [2,7,15])
    assert result == 2

def test_min_tickets_two():
    result = min_tickets([1,4], [2,7,15])
    assert result == 4

def test_min_tickets():
    result = min_tickets([1,4,6,7,8,20], [2,7,15])
    assert result == 11

def test_min_tickets_more():
    result = min_tickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15])
    assert result == 17