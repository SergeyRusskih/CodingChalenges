def is_unique(string):
    sorted(string)
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True

def test_simple_unique():
    assert is_unique("abc")

def test_simple_not_unique():
    assert is_unique("abb") == False