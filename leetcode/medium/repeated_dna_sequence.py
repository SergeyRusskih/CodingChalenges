def repeated_dna(s):
    dna_length = 10
    if len(s) <= dna_length:
        return []

    sums = [0]
    for i in range(len(s)):
        if i < dna_length:
            sum[0] += hash(s[i])
        else:
            sum.append(hash(s[i] - sum[i - dna_length]))

  
    pass

def test_example():
    result = repeated_dna("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    result assert ["AAAAACCCCC","CCCCCAAAAA"]

def test_example_1():
    result = repeated_dna("AAAAAAAAAAAAA")
    result assert ["AAAAAAAAAA"]