def one_away(one, another):
    if abs(len(one) - len(another)) > 1:
        return False

    largest = one
    smalest = another
    if len(another) > len(one):
        largest = another
        smalest = one

    largest_dict = dict_from_string(largest)
    smalest_dict = dict_from_string(smalest)

    diff_count = 0
    for key, value in largest_dict.items():
        if key in smalest_dict:
            diff = abs(smalest_dict[key] - value)
            if diff == 0:
                continue
            if diff == 1:
                diff_count += 1
                continue
            return False
        else:
            diff_count += 1

        if diff_count > 1:
            return False

    return True

def dict_from_string(string):
    dict = {}
    for i in range(len(string)):
        if string[i] in dict:
            dict[string[i]] += 1
        else:
            dict[string[i]] = 1
    return dict

def test_first_example():
    assert one_away("pale", "ple")

def test_second_example():
    assert one_away("pales", "pale")

def test_third_example():
    assert one_away("pale", "bale")

def test_forth_example():
    assert one_away("pale", "bake") == False