def string_remutation(input):
    
    result = []
    def dfs(i, value):
        if i == len(value):
            result.append(value)
            return

        for j in range(i, len(value)):
            dfs(i + 1, swap(i, j, value))

    def swap(i, j, value):
        new_value = list(value)
        tmp = new_value[i]
        new_value[i] = new_value[j]
        new_value[j] = tmp
        return new_value

    dfs(0, list(input))
    return [ "".join(item) for item in result ]

def test_simple():
    result = string_remutation("ABC")
    assert result == [
        'ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB'
    ]