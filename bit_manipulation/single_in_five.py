def single_in_five(numbers):
    one, two, three = 0, 0, 0
    for number in numbers:
        three ^= two & one & number
        two ^= one & number
        one ^= number

        mask = ~(one & ~two & three)
        one &= mask
        two &= mask
        three &= mask

    return one

def test_single_in_five():
    assert single_in_five([2,3,2,2,2,2,1,1,1,1,1]) == 3