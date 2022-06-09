# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        fast = slow = dummy_head
        for _ in range(n):
            fast = fast.next
            if not fast: return fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_head.next
    
    def arr2linkedList(self, arr):
        cur = dummy_head = ListNode(0)
        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy_head.next
    
"""
time complexity: O(L)   L is # of nodes in the list
space complexity: O(1)

let faster pointer go n steps first, then the gap between lower and faster pointer would be n
when faster pointer reach the end, the slower pointer reach the nth node from the end of list
So, we can find the target by one traversal
"""
    
if __name__ == '__main__':
    s = Solution()
    head = s.removeNthFromEnd(s.arr2linkedList([1,2,3,4,5]), 2)
    check = s.arr2linkedList([1,2,3,5])
    while head:
        assert head.val == check.val
        head = head.next
        check = check.next
    assert head == check == None
        
