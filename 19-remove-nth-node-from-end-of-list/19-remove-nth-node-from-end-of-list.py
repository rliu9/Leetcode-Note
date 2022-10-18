# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = dummy_head = ListNode(next=head)
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy_head.next
    
        #O(n)
        #O(1)