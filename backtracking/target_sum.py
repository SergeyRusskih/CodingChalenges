def target_sum(arr, k):

    results = []
    def dfs(current, start, intermediate):
        if current == k:
            results.append(list(intermediate))

        for i in range(start, len(arr)):
            if current + arr[i] <= k:
                intermediate.append(arr[i])
                dfs(current + arr[i], i, intermediate)
                intermediate.pop()

    dfs(0, 0, [])
    return len(results)


def target_sum_dp(arr, k):

    count = 0
    diffs = set([k])

    while diffs:
        current = diffs.pop()

        index = 0
        while index < len(arr):
            diff = current - arr[index]
            if diff == 0:
                count += 1
                arr.pop(index)
            elif diff > 0 and diff not in diffs:
                diffs.add(diff)

            index += 1
        
    return count

def test_target_sum():
    arr = [ 2, 3, 5, 6, 8 ]
    result = target_sum(arr, 7)
    assert result == 2

def test_target_sum_dp():
    arr = [ 2, 3, 5, 6, 8 ]
    result = target_sum_dp(arr, 7)
    assert result == 2