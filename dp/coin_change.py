# https://leetcode.com/problems/coin-change-2/
def coin_change(coins, amount):

    minCoins = [0] + [10**9] * amount

    for i in range(1, amount+1):
        for coin in coins:
            if i - coin >= 0:
                minCoins[i] = min(minCoins[i], minCoins[i-coin] + 1)

    if minCoins[-1] == 10**9:
        return -1

    return minCoins[-1]

def test_coin_change():
    coins = [1,2,5]
    amount = 11
    result = coin_change(coins, amount)
    assert result == 3

def test_coin_change_1():
    coins = [2]
    amount = 3
    result = coin_change(coins, amount)
    assert result == -1