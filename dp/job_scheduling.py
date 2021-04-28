def job_scheduling(start_time, end_time, profit):

    max_index = max(end_time)
    dp = [0] + ([0] * max_index)

    end_time_dict = {}
    for i, end in enumerate(end_time):
        if end in end_time_dict:
            lst = end_time_dict[end] 
            lst.append(i)
        else:
            end_time_dict[end] = [i]

    for i in range(1, max_index+1):
        dp[i] = max(dp[i-1], dp[i])
        if i in end_time_dict:
            for index in end_time_dict[i]:
                dp[i] = max(dp[i], profit[index]+dp[start_time[index]])

    return dp[-1]

def test_4():
    result = job_scheduling([4,2,4,8,2], [5,5,5,10,8], [1,2,8,10,4])
    assert result == 18

def test_1():
    result = job_scheduling([1,2,3,3], [3,4,5,6], [50,10,40,70])
    assert result == 120

def test_2():
    result = job_scheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60])
    assert result == 150

def test_3():
    result = job_scheduling([1,1,1], [2,3,4], [5,6,4])
    assert result == 6