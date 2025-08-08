from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swaps adjacent nodes in a linked list.
        """
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = prev.next.next

            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # Move to the next pair
            prev = first
        
        return dummy.next

# Helper functions for testing
def list_to_linkedlist(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

def linkedlist_to_list(head):
    items = []
    current = head
    while current:
        items.append(current.val)
        current = current.next
    return items

if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        {"input": [1, 2, 3, 4], "expected": [2, 1, 4, 3]},
        {"input": [], "expected": []},
        {"input": [1], "expected": [1]},
        {"input": [1, 2, 3], "expected": [2, 1, 3]},
    ]

    for i, tc in enumerate(test_cases):
        head = list_to_linkedlist(tc["input"])
        swapped_head = solution.swapPairs(head)
        result = linkedlist_to_list(swapped_head)
        if result == tc["expected"]:
            print(f"Test case {i + 1} passed.")
        else:
            print(f"Test case {i + 1} failed. Expected {tc['expected']}, got {result}")