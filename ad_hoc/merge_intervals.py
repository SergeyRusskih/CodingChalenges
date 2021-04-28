def merge_intervals(intervals):
    sorted_intervals = sorted(intervals, key=lambda item: item[0])

    result = [sorted_intervals[0]]
    for i in range(1, len(sorted_intervals)):
        prev = result.pop()
        current = sorted_intervals[i]

        if prev[1] < current[0]:
            result.append(prev)
            result.append(current)
        else:
            result.append([prev[0], max(prev[1], current[1]) ])

    return result

def test_1():
    result = merge_intervals([[1,3],[2,6],[8,10],[15,18]])
    assert result == [[1,6],[8,10],[15,18]]

def test_2():
    result = merge_intervals([[1,4],[4,5]])
    assert result == [[1,5]]
