def is_balanced(str):
    opened = {"(", "[", "{"}
    closed = {")": "(", "]": "[", "}": "{"}
    
    letters = []
    is_open = True
    for i, letter in enumerate(str):
        if letter in opened:
            if not is_open:
                return i
            letters.append(letter)
        elif letter in closed:
            is_open = False
            if len(letters) == 0 or letters.pop() != closed[letter]:
                return i
    return -1



def test_1():
    assert is_balanced("{abcd}") == -1

def test_2():
    assert is_balanced("(adfbf)(a)") == 7

def test_3():
    assert is_balanced(r"(abc{[d]})") == -1

def test_4():
    assert is_balanced(r"(abc{[d]})[]") == 10