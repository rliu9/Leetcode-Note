# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first = first_dummy = ListNode()
        second = second_dummy = ListNode()
        while head:
            if head.val >= x:
                second.next = ListNode(head.val)
                second = second.next
            else:
                first.next = ListNode(head.val)
                first = first.next
            head = head.next
        first.next = second_dummy.next
        return first_dummy.next