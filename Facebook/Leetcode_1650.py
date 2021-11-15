"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        cur_p, cur_q = p, q
        while cur_p != cur_q:
            cur_p, cur_q = cur_p.parent, cur_q.parent
            if not cur_p: cur_p = q
            if not cur_q: cur_q = p
        return cur_p
