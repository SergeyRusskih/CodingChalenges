# Counting sort assumes that each of the n input elements is an integer in the range
# 0 to k, for some integer k. When k = O(n), the sort runs in O(n) time
def counting_sort(arr, max):
    count_arr = [0] * (max+1)
    for item in arr:
        count_arr[item] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    result_arr = [0] * len(arr)
    for item in arr:
        result_arr[count_arr[item]-1] = item
        count_arr[item] -= 1

    return result_arr

def test_1():
    assert counting_sort([4, 4, 6, 8, 9, 1, 3], 9) == [1, 3, 4, 4, 6, 8, 9]