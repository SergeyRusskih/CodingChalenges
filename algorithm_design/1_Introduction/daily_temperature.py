# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have
# to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
# 
# https://leetcode.com/problems/daily-temperatures/
def daily_temperature(temperatures):

    answer = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            item = stack.pop()
            answer[item] = i - item

        stack.append(i)

    return answer

def test_1():
    result = daily_temperature([73,74,75,71,69,72,76,73])
    assert result == [1,1,4,2,1,1,0,0]

def test_2():
    result = daily_temperature([30,40,50,60])
    assert result == [1,1,1,0]

def test_3():
    result = daily_temperature([30,60,90])
    assert result == [1,1,0]
