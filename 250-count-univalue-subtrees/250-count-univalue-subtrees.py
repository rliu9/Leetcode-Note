# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:return True
            left,right = dfs(root.left),dfs(root.right)
            if left and right and (not root.left or root.left.val==root.val) and (not root.right or root.right.val==root.val):
                self.res += 1
                return True
        if not root:return 0
        dfs(root)
        return self.res
    
    # O(n)
    # O(h)