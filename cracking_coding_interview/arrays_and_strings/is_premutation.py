def is_premutation(one, another):
    if len(one) != len(another):
        return False

    for i in range(len(one)):
        if one[i] != another[len(one) - (1 + i)]:
            return False

    return True

def test_different_lengths():
    assert is_premutation("abcde", "abcd") == False

def test_simple_positive():
    assert is_premutation("abcde", "edcba")