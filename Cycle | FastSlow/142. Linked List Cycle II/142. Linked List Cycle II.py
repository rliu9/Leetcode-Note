# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cur = slow
                while cur != head:
                    head = head.next
                    cur = cur.next
                return cur
        return
    
    # time complexity: O(n)
    # space complexity: O(1)
    
    """
    F is # of nodes outside of the cycle
    C is the length of cycle
    a is the first intersection
    n is some integer
    
    fast pointer has traversed twice as many nodes as the low pointer 
    -> distance: 2*low = fast -> 2(F+a) = F+a+nC -> F = nC-a
    
    head goes F steps, it's the entrence
    the intersection goes nC-a steps, its also the entrence
    """
