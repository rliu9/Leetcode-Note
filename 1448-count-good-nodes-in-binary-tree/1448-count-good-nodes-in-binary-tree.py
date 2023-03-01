# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root, Max):
            if not root:return
            m = Max
            if root.val >= Max:
                self.res += 1
                m = root.val
            dfs(root.left, m)
            dfs(root.right, m)
        dfs(root, root.val)
        return self.res
    
    # O(n)
    # O(n)
        
                