import queue as queue

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

'''
      3
    /  \
    1    2
   /    / \
 -2    4   5
          / \
             7

[3, 1, 2, -2, None, 4, 5, None, None, None, None, None, None, 7]

x = 0 or 1 (left or right)
y = depth 
'''

def tree_to_array(tree):
    total_depth = calculate_depth(tree)
    arr = [None] * ((2 ** total_depth) - 1)

    q = queue.Queue()
    q.put(tree)

    count = 0
    while len(arr) != count:
        item = q.get()
        if item == None:
            q.put(None), q.put(None)
            arr[count] = None
        else:
            q.put(item.left), q.put(item.right)
            arr[count] = item.data


        count += 1

    return arr


def calculate_depth(node, count = 0) -> int:
    if node == None:
        return count
    
    count += 1
    left_length = calculate_depth(node.left, count)
    right_length = calculate_depth(node.right, count)

    return max(left_length, right_length)

def test_example():
    seven = Node(7, None, None)
    five = Node(5, None, seven)
    four = Node(4, None, None)
    two = Node(2, four, five)
    minus_two = Node(-2, None, None)
    one = Node(1, minus_two, None)
    three = Node(3, one, two) 

    assert tree_to_array(three) == [
        3, 1, 2, -2, None, 4, 5, None, None, None, None, None, None, None, 7
    ]
