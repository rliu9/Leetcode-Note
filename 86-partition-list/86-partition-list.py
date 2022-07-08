# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = left_dummy = ListNode()
        right = right_dummy = ListNode()
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        right.next = None
        left.next = right_dummy.next
        return left_dummy.next
    
    # Time Complexity: O(n)
    # Space Complexity: O(1) -> two dummy nodes and no extra space