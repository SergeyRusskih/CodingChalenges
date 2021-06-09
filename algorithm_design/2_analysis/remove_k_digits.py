def remove_k_digits(num, k):
    if len(num) == k:
        return "0"

    nums = list(num)
    j = 0
    while nums and k > 0:
        if len(nums) == 1 or j+1 >= len(nums):
            nums.pop()
        elif nums[j] > nums[j+1]:
            nums.pop(j)
            if j > 0:
                j -= 1
        else:
            j += 1
            continue

        while nums and nums[0] == '0':
            nums.pop(0)

        k -= 1

    if not nums:
        return "0"

    return "".join(nums)

def test_8():
    assert remove_k_digits("52660469", 2) == "260469"

def test_7():
    assert remove_k_digits("1234567890", 9) == "0"

def test_6():
    assert remove_k_digits("12345", 2) == "123"

def test_5():
    assert remove_k_digits("1111111", 3) == "1111"

def test_4():
    assert remove_k_digits("112", 1) == "11"

def test_1():
    assert remove_k_digits("1432219", 3) == "1219"

def test_2():
    assert remove_k_digits("10200", 1) == "200"

def test_3():
    assert remove_k_digits("10", 2) == "0"