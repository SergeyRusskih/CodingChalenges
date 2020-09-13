def compress(string):
    if len(string) < 2:
        return string

    prev = string[0]
    count = 1
    result = ""
    for i in range(1, len(string)):
        current = string[i]
        if current == prev:
            count += 1
            if i != len(string) - 1:
                continue
        result += prev + str(count)
        prev = current
        count = 1
    
    if len(result) < len(string):
        return result
    
    return string

def test_example():
    assert compress("aabcccccaaa") == "a2b1c5a3"

def test_compression_not_needed():
    assert compress("aabb") == "aabb"

def test_compression_not_needed():
    assert compress("aabbcd") == "aabbcd"