class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        new_node = ListNode(val)
        if index <= 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
            
        self.size -= 1

if __name__ == '__main__':
    import unittest

    class TestMyLinkedList(unittest.TestCase):
        def test_scenario(self):
            myLinkedList = MyLinkedList()
            myLinkedList.addAtHead(1)
            myLinkedList.addAtTail(3)
            myLinkedList.addAtIndex(1, 2)
            self.assertEqual(myLinkedList.get(1), 2)
            myLinkedList.deleteAtIndex(1)
            self.assertEqual(myLinkedList.get(1), 3)

    unittest.main()