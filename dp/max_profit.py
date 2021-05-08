def max_profit(prices):
    min_price, result = 10**9, 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        result = max(result, profit)

    return result

def test_1():
    result = max_profit([7,1,5,3,6,4])
    assert result == 5

def test_2():
    result = max_profit([1,2])
    assert result == 1

def test_3():
    result = max_profit([1,2,4])
    assert result == 3