def find_common_character(A):
    letter_set = dict()
    for i in A[0]:
        if i in letter_set:
            letter_set[i] += 1
        else:
            letter_set[i] = 1

    for i in A[1:]:
        temp_set = dict()
        for j in i:
            if j in temp_set:
                temp_set[j] += 1
            else:
                temp_set[j] = 1

        for _, v in enumerate(letter_set):
            if letter_set[v] is 0:
                continue

            if v not in temp_set:
                letter_set[v] = 0
            elif letter_set[v] > temp_set[v]:
                letter_set[v] = temp_set[v]

    result = []
    for _, v in enumerate(letter_set):
        for i in range(letter_set[v]):
            result.append(v)

    return result


def test_example_1():
    result = find_common_character(["bella","label","roller"])
    assert result == ["e","l","l"]

def test_example_2():
    result = find_common_character(["cool","lock","cook"])
    assert result == ["c","o"]  