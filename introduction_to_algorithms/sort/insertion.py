def insertion(numbers):
    for i in range(1, len(numbers)):
        index = i
        while numbers[index - 1] > numbers[index] and index > 0:
            tmp = numbers[index]
            numbers[index] = numbers[index - 1]
            numbers[index - 1] = tmp
            index -= 1 

    return numbers

def test_example():
    assert insertion([9,5,1,2,6]) == [1,2,5,6,9]