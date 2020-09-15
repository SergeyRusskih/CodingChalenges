from .singly_linked_list import SinglyLinkedList

def remove_duplicates(list):
    values_set = set()
    next = list.head
    while next != None:
        if next.data not in values_set:
            values_set.add(next.data)
        next = next.next

    item = values_set.pop()
    new_linked_list = SinglyLinkedList(item)

    while len(values_set) != 0:
        item = values_set.pop()
        new_linked_list.add_node(item)
        
    return new_linked_list

def test_remove_duplicates():
    list = SinglyLinkedList(0)
    list.add_node(1)
    list.add_node(0)
    list.add_node(2)
    list.add_node(1)

    result = SinglyLinkedList(0)
    result.add_node(1)
    result.add_node(2)

    assert remove_duplicates(list) == result