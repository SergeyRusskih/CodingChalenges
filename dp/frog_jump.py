def frog_jump(stones):

    arr = [[False for i in range(len(stones))] for j in range(len(stones))]
    arr[0][1] = True

    for i in range(1, len(stones)):
        for j in range(0, i):
            diff = stones[i]-stones[j]
            if diff < 0 or diff >= len(stones) or arr[j][diff] == False:
                continue

            arr[i][diff] = True

            if diff-1 >= 0:
                arr[i][diff-1] = True

            if diff+1 < len(stones):
                arr[i][diff+1] = True

            if i == len(stones)-1:
                return True

    return False

def test_3():
    assert not frog_jump([0,1,3,6,7])

def test_1():
    assert frog_jump([0,1,3,5,6,8,12,17])

def test_2():
    assert not frog_jump([0,1,2,3,4,8,9,11])