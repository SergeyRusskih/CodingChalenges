def longest_awesome(str):

    memo = dict()
    odd_count = 0

#111
#101
#1101
#221115 -> 
    for i in range(len(str)):
        odd_count = add_letter(memo, str[i], odd_count)

    if is_awsome(len(str), odd_count):
        return len(str)

    longest = 1
    for i in range(len(str)):
        tmp_odd_count = odd_count
        tmp_memo = memo.copy()
        for j in range(len(str), i, -1):
            letter = str[j-1]
            tmp_odd_count = substract_letter(tmp_memo, letter, tmp_odd_count)
            if is_awsome(j - i, tmp_odd_count) and j - i > longest:
                longest = j - i

        odd_count = substract_letter(memo, str[i], odd_count)

    return longest

def add_letter(memo, letter, count):
    if letter in memo:
        memo[letter] += 1
        if memo[letter] % 2 == 0:
             return count - 1
        return count + 1

    memo[letter] = 1
    return count + 1

def substract_letter(memo, letter, count):
    memo[letter] -= 1
    if memo[letter] == 0:
        memo.pop(letter)
        return count - 1

    if memo[letter] % 2 == 0:
        return count - 1
    
    return count + 1


def is_awsome(str_length, odd_count):
    if str_length % 2 == 0:
        if odd_count == 0:
            return True
        return False
    elif odd_count == 1:
        return True
    
    return False

def test_example_basic():
    longest_awesome("1") == 1

def test_example_simple():
    longest_awesome("10") == 1

def test_example_101():
    longest_awesome("101") == 3

def test_example_1():
    longest_awesome("3242415") == 5

def test_example_2():
    longest_awesome("12345678") == 1

def test_example_3():
    longest_awesome("213123") == 6