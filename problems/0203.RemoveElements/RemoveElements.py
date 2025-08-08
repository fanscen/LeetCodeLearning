# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to handle cases where the head needs to be removed.
        dummy = ListNode(next=head)
        current = dummy
        
        # Iterate through the list
        while current.next:
            if current.next.val == val:
                # Skip the node with the target value
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
                
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    items = []
    current = head
    while current:
        items.append(str(current.val))
        current = current.next
    print(" -> ".join(items))

if __name__ == '__main__':
    s = Solution()

    # Test Case 1
    head1 = create_linked_list([1,2,6,3,4,5,6])
    print("Original list:")
    print_linked_list(head1)
    result1 = s.removeElements(head1, 1)
    print("After removing 6:")
    print_linked_list(result1)
    print("-" * 20)

    # Test Case 2
    head2 = create_linked_list([])
    print("Original list:")
    print_linked_list(head2)
    result2 = s.removeElements(head2, 1)
    print("After removing 1:")
    print_linked_list(result2)
    print("-" * 20)

    # Test Case 3
    head3 = create_linked_list([7,7,7,7])
    print("Original list:")
    print_linked_list(head3)
    result3 = s.removeElements(head3, 7)
    print("After removing 7:")
    print_linked_list(result3)
    print("-" * 20)