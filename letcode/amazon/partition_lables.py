def partition_lables(str):
    intervals = {}
    for i in range(len(str)):
        if str[i] in intervals:
            j, _ = intervals[str[i]]
            intervals[str[i]] = (j, i)
            

def test_example():
    assert partition_lables('ababcbacadefegdehijhklij') == [9,7,8]
