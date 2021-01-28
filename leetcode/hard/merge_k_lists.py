class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def merge_k_lists(self, lists) -> ListNode:
        if not lists:
            return None

        if len(lists) < 2:
            return lists[0]

        heap = []
        for list in lists:
            next = list
            while next:
                heap.append(next.val)
                next = next.next
                
        if not heap:
            return None

        self.build_heap(heap)

        head = ListNode(self.pop(heap))
        self.heapify(heap, 1)

        next = head
        while heap[0] < 2 ** 31 - 1:
            next.next = ListNode(self.pop(heap))
            next = next.next
            self.heapify(heap, 1)

        return head

    def heapify(self, heap, index):
        left_index = self.left(index)
        right_index = self.right(index)

        smalest = index
        if left_index <= len(heap) and heap[left_index-1] < heap[smalest-1]:
            smalest = left_index

        if right_index <= len(heap) and heap[right_index-1] < heap[smalest-1]:
            smalest = right_index

        if smalest != index:
            self.swap(index-1, smalest-1, heap)
            self.heapify(heap, smalest)

    def build_heap(self, arr):
        for i in range(len(arr) // 2, 0, -1):
            self.heapify(arr, i)

    def pop(self, heap):
        top = heap.pop(0)
        heap.insert(0, 2 ** 31 - 1)
        return top

    def swap(self, x, y, arr):
        tmp = arr[x]
        arr[x] = arr[y]
        arr[y] = tmp

    def left(self, i):
        return i * 2

    def right(self, i):
        return (i * 2) + 1

def test_example2():

    # [[-1,1],[-3,1,4],[-2,-1,0,2]]
    list1 = ListNode(-1)
    list1.next = ListNode(1)

    list2 = ListNode(-3)
    list2.next = ListNode(1)
    list2.next.next = ListNode(4)

    list3 = ListNode(-2)
    list3.next = ListNode(-1)
    list3.next.next = ListNode(0)
    list3.next.next.next = ListNode(2)

    lists = [list1, list2, list3]
    result = Solution().merge_k_lists(lists)
    
    arr = []
    next = result
    while next:
        arr.append(next.val)
        next = next.next

    assert arr == [-3,-2,-1,-1,0,1,1,2,4]
    

def test_example():

    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    list3 = ListNode(2)
    list3.next = ListNode(6)

    lists = [list1,list2,list3]
    result = Solution().merge_k_lists(lists)
    
    arr = []
    next = result
    while next:
        arr.append(next.val)
        next = next.next

    assert arr == [1,1,2,3,4,4,5,6]


def test_example1():

    # [[1,2,3],[4,5,6,7]]
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)

    list2 = ListNode(4)
    list2.next = ListNode(5)
    list2.next.next = ListNode(6)
    list2.next.next.next = ListNode(7)

    lists = [list1,list2]
    result = Solution().merge_k_lists(lists)
    
    arr = []
    next = result
    while next:
        arr.append(next.val)
        next = next.next

    assert arr == [1,2,3,4,5,6,7]