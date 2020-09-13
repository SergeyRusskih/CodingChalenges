def palindrome_premutation(string):
    if len(string) == 0:
        return False

    string = string.replace(" ", "").lower()
    if len(string) == 0:
        return True

    dict = {}
    for current in string:
        if current in dict:
            dict[current] += + 1
        else:
            dict[current] = 1
    
    odd_found = False
    for val in dict.values():
        if val % 2 != 0:
            if not odd_found and len(string) % 2 == 1:
                odd_found = True
                continue
            return False

    return True

def test_example_is_premutation():
    assert palindrome_premutation("Tact Coa")

def test_even_is_premutation():
    assert palindrome_premutation("Tact  Ca")