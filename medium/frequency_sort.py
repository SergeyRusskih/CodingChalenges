def frequency_sort(s):
    char_dict = dict()
    for i in s:
        if i in char_dict:
            char_dict[i] += 1
        else:
            char_dict[i] = 1

    char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return "".join( x * char_dict[x] for x in char_dict)

def test_example():
    result = frequency_sort("tree")
    assert result == "eetr"

def test_example_1():
    result = frequency_sort("Aabb")
    assert result == "bbAa"

def test_example_2():
    result = frequency_sort("cccaaa")
    assert result == "cccaaa" 