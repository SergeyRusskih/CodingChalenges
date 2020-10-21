def merge_sort(numbers):
    if len(numbers) < 2:
        return numbers
    return divide(numbers, 0, len(numbers))

def divide(numbers, i, j):
    middle = (j - i) // 2
    if j - i > 2:
        divide(numbers, i, i+middle)
        divide(numbers, i+middle, j)
    return sort(numbers, i, j, i+middle)

def sort(numbers, start, end, middle):
    left = numbers[start:middle]
    right = numbers[middle:end]

    left_index, right_index = 0, 0
    for i in range(start, end):
        if right_index == len(right):
            numbers[i] = left[left_index]
            left_index += 1
        elif left_index == len(left):
            numbers[i] = right[right_index]
            right_index += 1
        elif left[left_index] > right[right_index]:
            numbers[i] = right[right_index]
            right_index += 1
        else:
            numbers[i] = left[left_index]
            left_index += 1

    return numbers

def test_simple_example():
    assert merge_sort([3,1]) == [1,3]

def test_example():
    assert merge_sort([3,1,5,7,2,9]) == [1,2,3,5,7,9]


    