# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = jump = ListNode(next=head)
        left = right = head
        while True:
            i = 0
            while right and i < k:
                right = right.next
                i += 1
            if i == k:
                pre, cur = right, left
                for _ in range(k):
                    cur.next, pre, cur = pre, cur, cur.next
                jump.next, jump, left = pre, left, right
                    
            else:
                return dummy.next
                
            