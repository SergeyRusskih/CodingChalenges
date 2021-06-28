# valid ip address - from 0.0.0.0 to 255.255.255.255
# valid ip segment
#  - from 0 to 255
#  - cannot start with 0
#  - can be 0
#  - can create segment if
#    - num of segments >= remaining length
#    - num of segments * 3 <= remaining length

# https://leetcode.com/problems/restore-ip-addresses/

def restore_ip(s):
    if len(s) < 4 or len(s) > 12:
        return []

    ips = []
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                for d in range(1, 4):
                    if a+b+c+d == len(s):
                        A = int(s[:a])
                        B = int(s[a:a+b])
                        C = int(s[a+b:a+b+c])
                        D = int(s[a+b+c:a+b+c+d])
                        if A <= 255 and B <= 255 and C <= 255 and D <= 255:
                            ip = f"{A}.{B}.{C}.{D}" 
                            if len(ip) == len(s)+3:
                                ips.append(ip)
    return ips

def test_1():
    result = restore_ip("25525511135")
    assert result == ["255.255.11.135","255.255.111.35"]

def test_2():
    result = restore_ip("0000")
    assert result == ["0.0.0.0"]

def test_3():
    result = restore_ip("1111")
    assert result == ["1.1.1.1"]

def test_4():
    result = restore_ip("010010")
    assert result == ["0.10.0.10","0.100.1.0"]

def test_5():
    result = restore_ip("101023")
    assert result == ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]