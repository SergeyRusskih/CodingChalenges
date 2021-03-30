def repeated_dna(s):

    if len(s) <= 10:
        return []

    hashes = set()
    added = set()
    result = []
    for i in range(len(s)):
        substring = s[i:10+i]
        if substring in hashes and substring not in added:
            result.append(substring)
            added.add(substring)
        else:
            hashes.add(substring)

    return result

def test_example():
    result = repeated_dna("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    assert result == ["AAAAACCCCC","CCCCCAAAAA"]

def test_example_1():
    result = repeated_dna("AAAAAAAAAAAAA")
    assert result == ["AAAAAAAAAA"]