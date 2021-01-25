class ListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Solution:

    def merge_k_lists(self, lists: [ListNode]):
        if not lists:
            return []

        if len(lists) < 2:
            return lists[0]

        heap = []
        for list in lists:
            for item in list:
                heap.insert(0, item)
                self.heapify(heap, 1)

        head = ListNode(heap.pop(0), None)
        self.heapify(heap, 1)

        next = head
        while len(heap) > 0:
            next.next = ListNode(heap.pop(0), None)
            next = next.next
            self.heapify(heap, 1)

        return head

    def heapify(self, heap, index):
        left_index = self.left(index)
        right_index = self.right(index)

        smalest = index
        if left_index <= len(heap) and heap[left_index-1] < heap[index-1]:
            smalest = left_index

        if right_index <= len(heap) and heap[right_index-1] < heap[index-1]:
            smalest = right_index

        if smalest != index:
            self.swap(index-1, smalest-1, heap)
            self.heapify(heap, smalest)

    def swap(self, x, y, arr):
        tmp = arr[x]
        arr[x] = arr[y]
        arr[y] = tmp

    def left(self, i):
        return i * 2

    def right(self, i):
        return (i * 2) + 1
    