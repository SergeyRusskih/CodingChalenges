# O(log n), maintains the max-heap property
# assumes that the binary trees rooted at LEFT(i) and RIGHT(i) are maxheaps, 
# but that A[i] might be smaller than its children, thus violating the max-heap
# property. HEAPIFY lets the value at A[i] 'float down' in the max-heap so
# that the subtree rooted at index i obeys the max-heap property.
def heapify(i, arr):
    left_index = left(i)
    right_index = right(i)

    largest = i
    if left_index <= len(arr) and arr[left_index-1] > arr[largest-1]:
        largest = left_index

    if right_index <= len(arr) and arr[right_index-1] > arr[largest-1]:
        largest = right_index

    if largest != i:
        swap(i-1, largest-1, arr)
        heapify(largest, arr)

def swap(x, y, arr):
    tmp = arr[y]
    arr[y] = arr[x]
    arr[x] = tmp

# O(n), produces a maxheap from an unordered input array
def build_heap(arr):
    for i in range(len(arr) // 2, 0, -1):
        heapify(i, arr)

# O(n lg n), sorts an array in place
def heapsort(arr):
    build_heap(arr)
    res = []
    while len(arr) > 0:
        res.insert(0, arr.pop(0))
        heapify(1, arr)
    return res

# O(lg n), allow the heap data structure to implement a priority queue
# insert new item into priority queue
def insert(arr, key):
    arr.isert(0, key)
    heapify(1, arr)

# returns the max value and removes it from the heap
def extract_max(arr):
    max = arr.pop(0)
    heapify(1, arr)
    return max

# increases the priority of the element
def increase_key(arr, i, key):
    arr[i-1] = key
    while i > 1 and arr[i-1] > arr[parent(i, arr)-1]:
        swap(i-1, parent(i)-1, arr)
        i = parent(i, arr)

# HEAP-MAXIMUM
def heap_maximum():
    pass

def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return (2 * i) + 1



def test_heapify():
    arr = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    heapify(2, arr)
    assert arr == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

def test_build_heap():
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    build_heap(arr)
    assert arr == [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

def test_heapsort():
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    res = heapsort(arr)
    assert res == [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]

def test_increase_key():
    arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    increase_key(arr, 9, 15)
    assert arr == [16, 15, 10, 14, 7, 9, 3, 2, 8, 1]