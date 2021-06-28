def combination_sum(candidates, target):
    result = []
    def backtrack(index, arr, remainder):
        if remainder == 0:
            result.append(arr.copy())
        elif remainder > 0:
            for i in range(index, len(candidates)):
                arr.append(candidates[i])
                backtrack(i, arr, remainder-candidates[i])
                arr.pop()
        
    backtrack(0, [], target)
    return result

def test_1():
    result = combination_sum([2,3,6,7], 7)
    assert result == [[2,2,3],[7]]

def test_2():
    result = combination_sum([2,3,5], 8)
    assert result == [[2,2,2,2],[2,3,3],[3,5]]

def test_3():
    result = combination_sum([2], 1)
    assert result == []

def test_4():
    result = combination_sum([1], 1)
    assert result == [[1]]

def test_5():
    result = combination_sum([1], 2)
    assert result == [[1,1]]