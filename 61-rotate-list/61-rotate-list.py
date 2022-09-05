# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:return
        if not head.next:return head

        pointer = head
        n = 1
        while pointer.next:
            pointer = pointer.next
            n += 1
        rotateTimes = k%n

        if k == 0 or rotateTimes == 0:return head

        fastPointer = slowPointer = head

        for _ in range(rotateTimes):fastPointer = fastPointer.next

        while fastPointer.next:
            slowPointer,fastPointer = slowPointer.next, fastPointer.next

        temp = slowPointer.next
        slowPointer.next = None
        fastPointer.next = head
        head = temp

        return head
        