def max_product(words):
        
    max_sum = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if not (set(words[i]) & set(words[j])):
                max_sum = max(max_sum, len(words[i]) * len(words[j]))
        
    return max_sum


def test_max_productd_1():
    result = max_product(["abcw","baz","foo","bar","xtfn","abcdef"])
    assert result == 16