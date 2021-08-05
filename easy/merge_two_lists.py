class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = current = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                current.next = ListNode(l1.val)
                current = current.next
            else:
                current.next = ListNode(l2.val)
                current = l2.next

        current.next = l1 or l2
        return result.next