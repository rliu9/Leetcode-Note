# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = cur = ListNode(0)
        carry = 0
        while l1 or l2:
            value = carry
            carry = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            while value >= 10:
                carry += 1
                value %= 10
            cur.next = ListNode(value)
            cur = cur.next
        if carry:cur.next = ListNode(carry)
        return dummy_head.next
    
    # Time Complexity: O(max(m,n))
    # Space Complexity: O(max(m,n))
    
if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2)
    l1.next, l1.next.next = ListNode(4), ListNode(3)
    l2 = ListNode(5)
    l2.next, l2.next.next = ListNode(6), ListNode(4)
    print(s.addTwoNumbers(l1, l2))