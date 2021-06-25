# https://leetcode.com/problems/generate-parentheses/
def generate_parentheses(n):
    result = []
    def generate(candidate, open, closed):
        if len(candidate) == n * 2:
            result.append(candidate)
        elif open == n:
            generate(candidate + ")", open, closed+1)
        elif open == closed:
            generate(candidate + "(", open+1, closed)
        else:
            generate(candidate + ")", open, closed+1)
            generate(candidate + "(", open+1, closed)

    generate("", 0, 0)
    return result

def test_1():
    result = generate_parentles(3)
    assert result == ["()()()","()(())","(())()","(()())","((()))"]

def test_2():
    result = generate_parentles(1)
    assert result == ["()"]