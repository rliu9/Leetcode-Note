# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        cur = dummy_head
        carry = 0
        while l1 or l2:
            nxt = carry
            if l1:
                nxt += l1.val
                l1 = l1.next
            if l2:
                nxt += l2.val
                l2 = l2.next
            carry = 0
            if nxt >= 10:
                carry = 1
                nxt = nxt % 10
            cur.next = ListNode(nxt)
            cur = cur.next
        if carry > 0:cur.next = ListNode(carry)
        return dummy_head.next