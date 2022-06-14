"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        d = {}
        def dfs(root, depth):
            if not root: return
            if depth in d:
                d[depth].next = root
            root.next = None
            d[depth] = root
            if root.left: dfs(root.left, depth+1)
            if root.right: dfs(root.right, depth+1)
        dfs(root, 0)
        return root