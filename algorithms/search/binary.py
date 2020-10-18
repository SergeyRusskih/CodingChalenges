def binary(arr, value):  
    index = len(arr) // 2
    if arr[index] == value:
        return True
    elif index == 0:
        return False

    if arr[index] > value:
        return binary(arr[:index], value)

    return binary(arr[index:], value)

def test_binary():
    assert binary([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2) == True

def test_binary1():
    assert binary([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -1) == False

def test_binary2():
    assert binary([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == False