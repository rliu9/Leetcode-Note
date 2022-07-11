"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(root):
            if not root:return
            for i in root.children:
                dfs(i)
                res.append(i.val)
        dfs(root)
        if root:res.append(root.val)
        return res