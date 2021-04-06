class Number:
    def __init__(self, last, count):
        self.last = last
        self.count = count

def dail_pad(n):

    count = 0
    lst = [ Number(item[0], 1) for item in get_map().items() ]

    while len(lst) != 0:
        current = lst.pop()

        if current.count is n:
            count += 1
        else:
            next = get_next(current.last)
            for x in next:
                lst.append(Number(x, current.count + 1))

    return count

def get_next(i):
    return get_map()[i]

def get_map():
    return {
        '1': [ '6', '8' ],
        '2': [ '7', '9' ],
        '3': [ '4', '8' ],
        '4': [ '3', '9', '0' ],
        '5': [      ],
        '6': [ '1', '7', '0'],
        '7': [ '2', '6' ],
        '8': [ '1', '3' ],
        '9': [ '2', '4' ],
        '0': [ '4', '6'  ]
    }
    
def test_dail_pad_1():
    result = dail_pad(1)
    assert result == 10

def test_dail_pad_2():
    result = dail_pad(2)
    assert result == 20

def test_dail_pad_3():
    result = dail_pad(3)
    assert result == 46

def test_dail_pad_4():
    result = dail_pad(4)
    assert result == 104

def test_dail_pad_3131():
    result = dail_pad(3131)
    assert result == 136006598\