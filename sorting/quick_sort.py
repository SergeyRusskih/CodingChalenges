# any comparison based sort algorithm requires at least O(n log n) in worst case
def quick_sort(arr, i, j):
    if i < j:
        p = partition(arr, i, j)
        quick_sort(arr, i, p-1)
        quick_sort(arr, p+1, j)

def partition(arr, i, j):
    pivotal = arr[j]
    index = i
    for x in range(i, j):
        if arr[x] <= pivotal:
            swap(arr, index, x)
            index += 1
            
    swap(arr, index, j)
    return index

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def test_quick_sort():
    arr = [2, 8, 7, 1, 3, 5, 6, 4]
    quick_sort(arr, 0, len(arr)-1)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8]
