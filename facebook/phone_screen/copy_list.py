# https://leetcode.com/problems/copy-list-with-random-pointer/

class Node:
    def __init__(self, x: int, next: None, random: None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(head):
    memo = dict()
    m = n = head
    while m:
        memo[m] = Node(m.val, None, None)
        m = m.next

    while n:
        memo[n].next = memo.get(n.next)
        memo[n].random = memo.get(n.random)
        n = n.next

    return memo.get(head)
        


def test_example_1():
    result = copy_random_list([[7,null],[13,0],[11,4],[10,2],[1,0]])
    assert result == [[7,null],[13,0],[11,4],[10,2],[1,0]]

def test_example_2():
    node1 = Node(1, None, None)
    node1.random = node1
    node2 = Node(2, None, node1)
    node1.next = node2

    result = copy_random_list(node1)
    assert result == node1

def test_example_3():
    result = copy_random_list([[3,null],[3,0],[3,null]])
    assert result == [[3,null],[3,0],[3,null]]