from .node import Node

class SinglyLinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def add_node(self, data):
        if self.head == None:
            self.head = Node(data)
            return

        next = self.head
        while next.next != None:
            next = next.next
        next.next = Node(data)

    def delete_node(self, data):
        next = self.head
        if next == None or next.next == None:
            return

        while next.next.data != data:
            next = next.next

        next.next = next.next.next

    def __eq__(self, other):
        self_head = self.head
        other_head = other.head
        while self_head != None and other_head != None:
            if self_head.data != other_head.data:
                return False
            self_head = self_head.next
            other_head = other_head.next
        if self_head == None and other_head == None:
            return True
        return False


def test_delete_node():
    list1 = SinglyLinkedList(0)
    list1.add_node(1)
    list1.add_node(2)

    list2 = SinglyLinkedList(0)
    list2.add_node(2)

    list1.delete_node(1)

    assert list1.__eq__(list2)