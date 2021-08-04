def radix_sort(arr, d):
    for i in range(d):
        count_arr = [0] * 10
        for item in arr:
            index = get_index(i, item)
            count_arr[index] += 1
        for j in range(1, len(count_arr)):
            count_arr[j] += count_arr[j-1]
        result = [0] * len(arr)
        for item in reversed(arr):
            index = get_index(i, item)
            result[count_arr[index]-1] = item
            count_arr[index] -= 1
        arr = result
    return arr


def get_index(i, item): 
    return (item % (10 ** (i + 1))) // 10 ** i

def test_1():
    arr = [329, 457, 657, 832, 436, 720, 355]
    assert radix_sort(arr, 3) == [
        329,
        355,
        436,
        457,
        657,
        720,
        832
    ]