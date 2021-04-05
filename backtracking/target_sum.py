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

def test_target_sum():
    arr = [ 2, 3, 5, 6, 8 ]
    result = target_sum(arr, 7)
    assert result == 2