# Given the head of a linked list, rotate the list to the right by k places.
#
# https://leetcode.com/problems/rotate-list/
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_right(head, k):
    if not head or not head.next:
        return head
        
    arr = []
    current = head
    while current :
        arr.append(current.val)
        current = current.next

    if k > len(arr):
        k %= len(arr)
    elif k == len(arr):
        return head

    for _ in range(k):
        last = arr.pop()
        arr.insert(0, last)

    current = head
    for item in arr:
        current.val = item
        current = current.next

    return head

def test_1():
    result = rotate_right(ListNode(0, ListNode(1, ListNode(2))), 4)