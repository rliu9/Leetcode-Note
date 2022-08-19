# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = prev = ListNode(next=head)
        while prev.next and prev.next.next:
            cur = prev.next
            nxt = prev.next.next
            prev.next = nxt
            cur.next = nxt.next
            nxt.next = cur
            prev = prev.next.next
        return dummy_head.next